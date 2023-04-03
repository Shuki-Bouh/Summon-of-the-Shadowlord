import time
from random import randrange, choice, random
import Code.personnage as perso
import threading
import os
import sqlite3

path = os.getcwd()
path += "\\Data"
os.chdir(path)

class Partie(list):
    """dans self sera contenu les ennemis avec les joueurs (à la position prévue)"""

    def __init__(self, l, h):
        super().__init__()
        self.__h = h + 2  # Pour compenser les False qui apparaissent
        self.__l = l + 2
        self.__generation_map()
        self.map = self.get_map()
        self.joueurs = {}
        self.ennemis = {}
        self.disparition = []
        self.limite_spawn = 5
        self.multi = False
        self.thread_ennemis = threading.Thread(target=self.action_mechant)
        self.mutex = threading.Lock()

    def __generation_map(self):
        for x in range(self.l):
            self.append([])
            for y in range(self.h):
                if x == 0 or x == self.l - 1 or y == 0 or y == self.h - 1:
                    self[x].append(False)
                else:
                    self[x].append(None)

    def new_player(self, nom, classe, niveau=1, pos=()):
        differentes_classes = {'epeiste': perso.Epeiste,
                               'garde': perso.Garde,
                               'sorcier': perso.Sorcier,
                               'druide': perso.Druide}
        classe = differentes_classes[classe]
        if not self.multi:
            if pos == ():
                joueur = classe(self, (self.l - self.l // 4, self.h // 2), nom, niveau=niveau)
            else:
                joueur = classe(self, pos, nom, niveau=niveau)
        else:
            pass  # On l'implémentera plus tard
        return

    @property
    def h(self):
        return self.__h

    @property
    def l(self):
        return self.__l

    def get_map(self):
        """Ca permet de faire le lien entre personnage et partie (en appelant la map dans personnage)"""
        return self

    def spawn_ennemi(self, niveau):
        if perso.Ennemi.compteur < self.limite_spawn:
            proba = random()
            if proba < 0.4:
                self.spawn_squelette(niveau)
            elif 0.4 <= proba < 0.8:
                self.spawn_crane(niveau)
            elif 0.8 <= proba < 0.9:
                self.spawn_invocateur(niveau)
            else:
                self.spawn_armure(niveau)
            return True

    def spawn_squelette(self, niveau, pos=()):
        """Le paramètre pos=() ne sert que pour les spawn de crânes dans l'attaque spéciale de l'Invocateur"""
        if pos != ():
            x, y = pos[0], pos[1]
        else:
            cases_possibles = []
            for i in range(self.h):
                for j in range(self.l):
                    if self[j][i] is None:
                        cases_possibles.append((i, j))
            x, y = choice(cases_possibles)
        ennemi = perso.Squelette(self, (x, y), niveau)

    def spawn_crane(self, niveau, pos=()):
        if pos != ():
            x, y = pos[0], pos[1]
        else:
            cases_possibles = []
            for i in range(self.h):
                for j in range(self.l):
                    if self[j][i] is None:
                        cases_possibles.append((i, j))
            x, y = choice(cases_possibles)
        ennemi = perso.Crane(self, (x, y), niveau)

    def spawn_armure(self, niveau, pos=()):
        if pos != ():
            x, y = pos[0], pos[1]
        else:
            cases_possibles = []
            for i in range(self.h):
                for j in range(self.l):
                    if self[j][i] is None:
                        cases_possibles.append((i, j))
            x, y = choice(cases_possibles)
        ennemi = perso.Armure(self, (x, y), niveau)

    def spawn_invocateur(self, niveau, pos=()):
        if pos != ():
            x, y = pos[0], pos[1]
        else:
            cases_possibles = []
            for i in range(self.h):
                for j in range(self.l):
                    if self[j][i] is None:
                        cases_possibles.append((i, j))
            x, y = choice(cases_possibles)
        ennemi = perso.Invocateur(self, (x, y), niveau)

    @staticmethod
    def create_save():
        # Création du fichier si inexistant, ouverture sinon
        connexion = sqlite3.connect('\\Save\\Base_de_données.db')
        # Création des tables
        cursor = connexion.cursor()  # Pour manipuler les BDD
        cursor.execute("""
               DROP TABLE Joueurs CASCADE CONSTRAINTS;
               DROP TABLE Partie CASCADE CONSTRAINTS;    
            
               CREATE TABLE IF NOT EXISTS Joueurs(
                   nom VARCHAR(12) NOT NULL UNIQUE,
                   id_partie INT(4) NOT NULL UNIQUE,
                   classe VARCHAR(7) NOT NULL CONSTRAINT classe IN ('Epeiste', 'Garde', 'Sorcier', 'Garde'),
                   niveau INT(2) NOT NULL CONSTRAINT niveau <= 20,
                   pos_x INT(2) NOT NULL,
                   pos_y INT(2) NOT NULL,
                   potion INT(1) CONSTRAINT potion <= 5,
                   argent INT(4) CONSTRAINT argent <= 9999,
                   CODEX INT(1) CONSTRAINT CODEX IN (0, 1),
                   CONSTRAINT PK_Joueurs PRIMARY KEY (nom)
               )

               CREATE TABLE IF NOT EXISTS Partie(
                   id_partie INT(4) NOT NULL UNIQUE,
                   temps_jeu HOUR() NOT NULL,
                   nb_mort INT(2) NOT NULL CONSTRAINT nb_mort <= 99,
                   nb_kill INT() NOT NULL,
                   nb_squelette INT() NOT NULL,
                   nb_crane INT() NOT NULL,
                   nb_armure INT() NOT NULL,
                   nb_invocateur INT() NOT NULL,
                   vivant INT(1) NOT NULL CONSTRAINT vivant IN (0, 1),
                   CONSTRAINT PK_partie PRIMARY KEY (id_partie)
               )
               
               ALTER TABLE Joueurs ADD (
                    CONSTRAINT FK_Joueurs_Partie
                        FOREIGN KEY (id_partie)
                            REFERENCES Partie (id_partie)),
                
               """)
        # Fermeture de la connexion
        connexion.close()

    @staticmethod
    def write_save(player):
        """Permet de sauvegarder, et de créer la sauvegarde si c'est la première partie."""
        try:
            open('\\Save\\Base_de_données.db')
        except FileNotFoundError:
            Partie.create_save()
        else:
            # Récupération des valeurs nécessaire pour la suite
            kill_squelette = perso.Squelette.total_compteur - perso.Squelette.compteur
            kill_crane = perso.Crane.total_compteur - perso.Crane.compteur
            kill_armure = perso.Armure.total_compteur - perso.Armure.compteur
            kill_invocateur = perso.Invocateur.total_compteur - perso.Invocateur.compteur
            kill = kill_squelette + kill_crane + kill_armure + kill_invocateur

            # Ouverture du fichier
            connexion = sqlite3.connect('Base_de_données.db')

            # Test pour savoir si le joueur a déjà une sauvegarde dans la table
            cursor = connexion.cursor()
            cursor.execute("""SELECT nom FROM Joueurs WHERE nom=player.nom""")
            value = cursor.fetchone()

            if value[0] is None:  # Pas de sauvegarde existante
                # On créer un id_partie aléatoire n'existant pas déjà
                cursor = connexion.cursor()
                cursor.execute("""SELECT id_partie FROM Partie""")
                id_values = cursor.fetchone()
                id_prt = 1
                while id_prt in id_values:
                    id_prt = randrange(1, 9999)
                # On crée la sauvegarde de la partie et du joueur
                cursor.execute("""
                INSERT INTO Joueurs(nom, id_partie, classe, niveau, pos_x, pos_y) VALUES(player.nom, id_prt, 
                                                player.classe, player.niveau, player.position[0], player.position[1]),
                
                INSERT INTO Partie(id_partie, temps_jeu, nb_mort, nb_kill, nb_squelette, nb_crane, nb_armure,
                nb_invocateur, vivant) VALUES(id_prt, perso.temps_jeu, perso.compteur_mort, kill, kill_squelette,
                kill_crane, kill_armure, kill_invocateur, player.vivant),
                """)

            else:  # Sauvegarde existante
                cursor = connexion.cursor()
                cursor.execute("""SELECT id_partie FROM Joueurs WHERE nom=player.nom""")
                id_prt = cursor.fetchone()
                # Suppression anciennes données
                cursor.execute("""
                DELETE FROM Joueurs WHERE nom=player.nom
                DELETE FROM Partie WHERE id_partie=id_prt
                """)
                # On remplace la sauvegarde
                cursor.execute("""
                INSERT INTO Joueurs(nom, id_partie, classe, niveau, pos_x, pos_y) VALUES(player.nom, id_prt, 
                player.classe, player.niveau, player.position[0], player.position[1]),

                INSERT INTO Partie(id_partie, temps_jeu, nb_mort, nb_kill, nb_squelette, nb_crane, nb_armure,
                nb_invocateur, vivant) VALUES(id_prt, perso.temps_jeu, perso.compteur_mort, kill, kill_squelette,
                kill_crane, kill_armure, kill_invocateur, player.vivant),
                """)

            # Fermeture de la connexion
            connexion.close()

    def open_save(self, nom):
        try:
            open('\\Save\\Base_de_données.db')
        except FileNotFoundError:
            return None  # Dans le cadre où la sauvegarde n'existe pas encore
        else:
            connexion = sqlite3.connect('Base_de_données.db')
            cursor = connexion.cursor()
            cursor.execute("""SELECT classe, niveau, pos_x, pos_y FROM Joueurs WHERE nom=player.nom""")
            cls, niv, posx, posy = cursor.fetchone()
            connexion.close()
            self.new_player(nom, cls, niv, (posx, posy))

    def suppr_ennemi(self):
        while len(self.disparition) > 0:
            mechant = self.ennemis.pop()
            del self.ennemis[mechant.nom]
            del mechant

    def action_mechant(self):
        """Cette fonction va tourner sur un thread avec une clock spécifique qui ralentira la cadence
        (comme dans bca en fait)"""
        i = 0
        while True:
            t0_loop = time.time()
            if self.mutex.locked():
                if perso.Ennemi.compteur < 5:
                    lv = list(self.joueurs.values())[0].niveau  # ça commence à être moche
                    lvl = lv + randrange(-2, 3)
                    self.spawn_ennemi(lvl)
                for mechant in self.ennemis.values():  # Y'a une erreur ici faut gérer la suppression des méchants d'une autre façon
                    self.mutex.acquire()
                    if mechant.portee():
                        mechant.attaquer()
                    else:
                        mechant.deplacement()
                    mechant.agro()
                    self.mutex.release()

                self.mutex.acquire()
                self.suppr_ennemi()
                self.mutex.release()

                t_loop = time.time() - t0_loop
                if t_loop < 1:  # Les 5 ennemis vont agir à 1 Hz
                    time.sleep(1 - t_loop)
                else:
                    print('Too many computation in this loop')  # Meilleur ref
            else:
                t_loop = time.time() - t0_loop
                if t_loop < 1/24:  # On réessaye à une fréquence de 24 Hz
                    time.sleep(1 - t_loop)
                else:
                    print('Too many computation in this loop')  # Meilleur ref

            i += 1
            if i == 10:
                break

    def action_joueur(self):
        """Là je sais pas encore quoi faire, ça dépend grv de PyQt"""
        pass

    def __str__(self):
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
    a = Partie(20, 10)
    print(a)
