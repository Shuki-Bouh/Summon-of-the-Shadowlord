from abc import abstractmethod, ABCMeta
import random
import numpy as np


# ESPACES COMMENTAIRES -----------------------------------------------------
# Il faudrait mettre en place la representation des personnages et ennemis, pour pas nous confondre en les manipulant
# plus tard, c'est-à-dire, faire une methode pour ou bien utiliser __repr__

# Toutes les entités devraient avoir la même modification de "__position"
# donc je mets le get/set dans "Entité" directement.

# --------------------------------------------------------------------------
# Classe mère abstraite Entité, où Personnages et Ennemis héritent d'Entité

class Entite(metaclass=ABCMeta):
    """Tous les personnages qui existent dans le jeu"""

    direction = {'up': 'x, y - 1',
                 'down': 'x, y + 1',
                 'left': 'x - 1, y',
                 'right': 'x + 1 , y'}

    def __init__(self, game, path: str, position: tuple, cooldown: int, niveau=1):
        # En réalité, on peut ne pas mettre tout ça en argument, mais juster générer les stats avec niveau
        self.path = path  # Permet de lire le fichier dans lequel
        # sont contenues les statistiques du perso pour chaque niveau
        self.__position = position  # N'est pas caché car toutes les vérifications de création se trouvent dans Partie
        self.cooldown = cooldown  # Est là pour ralentir l'utilisation des attaques
        self.__niveau = niveau
        self.niveau = niveau  # Dans niveau.setter, on va créer vie, attaque, défense et mana
        self.game = game
        self.position = position
        self.nom = 'entite'

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, newpos):
        x1, y1 = self.position
        x2, y2 = newpos
        if self.game[x2][y2] == None:
            self.__position = x2, y2
            self.game[x1][y1] = None
            self.game[x2][y2] = self

    @property
    def niveau(self):
        return self.__niveau # Pauvre fou, jamais de parenthèses !
    @niveau.setter
    def niveau(self, niveau):
        self.__niveau = niveau
        with open(self.path, 'r') as lvl:
            lvl = lvl.readlines()
            lvl = lvl[self.niveau].split() # On récupère la ligne correspondant aux stats du niveau
            for k in range(len(lvl)):
                lvl[k] = int(lvl[k])
            self.__viemax, self.attaque, self.defense, self.mana = lvl[:]
            self.__vie = self.__viemax

    @staticmethod
    def coup(attaquant, cible):
        if (attaquant.defense/cible.defense) < 1:
            cible.vie -= np.floor(attaquant.attaque*(attaquant.defense/cible.defense))
        else:
            cible.vie -= attaquant.attaque

    @property
    def viemax(self):
        return self.__viemax

    @property
    def vie(self):
        return self.__vie

    @vie.setter
    def vie(self, x):
        if x <= 0:
            self.mort()
        elif x >= self.viemax:
            self.__vie = self.viemax
        else:
            self.__vie = x

    @abstractmethod
    def attaquer(self):
        pass

    @abstractmethod
    def attaque_speciale(self):
        pass

    @abstractmethod
    def deplacement(self, direction):
        pass

    @abstractmethod
    def mort(self):
        pass

    def __str__(self):
        return self.nom

# ------------------------------------
# Développement des classes Personnage


class Personnage(Entite):
    def __init__(self, game, path: str, position: tuple, cooldown: int, nom: str, inventaire: dict, niveau: int):
        super().__init__(game, path, position, cooldown, niveau)
        self.inventory = inventaire  # Objet item
        self.nom = nom
        self.orientation = 'up'
        game.joueurs[self.nom] = self

    @abstractmethod
    def attaquer(self):
        pass

    @abstractmethod
    def attaque_speciale(self):
        pass

    def deplacement(self, direction):
        x, y = self.position
        x, y = eval(Entite.direction[direction])
        self.position = (x, y)
        self.orientation = direction

    def interagir(self):
        """Permet d'utiliser objet"""
        pass

    def levelup(self):
        self.niveau += 1

    def mort(self):
        pass


