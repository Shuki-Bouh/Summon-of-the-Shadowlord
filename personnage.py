from abc import abstractmethod, ABCMeta
from random import random

import numpy as np


## ESPACES COMMENTAIRES
# Il faudrait mettre en place la representation des personnages et ennemis, pour pas nous confondre en les manipulant
# plus tard, ie, faire une methode pour ou bien utliser __repr__
# Toutes les entités devraient avoir la même modification de de "__position" donc je mets le get/set dans Entite directement





# --------------------------------------------------------------------------
# Classe mère abstraite Entite, où Personnages et Ennemis héritent de Entite

class Entite(metaclass=ABCMeta):
    """Tous les personnages qui existent dans le jeu"""

    direction = {'up': 'x, y - 1', # C'est peut-être un peu tordu, mais c'est plus rapide à coder...
                 'down': 'x, y + 1',
                 'left': 'x - 1, y',
                 'right': 'x + 1 , y'}

    id_ennemi = {'Squelette': 0,
                 'Crane': 1,
                 'Armure': 2}

    proba_attaque = {'Epeiste': [0.2, 0.3, 0.6],
                     'Garde': [0.2, 0.4, 0.5],
                     'Sorcier': [0.1, 0.2, 0.9],
                     'Druide': [0.2, 0.2, 0.4]}

    def __init__(self, game, path: str, position: tuple, cooldown: int, niveau = 1): # En réalité, on peut ne pas mettre tout ça en argument, mais juster générer les stats avec niveau
        self.path = path # Permet de lire le fichier dans lequel sont contenues les statistiques du perso pour chaque niveau
        self.__position = position # N'est pas caché car toutes les vérifications de création se trouvent dans Partie
        self.cooldown = cooldown # Est là pour ralentir l'utilisation des attaques
        self.__niveau = niveau
        self.niveau = niveau  # Dans niveau.setter, on va créer vie, attaque, défense et mana
        self.game = game
        self.position = position
        self.nom = 'entite'
        game.joueur[self.nom] = self

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
            lvl = lvl[self.niveau].split() # si je me trompe pas, j'ai récup la ligne correspondant au niveau du gars et j'en ai fait une liste
            for k in range(len(lvl)):
                lvl[k] = int(lvl[k])
            self.__viemax, self.attaque, self.defense, self.mana = lvl[:]
            self.__vie = self.__viemax

    @staticmethod
    def attJ_E(joueur, ennemi):
        """proba = cible.defense/(2*attaquant.attaque)
        si on veut fonctionner avec des probas évolutives, mais le sorcier devient OP avec la meilleure attaque"""
        id = Entite.id_ennemi[ennemi]
        prob = Entite.proba_attaque[joueur][id]
        if prob < random():
            ennemi.vie -= joueur.attaque

    @staticmethod
    def attE_J(ennemi, joueur):
        id = Entite.id_ennemi[ennemi]
        prob = Entite.proba_attaque[joueur][id]
        if (1-prob) < random():
            joueur.vie -= ennemi.attaque

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
        assert self.vie == 0  #Vérifie la mort du personnage
        pass



class Epeiste(Personnage):
    def __init__(self, game, position: tuple, nom: str, inventaire = {}, niveau = 1):
        # Pour position, à voir comment on génère ça, ptet pas en arg
        cooldown = 0
        super().__init__(game, "Epeiste_lvl.txt", position, cooldown, nom, inventaire, niveau)

    def attaquer(self):
        """Rappel : attaque d'épéiste est un simple coup dans la direction regardée"""
        x, y = self.position
        x_att, y_att = eval(Entite.direction[self.orientation])
        entity = self.game[x_att][y_att]
        if entity in self.game.ennemis.values():
            self.attJ_E(self, entity)

    def attaque_speciale(self):
        """
        Rappel : attaque spéciale d'épéiste est un balayage avec dégâts sur les 3 cases faces à sa vision
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
                self.attJ_E(self, entity)


class Garde(Personnage):
    def __init__(self, game, position: tuple, cooldown: int, nom: str, inventaire={}, niveau=1):
        super().__init__(game, "Garde_lvl.txt", position, cooldown, nom, inventaire, niveau)

    def attaquer(self):
        """Rappel : attaque de garde est un simple coup dans la direction regardée"""
        x, y = self.position
        x_att, y_att = eval(Entite.direction[self.orientation])
        entity = self.game[x_att][y_att]
        if entity in self.game.ennemis.values():
            self.attJ_E(self, entity)

    def attaque_speciale(self):
        """
        Rappel : attaque spéciale de garde est une attaque sur les deux cases dans la direction regardée
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
                self.attJ_E(self, entity)


