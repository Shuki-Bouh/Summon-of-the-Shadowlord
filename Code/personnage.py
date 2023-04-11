from abc import abstractmethod, ABCMeta
import random
import numpy as np
from PyQt5 import QtCore, QtGui

class Entite(metaclass=ABCMeta):
    """Classe mère héritant de metaclass. L'ensemble des personnages et ennemis du jeu en hérite."""

    # Dictionnaire utilisé pour faciliter l'acquisition des coordonnées des cases adjacentes aux entités
    direction = {'up': 'x, y - 1',
                 'down': 'x, y + 1',
                 'left': 'x - 1, y',
                 'right': 'x + 1 , y'}

    def __init__(self, game, path: str, position: tuple, cooldown: int, niveau=1):
        """Game est du type Partie du fichier partie.py"""
        self.path = path  # Path vers le fichier devant être ouvert, contenant les informations prédéfinis des entités.
        # On y retrouve les statistiques des personnages et ennemis pour chaque niveau.
        self.cooldown = cooldown  # Permet de cadencer la vitesse d'attaque des entités.
        self.__niveau = niveau
        self.niveau = niveau  # Appel la méthode "niveau.setter", dans laquelle vont être lu les informations de vie,
        # attaque, défense et mana du personnage, pour lui être attribués.
        self.game = game  # Permet de considérer la partie actuelle.
        self.__position = position
        self.nom = 'entite'  # Nom par défaut, modifié par la suite.
        self.position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, newpos: tuple):
        """Accepte un déplacement ssi la prochaine case est vide et sur la map.
        Nb : Les bords de la map sont False actuellement"""
        x1, y1 = self.position
        x2, y2 = newpos
        if self.game[x2][y2] is None:  # La nouvelle case est vide
            self.__position = x2, y2  # On change la position
            self.game[x1][y1] = None  # On actualise dans game
            self.game[x2][y2] = self

    @property
    def niveau(self):
        return self.__niveau

    @niveau.setter
    def niveau(self, niveau: int):
        """Permet d'attribuer à un personnage ses différentes caractéristiques, en fonction de son niveau en lisant
        les données dans un fichier txt.
        Dans chaque txt est contenu les vies max du perso, son attaque, sa défense et la magie qu'il dispose"""
        niveau = max(1, niveau)  # Supprime la possibilité d'avoir un niveau inférieur à 1
        if niveau <= 20:  # N'évolue plus après le lv 20
            self.__niveau = niveau
            with open(self.path, 'r') as lvl:
                lvl = lvl.readlines()
                lvl = lvl[self.niveau].split()  # On récupère la ligne correspondant aux stats du niveau dans le txt
                for k in range(len(lvl)):
                    lvl[k] = int(lvl[k])
                self.__viemax, self.attaque, self.defense, self.__manamax = lvl[:]  # On génère les stats du joueur
                self.__vie = self.__viemax  # à chaque lvlup, il récupère toutes ses vies
                self.__mana = self.__manamax

    @staticmethod
    @abstractmethod
    def coup(attaquant, cible):
        """Attaque d'attaquant sur cible."""
        pass

    @staticmethod
    def norm(vect1: tuple, vect2: tuple):
        """Renvoie la norme entre deux vecteurs."""
        x1, y1 = vect1
        x2, y2 = vect2
        return np.linalg.norm(np.array([x1 - x2, y1 - y2]))

    @property
    def viemax(self):
        return self.__viemax

    @property
    def vie(self):
        return self.__vie

    @vie.setter
    def vie(self, x):
        """Permet de réguler la vie des entités, afin qu'elles ne dépassent pas self.viemax
        ni qu'elles descendent sous une vie égale à 0."""
        if x <= 0:
            self.__vie = 0
            self.mort()
        elif x >= self.viemax:
            self.__vie = self.viemax
        else:
            self.__vie = x

    @property
    def manamax(self):
        return self.__manamax

    @property
    def mana(self):
        return self.__mana

    @mana.setter
    def mana(self, x):
        """Permet de réguler le mana des entités, afin qu'elles ne dépassent pas self.manamax
        ni qu'elles descendent sous un mana égal à 0."""
        if x <= 0:
            self.__mana = 0
        elif x >= self.manamax:
            self.__mana = self.manamax
        else:
            self.__mana = x

    @abstractmethod
    def attaquer(self):
        """Schéma d'attaque classique des entités."""
        pass

    @abstractmethod
    def attaque_speciale(self):
        """Schéma d'attaque spéciale des entités."""
        pass

    @abstractmethod
    def mort(self):
        """Permet de faire mourir une entité, et donc de libérer son espace mémoire associé."""
        pass

    @abstractmethod
    def dessinImage(self, qp, x_win, y_win):
        pass


    def __str__(self):
        """Permet de représenter une entité par son nom."""
        return self.nom


