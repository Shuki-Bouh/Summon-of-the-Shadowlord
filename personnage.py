from abc import abstractmethod, ABCMeta
from partie import Partie

## ESPACES COMMENTAIRES
# Il faudrait mettre en place la representation des personnages et ennemis, pour pas nous confondre en les manipulant
# plus tard, ie, faire une methode pour ou bien utliser __repr__
# Toutes les entités devraient avoir la même modification de de "__position" donc je mets le get/set dans Entite directement





# --------------------------------------------------------------------------
# Classe mère abstraite Entite, où Personnages et Ennemis héritent de Entite

class Entite(metaclass=ABCMeta):
    """Tous les personnages qui existent dans le jeu"""

    direction = {'up': 'y-1, x',
                 'down': 'y+1, x',
                 'left': 'y, x-1',
                 'right': 'y, x+1'}
    def __init__(self, position: tuple, cooldown: int, niveau = 1): # En réalité, on peut ne pas mettre tout ça en argument, mais juster générer les stats avec niveau
        self.vie = 0
        self.attaque = 0
        self.defense = 0
        self.mana = 0
        self.path = ''
        self.__position = position
        self.cooldown = cooldown
        self.__niveau = niveau
        self.niveau = niveau

    @property
    def niveau(self):
        return (self.__niveau)

    @niveau.setter
    def niveau(self, niveau):
        # On peut penser à faire des paliers de nuveau, avec des bonus supplémentaires (ex: de 5 en 5 jusqu'au niveau 30)
        with open(self.path, 'r') as lvl:
            lvl = lvl.readline()
            lvl = lvl[self.niveau] # si je me trompe pas, j'ai récup la ligne correspondant au niveau du gars et j'en ai fait une liste
            lvl = lvl.split()
            self.vie, self.attaque, self.defense, self.mana = lvl[:]
        self.__niveau = niveau

    @property
    def position(self):
        return self.__position
    # ça sert ptet pas en fait
    @position.setter
    def position(self, nextPosition):
        pass

    @abstractmethod
    def attaquer(self):
        pass

    @abstractmethod
    def attaquer_speciale(self):
        pass

    @abstractmethod
    def deplacement(self, x, y):
        pass

    @abstractmethod
    def mort(self):
        pass


# ------------------------------------
# Développement des classes Personnage


class Personnage(Entite):
    def __init__(self, position: tuple, cooldown: int, niveau: int, inventaire: dict, nom: str):
        super().__init__(position, niveau, cooldown)
        self.inventory = inventaire  # Objet item
        self.nom = nom

    @abstractmethod
    def attaquer(self):
        pass

    @abstractmethod
    def attaquer_speciale(self):
        pass

    def deplacement(self, game, direction):

        if game.rien_autour_position(self.position, direction):
            x, y = self.position
            self.position = eval(Entite.direction[direction])


    def interagir(self):
        """Permet d'utiliser objet"""
        pass

    def levelup(self):
        self.niveau += 1

    def mort(self):
        assert (self.vie == 0)  #Vérifie la mort du personnage
        pass


class Epeiste(Personnage):
    def __init__(self, position, cooldown,nom, niveau = 1, inventaire = {}): # Pour position, à voir comment on génère ça, ptet pas en arg
        super().__init__(position, cooldown, niveau, inventaire, nom)
        self.niveau = niveau
        self.path = "Schema lv epeiste.txt"

    def attaquer(self):
        pass

    def attaquer_speciale(self):
        pass

class Garde(Personnage):
    def __init__(self, position, niveau=1, inventaire={}):
        super().__init__(15, 6, 6, 5, position, 10, niveau, inventaire)
        self.__niveau = niveau

    def attaquer(self):
        pass

    def attaquer_speciale(self):
        pass

    @property
    def niveau(self):
        return (self.__niveau)

    @niveau.setter
    def niveau(self, niveau):
        self.vie = 5 * niveau
        self.attaque += 2
        self.defense += 4
        # self.mana = 5
        # self.vitesse = 5
        self.__niveau = niveau


class Sorcier(Personnage):
    def __init__(self, position, niveau=1, inventaire={}):
        super().__init__(6, 8, 3, 5, position, 13, niveau, inventaire)
        self.__niveau = niveau

    def attaquer(self):
        pass

    def attaquer_speciale(self):
        pass

    @property
    def niveau(self):
        return (self.__niveau)

    @niveau.setter
    def niveau(self, niveau):
        self.vie = 5 * niveau
        self.attaque += 5
        self.defense += 1
        # self.mana = 5
        # self.vitesse = 5
        self.__niveau = niveau

class Druide(Personnage):
    def __init__(self, position, niveau=1, inventaire={}):
        super().__init__(9, 6, 5, 5, position, 13, niveau, inventaire)
        self.__niveau = niveau

    def attaquer(self):
        pass

    def attaquer_speciale(self):
        pass

    @property
    def niveau(self):
        return (self.__niveau)

    @niveau.setter
    def niveau(self, niveau):
        self.vie = 5 * niveau
        self.attaque += 3
        self.defense += 3
        # self.mana = 5
        # self.vitesse = 5
        self.__niveau = niveau


# ----------------------------------
# Développement des classes d'Ennemi

class Ennemi(Entite):
    def __init__(self, niveau, position):
        vie = 5 * niveau
        attaque = 5 * niveau
        defense = 5 * niveau
        mana = 5
        vitesse = 5
        super().__init__(vie, attaque, defense, mana, position, vitesse, niveau)

    @abstractmethod
    def attaquer(self):
        pass

    @abstractmethod
    def attaquer_speciale(self):
        pass

    def deplacement(self):
        pass

    def mort(self):
        pass