class Epeiste(Personnage):
    def __init__(self, game, position: tuple, nom: str, inventaire={}, niveau=1):
        # Pour position, à voir comment on génère ça, peut-être pas en argument...
        cooldown = 0
        super().__init__(game, "../Data/Epeiste_lvl.txt", position, cooldown, nom, inventaire, niveau)

    def attaquer(self):
        """Nota : attaque d'épéiste est un simple coup dans la direction regardée"""
        x, y = self.position
        x_att, y_att = eval(Entite.direction[self.orientation]) # On se sert de Entite.direction comme d'un switch
        entity = self.game[x_att][y_att]
        if entity in self.game.ennemis.values(): # Permet de vérifier si on est face à un ennemi ou un joueur
            self.coup(self, entity)

    def attaque_speciale(self):
        """
        Nota : attaque spéciale d'épéiste est un balayage avec dégâts sur les 3 cases faces à sa vision
        Cooldown COURT !
        """
        x, y = self.position
        x_att, y_att = eval(Entite.direction[self.orientation])
        list_dir = [-1, 0, 1]
        liste_entite = []
        if self.orientation == "up" or self.orientation == "down":
            for k in list_dir:
                liste_entite.append(self.game[x_att + k, y_att])
        else:
            for k in list_dir:
                liste_entite.append(self.game[x_att, y_att + k])
        for entity in liste_entite:
            if entity in self.game.ennemis.values():
                self.coup(self, entity) # On pourrait pas mettre un buff ? Genre c'est un peu triste que le spécial soit pas à peine plus puissant


class Garde(Personnage):
    def __init__(self, game, position: tuple, cooldown: int, nom: str, inventaire={}, niveau=1):
        super().__init__(game, "../Data/Garde_lvl.txt", position, cooldown, nom, inventaire, niveau)

    def attaquer(self):
        """Nota : attaque de garde est un simple coup dans la direction regardée"""
        x, y = self.position
        x_att, y_att = eval(Entite.direction[self.orientation])
        entity = self.game[x_att][y_att]
        if entity in self.game.ennemis.values():
            self.coup(self, entity)

    def attaque_speciale(self):
        """
        Nota : attaque spéciale de garde est une attaque sur les deux cases dans la direction regardée
        Cooldown COURT
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
        for entity in liste_entite:
            if entity in self.game.ennemis.values():
                self.coup(self, entity)


class Sorcier(Personnage):
    def __init__(self, game, position: tuple, cooldown: int, nom: str, inventaire={}, niveau=1):
        self.path = "../Data/Sorcier_lvl.txt"
        super().__init__(game, "../Data/Sorcier_lvl.txt", position, cooldown, nom, inventaire, niveau)

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
        Cooldown : LONG
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

class Druide(Personnage):
    def __init__(self, game, position: tuple, cooldown: int, nom: str, inventaire={}, niveau=1):
        super().__init__(game, "../Data/Druide_lvl.txt", position, cooldown, nom, inventaire, niveau)

    def attaquer(self):
        """Nota : attaque de druide est un simple coup dans la direction regardée"""
        x, y = self.position
        x_att, y_att = eval(Entite.direction[self.orientation])
        entity = self.game[x_att][y_att]
        if entity in self.game.ennemis.values():
            self.coup(self, entity)

    def attaque_speciale(self, direction=""):  # Pas besoin de direction dans celle-ci
        """
        Nota : attaque spéciale de druide agit sur tous les ennemis dont la distance est au maximum d'une case
        Cooldown : MOYEN
        """
        x_att, y_att = self.position
        liste_entite = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                liste_entite.append(self.game[x_att + i][y_att + j])
        for entity in liste_entite:
            if entity in self.game.ennemis.values():
                self.coup(self, entity)


# ----------------------------------
# Développement des classes d'Ennemi

class Ennemi(Entite):
    compteur = 0
    
    def __init__(self, game, path: str, position: tuple, cooldown: int, niveau):
        super().__init__(game, path, position, cooldown, niveau)
        Ennemi.compteur += 1
        self.cible = False

    @abstractmethod
    def attaquer(self, direction=""):
        pass

    @abstractmethod
    def attaque_speciale(self, direction=""):
        pass

    @abstractmethod
    def deplacement(self, direction=""):
        pass

    def mort(self):
        """Bon il faut faire quoi là ?"""
        # Si multi : multi va probablement devenir une variable de classe Partie
        # Donc s'il est solo, c'est un game over, comment on fait ?
        # Changement d'image, suppression des ennemis
        # Possibilité de recommencer (par un load où on va modifier les vies)
        # Si multi : il meurt, possibilité de respawn ?
        # Une fois que tous les joueurs sont morts, même game over
        pass


class Squelette(Ennemi):
    compteur = 0
    total_compteur = 0

    def __init__(self, game, position: tuple, niveau):
        super().__init__(game, "../Data/Squelette_lvl.txt", position, cooldown=5, niveau=niveau)
        Squelette.compteur += 1
        Squelette.total_compteur += 1
        Ennemi.compteur += 1
        self.nom = "Squelette " + str(Squelette.total_compteur)
        self.game.ennemis[self.nom] = self

    def attaquer(self, direction=""):
        """Nota : attaque de squelette est un simple coup porté si un joueur se situe à une case adjacente"""
        pass

    def attaque_speciale(self, direction=""):
        """
        Nota : attaque spéciale de squelette est un coup de dégâts (x2), nécessairement réussi.
        Cooldown : COURT
        """
        """Nota : attaque de squelette est un simple coup porté si un joueur se situe à une case adjacente"""
        liste_direction = list(Entite.direction.values())
        liste_pos = []
        for k in range(4):
            liste_pos.append(liste_direction[k])
        for dir in liste_pos:
            x, y = self.position
            x, y = eval(dir)
            entity = self.game[x][y]
            if entity in self.game.joueurs.values():
                entity.vie -= 2*self.attaque
                break

    def deplacement(self):
        # A CODER : Déplacement vers ennemi le plus proche quand agro()
        """Déplacement aléatoire d'une case"""
        if self.cible:
            mechant = self.cible
            xc, yc = mechant.position
            xs, ys = self.position
            if abs(xc - xs) == 1 or abs(yc - ys) == 1:
                mechant.attaquer()
            elif xc < xs:
                direction = "left"
            elif xc > xs:
                direction = "right"
            elif yc < ys:
                direction = "up"
            else:
                direction = "down"
        else:
            direction = random.choice(tuple(Entite.direction.keys()))
        x, y = self.position
        x, y = eval(Entite.direction[direction])
        self.position = (x, y)

    def mort(self):
        Squelette.compteur -= 1
        Ennemi.compteur -= 1
        del self.game.ennemis[self.nom]
        x, y = self.position
        self.game[x][y] = None

    def agro(self):
        """Vision MOYENNE (4 cases)"""
        for joueur in self.game.values():
            if np.linalg.norm([self.position, joueur.position]) < 4:
                self.cible = joueur