# ------------------------------------
# Développement des classes Personnage

class Personnage(Entite):
    """Définition ici de l'ensemble des personnages pouvant être joués par l'utilisateur.
    Au début d'une partie, le joueur choisit un personnage avec lequel il entreprendra son aventure."""

    def __init__(self, game, path: str, position: tuple, cooldown: int, nom: str, inventaire: dict, niveau: int):
        super().__init__(game, path, position, cooldown, niveau)
        self.inventory = inventaire
        self.nom = nom
        self.orientation = 'up'  # L'orientation sert à l'affichage du personnage et pour la direction de ses attaques
        self.xp = 0
        self.vivant = True
        game.joueurs[self.nom] = self  # On ajoute dans la partie actuelle le joueur dans la case adéquate

    @abstractmethod
    def attaquer(self):
        pass

    @abstractmethod
    def attaque_speciale(self):
        pass

    def deplacement(self, direction: str):
        """Déplacement du joueur, avec la direction donnée par PyQt"""
        x, y = self.position
        x, y = eval(Entite.direction[direction])  # Renvoie un tuple de type (x + 1, y) (utilisation d'un switch)
        self.position = (x, y)
        self.orientation = direction

    def interagir(self):
        """Permet d'utiliser objet"""
        pass

    def levelup(self):
        """Permet de faire évoluer le niveau du personnage lorsqu'il a tué suffisamment d'ennemis"""
        if self.xp > self.niveau * 10 and self.niveau < 20:  # C'est un peu arbitraire pour le moment
            self.xp -= self.niveau * 10
            self.niveau += 1

    @staticmethod
    def coup(attaquant, cible):
        """La fonction qui permet à un joueur de retirer de la vie à un ennemi"""
        if (attaquant.defense / cible.defense) < 1:
            vie = cible.vie - attaquant.attaque * attaquant.defense // cible.defense
        else:  # Formula damage
            vie = cible.vie - attaquant.attaque
        if vie < 1:  # Si l'ennemi n'a plus de vie
            attaquant.xp += cible.xp  # Le joueur gagne de l'xp
            attaquant.levelup()  # Puis on vérifie s'il a suffisamment d'xp pour lvlup
        cible.vie = vie

    def mort(self):
        """La mort bloque en réalité l'utilisation des touches actions"""
        self.vivant = False
        pass


