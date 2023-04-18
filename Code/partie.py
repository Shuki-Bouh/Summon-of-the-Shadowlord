from random import randrange, choice, random
import Code.personnage as perso
import sqlite3

class Partie(list):
    """Dans self sera contenu les ennemis avec les joueurs (à la position prévue)"""

    def __init__(self, l: int, h: int):
        list().__init__()
        self.__h = h + 2  # Pour compenser les False qui apparaissent
        self.__l = l + 2
        self.__generation_map()
        self.joueurs = {}
        self.ennemis = {}
        self.disparition = []
        self.limiteSpawn = 5
        self.multi = False

    def __generation_map(self):
        """Ne doit pas être appelé en dehors de la classe. Il crée la forme générale de la map (static array)"""
        for x in range(self.l):
            self.append([])
            for y in range(self.h):
                if x == 0 or x == self.l - 1 or y == 0 or y == self.h - 1:
                    self[x].append(False)
                else:
                    self[x].append(None)

    def new_player(self, nom: str, classe: str, niveau=1, pos=()):
        """Création d'un nouveau joueur selon la classe sélectionnée par le joueur"""
        differentes_classes = {'epeiste': perso.Epeiste,
                               'garde': perso.Garde,
                               'sorcier': perso.Sorcier,
                               'archer': perso.Archer}
        classe = differentes_classes[classe]
        if not self.multi:
            if pos == ():
                classe(self, (self.l // 2, self.h - self.h // 4), nom, niveau=niveau)
            else:
                classe(self, pos, nom, niveau=niveau)
        else:
            pass  # On l'implémentera plus tard
        return

    @property
    def h(self):
        """Ces getter permet d'empêcher la modification de h et l (moyen de faire un int const h, l ...)"""
        return self.__h

    @property
    def l(self):
        return self.__l

    def spawn_ennemi(self):
        """Fais apparaître des ennemis de type aléatoire sur la map
        La position est aléatoire sur les cases disponibles"""
        if perso.Ennemi.compteur < self.limiteSpawn:
            lv = list(self.joueurs.values())[0].niveau  # ça commence à être moche
            lvl = lv + randrange(-2, 3)
            proba = random()
            if proba < 0.4:
                self.spawn('squelette', lvl)
            elif 0.4 <= proba < 0.8:
                self.spawn('crane', lvl)
            elif 0.8 <= proba < 0.9:
                self.spawn('invocateur', lvl)
            else:
                self.spawn('armure', lvl)
            return True

    def spawn(self, classe: str, niveau: int, pos=()):
        """Le paramètre pos=() ne sert que pour les spawn de crânes dans l'attaque spéciale de l'Invocateur"""
        ennemi = {'squelette': perso.Squelette,
                  'crane': perso.Crane,
                  'invocateur': perso.Invocateur,
                  'armure': perso.Armure}
        ennemi = ennemi[classe]  # On change le type de ennemi pour avoir directement la classe d'ennemi qu'on va générer
        if pos == ():
            cases_possibles = []
            for i in range(self.l):
                for j in range(self.h):
                    if self[i][j] is None:
                        cases_possibles.append((i, j))
            pos = choice(cases_possibles)
        ennemi(self, pos, niveau)

    @staticmethod
    def create_save():
        # Création du fichier si inexistant, ouverture sinon
        connexion = sqlite3.connect('./_Save/Base_de_données.db')
        # Création des tables
        cursor = connexion.cursor()  # Pour manipuler les BDD
        cursor.execute("""
               CREATE TABLE IF NOT EXISTS Partie(
                   id_partie INT(4) NOT NULL UNIQUE,
                   temps_jeu HOUR NOT NULL,
                   nb_mort INT(2) NOT NULL CHECK (nb_mort <= 99),
                   nb_kill INT NOT NULL,
                   nb_squelette INT NOT NULL,
                   nb_crane INT NOT NULL,
                   nb_armure INT NOT NULL,
                   nb_invocateur INT NOT NULL,
                   vivant INT(1) NOT NULL CHECK (vivant IN (0, 1)),
                   CONSTRAINT PK_partie PRIMARY KEY (id_partie)
               )""")
        connexion.commit()
        cursor.execute("""  
                       CREATE TABLE IF NOT EXISTS Joueurs(
                           nom VARCHAR(12) NOT NULL UNIQUE,
                           id_partie INT(4) NOT NULL UNIQUE,
                           classe VARCHAR(7) NOT NULL CHECK (classe IN ('epeiste', 'garde', 'sorcier', 'archer')),
                           niveau INT(2) NOT NULL CHECK (niveau <= 20),
                           pos_x INT(2) NOT NULL,
                           pos_y INT(2) NOT NULL,
                           potion INT(1) CHECK (potion <= 5),
                           argent INT(4) CHECK (argent <= 9999),
                           CODEX INT(1) CHECK (CODEX IN (0, 1)),
                           CONSTRAINT PK_Joueurs PRIMARY KEY (nom),
                           CONSTRAINT FK_Joueurs_Partie FOREIGN KEY (id_partie)
                           REFERENCES Partie(id_partie)
                       )""")
        connexion.commit()
        # Fermeture de la connexion
        connexion.close()

    def write_save(self, name):
        """Permet de sauvegarder, et de créer la sauvegarde si c'est la première partie."""
        try:
            open('./_Save/Base_de_données.db')
        except FileNotFoundError:
            Partie.create_save()
        else:
            # Récupération des valeurs nécessaire pour la suite
            player = self.joueurs[str(name)]
            kill_squelette = perso.Squelette.total_compteur - perso.Squelette.compteur
            kill_crane = perso.Crane.total_compteur - perso.Crane.compteur
            kill_armure = perso.Armure.total_compteur - perso.Armure.compteur
            kill_invocateur = perso.Invocateur.total_compteur - perso.Invocateur.compteur
            kill = kill_squelette + kill_crane + kill_armure + kill_invocateur

            # A implémenter ?
            temps_jeu = 0
            compteur_mort = 0

            # Ouverture du fichier
            connexion = sqlite3.connect('./_Save/Base_de_données.db')
            # Test pour savoir si le joueur a déjà une sauvegarde dans la table
            cursor = connexion.cursor()
            cursor.execute("""SELECT nom FROM Joueurs WHERE nom=?""", (player.nom,))
            result = cursor.fetchone()
            if result == None:  # Pas de sauvegarde existante
                cursor = connexion.cursor()
                cursor.execute("""SELECT id_partie FROM Partie""")
                id_values = cursor.fetchall()
                id_prt = 1
                if len(id_values) != 0:  # idée créée de manière itérative
                    id_prt = id_values[-1][0] + 1
                # On crée la sauvegarde de la partie et du joueur
                cursor.execute("""
                INSERT INTO Joueurs(nom, id_partie, classe, niveau, pos_x, pos_y, potion, argent, CODEX)
                VALUES(?,?,?,?,?,?,?,?,?)""", (player.nom, id_prt, player.classe, player.niveau, player.position[0],
                                               player.position[1], 0, 0, 0,))
                connexion.commit()
                cursor.execute("""
                INSERT INTO Partie(id_partie, temps_jeu, nb_mort, nb_kill, nb_squelette, nb_crane, nb_armure,
                nb_invocateur, vivant) VALUES(?,?,?,?,?,?,?,?,?)""", (id_prt, temps_jeu, compteur_mort, kill,
                                                                      kill_squelette, kill_crane, kill_armure,
                                                                      kill_invocateur, player.vivant,))
                connexion.commit()
                print("4")
            else:  # Sauvegarde existante
                cursor = connexion.cursor()
                cursor.execute("""SELECT id_partie FROM Joueurs WHERE nom=?""", (player.nom,))
                id_prt = list(cursor.fetchone())[0]
                # Suppression anciennes données
                cursor.execute("""DELETE FROM Joueurs WHERE nom=?""", (player.nom,))
                cursor.execute("""DELETE FROM Partie WHERE id_partie=?""", (id_prt,))
                cursor.execute("""
                INSERT INTO Joueurs(nom, id_partie, classe, niveau, pos_x, pos_y, potion, argent, CODEX) 
                VALUES(?,?,?,?,?,?,?,?,?)""",
                               (player.nom, id_prt, player.classe, player.niveau,
                                player.position[0], player.position[1], 0, 0, 0,))
                connexion.commit()
                cursor.execute("""
                INSERT INTO Partie(id_partie, temps_jeu, nb_mort, nb_kill, nb_squelette, nb_crane, nb_armure,
                nb_invocateur, vivant) VALUES(?,?,?,?,?,?,?,?,?)""", (id_prt, temps_jeu, compteur_mort, kill,
                                                                      kill_squelette, kill_crane, kill_armure,
                                                                      kill_invocateur, player.vivant,))
                connexion.commit()
            # Fermeture de la connexion
            connexion.close()

    @staticmethod
    def destroy_dbb():
        try:
            open('./_Save/Base_de_données.db')
        except FileNotFoundError:
            Partie.create_save()  # Dans le cadre où la sauvegarde n'existe pas encore
        else:
            connexion = sqlite3.connect('./_Save/Base_de_données.db')
            cursor = connexion.cursor()
            cursor.execute("""DROP TABLE Joueurs""")
            connexion.commit()
            cursor.execute("""DROP TABLE Partie""")
            connexion.commit()

    @staticmethod
    def lecture_perso():
        try:
            open('./_Save/Base_de_données.db')
        except FileNotFoundError:
            Partie.create_save()  # Dans le cadre où la sauvegarde n'existe pas encore
        else:
            connexion = sqlite3.connect('./_Save/Base_de_données.db')
            cursor = connexion.cursor()
            cursor.execute("""SELECT * FROM Joueurs""")
            result = cursor.fetchall()
            return result

    def suppr_ennemi(self):
        """Suppression des objets Ennemi"""
        while len(self.disparition) > 0:
            mechant = self.disparition.pop()
            del self.ennemis[mechant.nom]  # On vide le dictionnaire
            del mechant  # On supprime l'objet pour un peu de performance

    def action_mechant(self):
        """Dans cette fonction, on gère les actions de chaque ennemi, cette fonction est appelée par QTimer par la suite
        (On voulait la mettre sur un thread à part mais PyQt n'apprécie pas tellement)"""
        self.spawn_ennemi()  # On fait apparaitre les ennemis à chaque iteration s'il n'y en a pas assez
        for mechant in self.ennemis.values():
            if mechant.portee():  # Attaque ssi le joueur est assez proche
                mechant.attaquer()
            else:
                mechant.deplacement()  # Sinon il essaie de se rapprocher
            mechant.agro()  # Quoi qu'il arrive, il essaie de taper le joueur le plus proche donc sa cible est
            # réactualisé à chaque iteration

    def __str__(self):
        """Permet d'afficher le jeu sur terminal, mais le terminal n'est pas assez efficace pour afficher 24 fps..."""
        canvas = ""
        for y in range(self.h):
            for x in range(self.l - 1):
                a = str(self[x][y])
                while len(a) < 12:
                    a += " "
                canvas += a + " "
            canvas += str(self[self.l - 1][y])
            canvas += "\n"
        return canvas


if __name__ == '__main__':
    pass

