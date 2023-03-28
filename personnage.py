from abc import abstractmethod, ABCMeta


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
    def __init__(self, path, position: tuple, cooldown: int, niveau = 1): # En réalité, on peut ne pas mettre tout ça en argument, mais juster générer les stats avec niveau
        self.niveau = niveau  # permet de creer vie, attaque, defense, mana
        self.path = path
        self.__position = position
        self.cooldown = cooldown
        self.__niveau = niveau

    @property
    def niveau(self):
        return (self.__niveau)
    @niveau.setter
    def niveau(self, niveau):
        self.niveau = niveau
        with open(self.path, 'r') as lvl:
            lvl = lvl.readline()
            lvl = lvl[self.niveau] # si je me trompe pas, j'ai récup la ligne correspondant au niveau du gars et j'en ai fait une liste
            lvl = lvl.split()
            self.vie, self.attaque, self.defense, self.mana = lvl[:]

    @abstractmethod
    def attaquer(self):
        pass

    @abstractmethod
    def attaquer_speciale(self):
        pass

    @abstractmethod
    def deplacement(self):
        pass

    @abstractmethod
    def mort(self):
        pass


# ------------------------------------
# Développement des classes Personnage


class Personnage(Entite):
    def __init__(self, path, position: tuple, cooldown: int, nom: str, inventaire: dict, niveau: int):
        super().__init__(path, position, cooldown, niveau)
        self.inventory = inventaire  # Objet item
        self.nom = nom


    @abstractmethod
    def attaquer(self):
        pass

    @abstractmethod
    def attaquer_speciale(self):
        pass

    def deplacement(self):
        pass


    def interagir(self):
        """Permet d'utiliser objet"""
        pass

    def levelup(self):
        self.niveau += 1

    def mort(self):
        assert (self.vie == 0)  #Vérifie la mort du personnage
        pass


class Epeiste(Personnage):
    def __init__(self, position: tuple, cooldown: int, nom: str, inventaire = {}, niveau = 1):
        # Pour position, à voir comment on génère ça, ptet pas en arg
        self.niveau = niveau
        self.path = "Epeiste_lvl.txt"
        super().__init__(self.path, position, cooldown, nom, inventaire, niveau)

    def attaquer(self):
        pass

    def attaquer_speciale(self):
        pass

class Garde(Personnage):
    def __init__(self, position: tuple, cooldown: int, nom: str, inventaire={}, niveau=1):
        # Pour position, à voir comment on génère ça, ptet pas en arg
        self.niveau = niveau
        self.path = "Garde_lvl.txt"
        super().__init__(self.path, position, cooldown, nom, inventaire, niveau)

    def attaquer(self):
        pass

    def attaquer_speciale(self):
        pass


class Sorcier(Personnage):
    def __init__(self, position: tuple, cooldown: int, nom: str, inventaire={}, niveau=1):
        # Pour position, à voir comment on génère ça, ptet pas en arg
        self.niveau = niveau
        self.path = "Sorcier_lvl.txt"
        super().__init__(self.path, position, cooldown, nom, inventaire, niveau)

    def attaquer(self):
        pass

    def attaquer_speciale(self):
        pass


class Druide(Personnage):
    def __init__(self, position: tuple, cooldown: int, nom: str, inventaire={}, niveau=1):
        # Pour position, à voir comment on génère ça, ptet pas en arg
        self.niveau = niveau
        self.path = "Druide_lvl.txt"
        super().__init__(self.path, position, cooldown, nom, inventaire, niveau)

    def attaquer(self):
        pass

    def attaquer_speciale(self):
        pass


# ----------------------------------
# Développement des classes d'Ennemi

class Ennemi(Entite):
    def __init__(self, position: tuple, cooldown: int, niveau):
        self.niveau = niveau
        self.path = ''
        super().__init__(self.path, position, cooldown, niveau)

    def attaquer(self):
        pass

    def attaquer_speciale(self):
        pass

    def deplacement(self):
        pass

    def mort(self):
        pass