class Epeiste(Personnage):

    def __init__(self, game, position: tuple, nom: str, inventaire={}, niveau=1):
        self.cooldown = 0
        self.classe = 'Epeiste'
        self.image = QtGui.QImage("./Epeiste/Idle/idle.jpg")
        super().__init__(game, "Epeiste_lvl.txt", position, self.cooldown, nom, inventaire, niveau)

    def attaquer(self):
        """Nota : attaque d'épéiste est un simple coup dans la direction regardée"""
        x, y = self.position
        x_att, y_att = eval(Entite.direction[self.orientation])  # On se sert de Entite.direction comme d'un switch
        entity = self.game[x_att][y_att]
        if entity in self.game.ennemis.values():  # Permet de vérifier si on est face à un ennemi ou un joueur
            self.coup(self, entity)

    def attaque_speciale(self):
        """
        Nota : attaque spéciale d'épéiste est un balayage avec dégâts sur les 3 cases faces à sa vision.
        Les dégâts infligés sont certains et doublés.
        Cooldown : MOYEN (10 sec)
            """
        if self.mana:
            x, y = self.position
            x_att, y_att = eval(Entite.direction[self.orientation])
            list_dir = [-1, 0, 1]
            liste_entite = []
            if self.orientation == "up" or self.orientation == "down":
                for k in list_dir:
                    liste_entite.append(self.game[x_att + k][y_att])
            else:
                for k in list_dir:
                    liste_entite.append(self.game[x_att][y_att + k])
            for entity in liste_entite:
                if entity in self.game.ennemis.values():
                    self.attaque *= 2
                    self.coup(self, entity) # Y'a l'air d'avoir problème, à checker hein
                    self.attaque //= 2
                    self.mana -= 1

    def dessinImage(self, qp, x_win, y_win):
        qp.drawImage(QtCore.QRect(x_win, y_win, 50, 50), self.image)


class Garde(Personnage):
    def __init__(self, game, position: tuple, nom: str, inventaire={}, niveau=1):
        self.cooldown = 0
        self.classe = 'Garde'
        self.image = QtGui.QImage("./Garge/Idle/idle.jpg")
        super().__init__(game, "Garde_lvl.txt", position, self.cooldown, nom, inventaire, niveau)

    def attaquer(self):
        """Nota : attaque de garde est un simple coup dans la direction regardée"""
        x, y = self.position
        x_att, y_att = eval(Entite.direction[self.orientation])
        entity = self.game[x_att][y_att]
        if entity in self.game.ennemis.values():
            self.coup(self, entity)

    def attaque_speciale(self):
        """
        Nota : attaque spéciale de garde est une attaque sur les deux cases dans la direction regardée.
        Cette attaque est certaine et expulse les ennemis une case en arrière.
        Cooldown : COURT (5 sec)
        """
        x, y = self.position
        x_att, y_att = eval(Entite.direction[self.orientation])
        liste_entite = [self.game[x_att][y_att]]
        x_2ecase, y_2ecase = x_att, y_att
        if self.orientation == "up":
            y_2ecase -= 1
        elif self.orientation == "down":
            y_2ecase += 1
        elif self.orientation == "left":
            x_2ecase -= 1
        else:
            x_2ecase += 1
        liste_entite.append(self.game[x_2ecase][y_2ecase])
        liste_entite.sort(reverse=True)  # Pour faire déplacer l'ennemi le plus loin d'abord, sinon, collisions.
        for entity in liste_entite:
            if entity in self.game.ennemis.values():
                entity.vie -= self.attaque
                x, y = entity.position
                x, y = eval(Entite.direction[self.orientation])
                entity.position = (x, y)

    def dessinImage(self, qp, x_win, y_win):
        qp.drawImage(QtCore.QRect(x_win, y_win, 50, 50), self.image)


class Sorcier(Personnage):
    def __init__(self, game, position: tuple, nom: str, inventaire={}, niveau=1):
        self.cooldown = 0
        self.classe = 'Sorcier'
        self.image = QtGui.QImage("./Sorcier/Idle/idle.jpg")
        super().__init__(game, "Sorcier_lvl.txt", position, self.cooldown, nom, inventaire, niveau)

    def attaquer(self):
        """Nota : attaque de sorcier est un simple coup dans la direction regardée"""
        x, y = self.position
        x_att, y_att = eval(Entite.direction[self.orientation])
        entity = self.game[x_att][y_att]
        if entity in self.game.ennemis.values():
            self.coup(self, entity)

    def attaque_speciale(self, direction=""):  # Pas besoin de direction dans celle-ci
        """
        Nota : attaque spéciale de sorcier agit sur tous les ennemis dont la distance est au maximum 2 cases
        Cooldown : LONG (20 sec)
        """
        # C'est long à écrire, mais au moins c'est fait et on ne perd pas le temp sde calcul des boucles, et on est
        # sûr que le résultat est le bon.
        x_att, y_att = self.position
        liste_entite = []
        for k in range(-2, 3):
            liste_entite.append(self.game[x_att + k][y_att])
            liste_entite.append(self.game[x_att][y_att + k])
        for entity in liste_entite:
            if entity in self.game.ennemis.values():
                self.coup(self, entity)

    def dessinImage(self, qp, x_win, y_win):
        qp.drawImage(QtCore.QRect(x_win, y_win, 50, 50), self.image)