class Sorcier(Personnage):
    def __init__(self, game, position: tuple, cooldown: int, nom: str, inventaire={}, niveau=1):
        self.path = "Sorcier_lvl.txt"
        super().__init__(game, "Sorcier_lvl.txt", position, cooldown, nom, inventaire, niveau)

    def attaquer(self):
        """Rappel : attaque de sorcier est un simple coup dans la direction regardée"""
        x, y = self.position
        x_att, y_att = eval(Entite.direction[self.orientation])
        entity = self.game[x_att][y_att]
        if entity in self.game.ennemis.values():
            self.attJ_E(self, entity)

    def attaque_speciale(self, direction=""):  # Pas besoin de direction dans celle-ci
        """
        Rappel : attaque spéciale de sorcier agit sur tous les ennemis dont la distance est au maximum 2 cases
        Cooldown : LONG
        """
        # C'est long à écrire, mais au moins c'est fait et on ne perd pas le temp sde calcul des boucles, et on est
        # sûr que le résultat est le bon.
        x_att, y_att = self.position
        liste_entite = []
        liste_entite.append(self.game[x_att][y_att + 1])
        liste_entite.append(self.game[x_att][y_att - 1])
        liste_entite.append(self.game[x_att + 1][y_att])
        liste_entite.append(self.game[x_att - 1][y_att])
        liste_entite.append(self.game[x_att][y_att + 2])
        liste_entite.append(self.game[x_att][y_att - 2])
        liste_entite.append(self.game[x_att + 2][y_att])
        liste_entite.append(self.game[x_att - 2][y_att])
        liste_entite.append(self.game[x_att + 1][y_att - 1])
        liste_entite.append(self.game[x_att + 1][y_att + 1])
        liste_entite.append(self.game[x_att - 1][y_att - 1])
        liste_entite.append(self.game[x_att - 1][y_att + 1])
        for entity in liste_entite:
            if entity in self.game.ennemis.values():
                self.attJ_E(self, entity)

class Druide(Personnage):
    def __init__(self, game, position: tuple, cooldown: int, nom: str, inventaire={}, niveau=1):
        super().__init__(game, "Druide_lvl.txt", position, cooldown, nom, inventaire, niveau)

    def attaquer(self):
        """Rappel : attaque de druide est un simple coup dans la direction regardée"""
        x, y = self.position
        x_att, y_att = eval(Entite.direction[self.orientation])
        entity = self.game[x_att][y_att]
        if entity in self.game.ennemis.values():
            self.attJ_E(self, entity)

    def attaque_speciale(self, direction=""):  # Pas besoin de direction dans celle-ci
        """
        Rappel : attaque spéciale de druide agit sur tous les ennemis dont la distance est au maximum d'une case
        Cooldown : MOYEN
        """
        x_att, y_att = self.position
        liste_entite = []
        liste_entite.append(self.game[x_att][y_att + 1])
        liste_entite.append(self.game[x_att][y_att - 1])
        liste_entite.append(self.game[x_att + 1][y_att])
        liste_entite.append(self.game[x_att - 1][y_att])
        for entity in liste_entite:
            if entity in self.game.ennemis.values():
                self.attJ_E(self, entity)


# ----------------------------------
# Développement des classes d'Ennemi

class Ennemi(Entite):
    compteur = 0
    liste_ennemis = {}
    
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
        pass

class Squelette(Ennemi):
    compteur = 0
    total_compteur = 0

    def __init__(self, game, position: tuple, niveau):
        super().__init__(game, "Squelette_lvl.txt", position, cooldown=5, niveau=niveau)
        Squelette.compteur += 1
        Squelette.total_compteur += 1
        self.nom = "Squelette " + str(Squelette.total_compteur)
        self.game.ennemis[self.nom] = self

    def attaquer(self, direction=""):
        for x,y in Entite.direction.values():
            entity = self.game[x][y]
            if entity in self.game.joueurs.values():
                self.attE_J(self, entity)

    def attaque_speciale(self, direction=""):
        for x, y in Entite.direction.values():
            entity = self.game[x][y]
            if entity in self.game.joueurs.values():
                entity -= 2*self.attaque  #Double coup

    def deplacement(self, direction=""):
        """Vision à definir de maniere efficace"""
        x = 1 if random() > 0.5 else -1
        y = 1 if random() > 0.5 else -1
        x_pos, y_pos = self.position
        self.position = (x_pos + x, y_pos + y)

    def mort(self):
        Squelette.compteur -= 1
        Ennemi.compteur -= 1
        del self.game.ennemis[self.nom]
        x, y = self.position
        self.game[y][x] = None

    def agro(self):
        for joueur in self.game.values():
            if np.linalg.norm(np.array(self.position), np.array(joueur.position)) < 4:
                self.cible = joueur



if __name__ == '__main__':
    pass