class Crane(Ennemi):
    compteur = 0
    total_compteur = 0

    def __init__(self, game, position: tuple, niveau):
        super().__init__(game, "../Data/Crane_lvl.txt", position, cooldown=5, niveau=niveau)
        Crane.compteur += 1
        Crane.total_compteur += 1
        Ennemi.compteur += 1
        self.nom = "Crane " + str(Squelette.total_compteur)
        self.game.ennemis[self.nom] = self

    def attaquer(self, direction=""):
        """Nota : attaque de crâne est un simple coup porté si un joueur se situe à une case adjacente"""
        for x, y in Entite.direction.items():
            entity = self.game[x][y]
            if entity in self.game.joueurs.values():
                self.coup(self, entity)

    def attaque_speciale(self, direction=""):
        """
        Nota : Bump le personnage de 2 cases en arrière (dans la mesure du possible),
        et lui vole 1/3 de sa vie pour se régénérer
        Cooldown : LONG
        """
        for x, y in Entite.direction.values():
            entity = self.game[x][y]
            if entity in self.game.joueurs.values():
                vol_vie = np.floor(entity.vie*(1/3))
                entity.vie -= vol_vie
                self.vie += vol_vie
                direction = entity.direction
                if direction == 'up':
                    opp_dir = 'down'
                elif direction == 'down':
                    opp_dir = 'up'
                elif direction == 'left':
                    opp_dir = 'right'
                else:
                    opp_dir = 'left'
                entity.deplacement(opp_dir)
                entity.deplacement(opp_dir)

    def deplacement(self, direction=""):
        # A CODER : Déplacement vers ennemi le plus proche quand agro()
        """Double déplacement"""
        for k in range(2):
            direction = random.choice(tuple(Entite.direction.keys()))
            x, y = self.position
            x, y = eval(Entite.direction[direction])
            self.position = (x, y)

    def mort(self):
        Crane.compteur -= 1
        Ennemi.compteur -= 1
        del self.game.ennemis[self.nom]
        x, y = self.position
        self.game[x][y] = None

    def agro(self):
        """Vision LONGUE (6 cases)"""
        for joueur in self.game.values():
            if np.linalg.norm(np.array([self.position, joueur.position])) < 6:
                self.cible = joueur


if __name__ == '__main__':
    pass