class Archer(Personnage):
    def __init__(self, game, position: tuple, nom: str, inventaire={}, niveau=1):
        self.cooldown = 0
        self.classe = 'Archer'
        self.image = QtGui.QImage("./Archer/Idle/idle.jpg")
        super().__init__(game, "Archer_lvl.txt", position, self.cooldown, nom, inventaire, niveau)

    def attaquer(self):
        """Nota : attaque d'archer est un simple coup dans la direction regardée"""
        x, y = self.position
        x_att, y_att = eval(Entite.direction[self.orientation])
        entity = self.game[x_att][y_att]
        if entity in self.game.ennemis.values():
            self.coup(self, entity)

    def attaque_speciale(self, direction=""):  # Pas besoin de direction dans celle-ci
        """
        Nota : attaque spéciale d'archer agit sur tous les ennemis dont la distance est au maximum d'une case,
        et leur inflige un coup certain.
        Cooldown : MOYEN
        """
        x_att, y_att = self.position
        liste_entite = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                liste_entite.append(self.game[x_att + i][y_att + j])
        for entity in liste_entite:
            if entity in self.game.ennemis.values():
                entity.vie -= self.attaque

    def dessinImage(self, qp, x_win, y_win):
        qp.drawImage(QtCore.QRect(x_win, y_win, 50, 50), self.image)


# ----------------------------------
# Développement des classes d'Ennemi


class Ennemi(Entite):
    """Définition ici de l'ensemble des ennemis pouvant être rencontrés par l'utilisateur.
    Leur nombre est limité à 5 en simultané, de sorte que le jeu soit jouable."""

    compteur = 0  # Ce compteur permet d'éviter de générer trop d'ennemis sur la map en même temps

    def __init__(self, game, path: str, position: tuple, cooldown: int, niveau):
        super().__init__(game, path, position, cooldown, niveau)
        Ennemi.compteur += 1  # Il est incrémenté à chaque ennemi créé
        self.cible = None  # Chaque ennemi va essayer de poursuivre sa cible
        self.vision = 0  # Pour savoir jusqu'où il cherche une nouvelle cible

    @abstractmethod
    def attaquer(self):
        pass

    @abstractmethod
    def attaque_speciale(self):
        pass

    def deplacement(self):
        """Déplacement aléatoire d'une case"""
        if self.cible:  # S'il a une cible, il essaie de s'en rapprocher : d'abord en horizontal puis en latéral
            mechant = self.cible  # La cible est le joueur qui est rentré dans la zone de vision (cf agro)
            xc, yc = mechant.position
            xs, ys = self.position
            if xc < xs:
                direction = "left"
            elif xc > xs:
                direction = "right"
            elif yc < ys:
                direction = "up"
            else:
                direction = "down"
        else:
            direction = random.choice(tuple(Entite.direction.keys()))  # S'il n'a pas de cible, il se balade librement
        x, y = self.position
        x, y = eval(Entite.direction[direction])
        self.position = (x, y)

    @staticmethod
    def coup(attaquant, cible):
        if (attaquant.defense / cible.defense) < 1:
            cible.vie -= attaquant.attaque * attaquant.defense // cible.defense
        else:
            cible.vie -= attaquant.attaque

    def portee(self):
        """Portée d'un coup : si un joueur est suffisamment proche, l'ennemi attaque (cf action_mechant)"""
        x1, y1 = self.position
        try:  # Si l'ennemi n'a pas encore de cible, self.cible is None
            x2, y2 = self.cible.position
            if (x1 == x2 and abs(y1 - y2) == 1) or (abs(x1 - x2) == 1 and y1 == y2):
                return True
        except AttributeError:
            return False
        return False

    def mort(self):
        """Mort d'un méchant"""
        Ennemi.compteur -= 1
        x, y = self.position
        self.game [x][y] = None  # One le retire de la map immédiatement et on l'ajoute à la liste des ennemis à del
        self.game.disparition.append(self)
        pass

    def agro(self):
        """Vision : COURT (2 cases) / MOYEN (4 cases) / LONG (6 cases)"""
        dict_normes = {}  # Ce dictionnaire stock (joueur, norme)
        for joueur in self.game.joueurs.values():
            if self.norm(self.position, joueur.position) < self.vision:  # On vérifie que le joueur est dans le champ
                dict_normes[joueur] = self.norm(self.position, joueur.position)
        if len(dict_normes):  # On gère le cas où personne n'est dans la zone
            dict_normes = sorted(dict_normes.items(), key=lambda t: t[1])  # On trie par rapport à la norme
            self.cible = dict_normes[0][0]  # La cible est le min des normes → 1e élément de la liste triée


class Squelette(Ennemi):
    compteur = 0
    total_compteur = 0

    def __init__(self, game, position: tuple, niveau):
        super().__init__(game, "Squelette_lvl.txt", position, cooldown=5, niveau=niveau)
        Squelette.compteur += 1  # Nombre de squelettes présents
        Squelette.total_compteur += 1  # Nb de squelettes étant déjà apparu
        self.nom = "Squelette " + str(Squelette.total_compteur)  # Permet d'être sûr de ne pas avoir deux squelettes
        # identiques
        self.game.ennemis[self.nom] = self
        self.xp = (10 * self.niveau) // 3  # L'xp que gagne le joueur s'il le tue
        self.vision = 4
        self.image = QtGui.QImage("./Squelette/Idle/idle.jpg")

    def attaquer(self):
        """Nota : attaque de squelette est un simple coup porté si un joueur se situe à une case adjacente"""
        self.coup(self, self.cible)

    def attaque_speciale(self):
        """
        Nota : attaque spéciale de squelette est un coup de dégâts (x2), nécessairement réussi.
        Cooldown : COURT (5 sec)
        """
        self.cible.vie -= 2 * self.attaque

    def mort(self):
        Squelette.compteur -= 1
        Ennemi.mort(self)

    def dessinImage(self, qp, x_win, y_win):
        qp.drawImage(QtCore.QRect(x_win, y_win, 50, 50), self.image)


class Crane(Ennemi):
    compteur = 0
    total_compteur = 0

    def __init__(self, game, position: tuple, niveau):
        super().__init__(game, "Crane_lvl.txt", position, cooldown=5, niveau=niveau)
        Crane.compteur += 1
        Crane.total_compteur += 1
        self.nom = "Crane " + str(Crane.total_compteur)
        self.xp = (10 * self.niveau) // 3
        self.game.ennemis[self.nom] = self
        self.vision = 6
        self.image = QtGui.QImage("./Crane/Idle/idle.jpg")

    def attaquer(self):
        """Nota : attaque de crâne est un simple coup porté si un joueur se situe à une case adjacente"""
        self.coup(self, self.cible)

    def attaque_speciale(self):
        """
        Nota : Bump le personnage de 2 cases en arrière (dans la mesure du possible),
        et lui vole 1/3 de sa vie pour se régénérer
        Cooldown : MOYEN (10 sec)
        """
        vol_vie = self.cible.vie // 3
        self.cible.vie -= vol_vie
        self.vie += vol_vie
        x1, y1 = self.position
        x2, y2 = self.cible.position
        if x1 == x2:
            if y1 > y2:
                direction = 'up'
            else:
                direction = 'down'
        elif x1 < x2:
            direction = 'right'
        else:
            direction = 'left'
        self.cible.deplacement(direction)
        self.cible.deplacement(direction)

    def deplacement(self):
        """Double déplacement"""
        for k in range(2):
            Ennemi.deplacement(self)

    def mort(self):
        Crane.compteur -= 1
        Ennemi.mort(self)

    def dessinImage(self, qp, x_win, y_win):
        qp.drawImage(QtCore.QRect(x_win, y_win, 50, 50), self.image)


class Armure(Ennemi):
    compteur = 0
    total_compteur = 0

    def __init__(self, game, position: tuple, niveau):
        super().__init__(game, "Armure_lvl.txt", position, cooldown=5, niveau=niveau)
        Armure.compteur += 1
        Armure.total_compteur += 1
        self.nom = "Armure " + str(Armure.total_compteur)
        self.xp = 20 * self.niveau // 3
        self.game.ennemis[self.nom] = self
        self.vision = 2
        self.image = QtGui.QImage("./Armure/Idle/idle.jpg")

    def attaquer(self):
        """Nota : attaque d'armure est un simple coup porté si un joueur se situe à une case adjacente"""
        self.coup(self, self.cible)

    def attaque_speciale(self):
        """
        Nota : Réduit son attaque de moitié pour se redonner 1/3 de sa vie,
        attaque sa cible à coup sûr et la fait reculer d'une case
        Cooldown : LONG (15 sec)
        """
        self.attaque //= 2
        self.vie = (self.vie * 4) // 3
        self.cible.vie -= self.attaque
        x1, y1 = self.position
        x2, y2 = self.cible.position
        if x1 == x2:
            if y1 > y2:
                direction = 'up'
            else:
                direction = 'down'
        elif x1 < x2:
            direction = 'right'
        else:
            direction = 'left'
        self.cible.deplacement(direction)

    def mort(self):
        Armure.compteur -= 1
        Ennemi.mort(self)

    def dessinImage(self, qp, x_win, y_win):
        qp.drawImage(QtCore.QRect(x_win, y_win, 50, 50), self.image)


class Invocateur(Ennemi):
    compteur = 0
    total_compteur = 0

    def __init__(self, game, position: tuple, niveau):
        super().__init__(game, "Invocateur_lvl.txt", position, cooldown=5, niveau=niveau)
        Invocateur.compteur += 1
        Invocateur.total_compteur += 1
        self.nom = "Invocateur " + str(Invocateur.total_compteur)
        self.xp = (30 * self.niveau) // 3
        self.game.ennemis[self.nom] = self
        self.vision = 5
        self.image = QtGui.QImage("./Invocateur/Idle/idle.jpg")

    def attaquer(self):
        """Nota : attaque d'invocateur est un simple coup porté si un joueur se situe à une case adjacente"""
        self.coup(self, self.cible)

    def attaque_speciale(self):
        """
        Nota : Fais spawn deux crânes à ses côtés pour combattre si cela est possible,
        sinon, il régénère entièrement sa vie. De plus, il porte un coup sûr au joueur.
        Cooldown : LONG (20 sec)
        """
        self.cible.vie -= self.attaque
        if self.game.limite_spawn - Ennemi.compteur >= 2:
            x1, y1 = self.position
            x2, y2 = self.cible.position
            if x1 == x2:
                x3, y3 = x1, y1 - 1
                x4, y4 = x1, y1 + 1
            else:
                x3, y3 = x1 - 1, y1
                x4, y4 = x1 + 1, y1
            self.game.spawn_crane(self.niveau, (x3, y3))
            self.game.spawn_crane(self.niveau, (x4, y4))
        else:
            self.vie = self.viemax

    def mort(self):
        Invocateur.compteur -= 1
        Ennemi.mort(self)

    def dessinImage(self, qp, x_win, y_win):
        qp.drawImage(QtCore.QRect(x_win, y_win, 50, 50), self.image)


if __name__ == '__main__':
    pass
