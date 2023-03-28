from abc import abstractmethod, ABCMeta


## ESPACES COMMENTAIRES
# Il faudrait mettre en place la representation des personnages et ennemis, pour pas nous confondre en les manipulant
# plus tard, ie, faire une methode pour ou bien utliser __repr__
# Toutes les entités devraient avoir la même modification de de "__position" donc je mets le get/set dans Entite directement





# --------------------------------------------------------------------------
# Classe mère abstraite Entite, où Personnages et Ennemis héritent de Entite

class Entite(metaclass=ABCMeta):
    """Tous les personnages qui existent dans le jeu"""

    direction = {'up': 'x, y - 1', # C'est peut-être un peu tordu mais c'est plus rapide à coder...
                 'down': 'x, y + 1',
                 'left': 'x - 1, y',
                 'right': 'x + 1 , y'}

    def __init__(self, game, path: str, position: tuple, cooldown: int, niveau = 1): # En réalité, on peut ne pas mettre tout ça en argument, mais juster générer les stats avec niveau
        self.path = path # Permet de lire le fichier dans lequel sont contenues les statistiques du perso pour chaque niveau
        self.__position = position # N'est pas caché car toutes les vérifications de création se trouvent dans Partie
        self.cooldown = cooldown # Est là pour ralentir l'utilisation des attaques
        self.__niveau = niveau
        self.niveau = niveau  # Dans niveau.setter, on va créer vie, attaque, défense et mana
        self.game = game
        self.position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, newpos):
        x1, y1 = self.position
        x2, y2 = newpos
        if self.game[y2][x2] == None:
            self.__position = x2, y2
            self.game[y1][x1] = None
            self.game[y2][x2] = self

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
            self.vie, self.attaque, self.defense, self.mana = lvl[:]

    @abstractmethod
    def attaquer(self):
        pass

    @abstractmethod
    def attaquer_speciale(self):
        pass

    @abstractmethod
    def deplacement(self, direction):
        pass

    @abstractmethod
    def mort(self):
        pass


# ------------------------------------
# Développement des classes Personnage


class Personnage(Entite):
    def __init__(self, game, path: str, position: tuple, cooldown: int, nom: str, inventaire: dict, niveau: int):
        super().__init__(game, path, position, cooldown, niveau)
        self.inventory = inventaire  # Objet item
        self.nom = nom


    @abstractmethod
    def attaquer(self):
        pass

    @abstractmethod
    def attaquer_speciale(self):
        pass

    def deplacement(self, direction):
        x, y = self.position
        x, y = eval(Entite.direction[direction])
        self.position = x, y
    def interagir(self):
        """Permet d'utiliser objet"""
        pass

    def levelup(self):
        self.niveau += 1

    def mort(self):
        assert self.vie == 0  #Vérifie la mort du personnage
        pass

    def __str__(self):
        return self.nom


class Epeiste(Personnage):
    def __init__(self, game, position: tuple, cooldown: int, nom: str, inventaire = {}, niveau = 1):
        # Pour position, à voir comment on génère ça, ptet pas en arg
        super().__init__(game, "Epeiste_lvl.txt", position, cooldown, nom, inventaire, niveau)

    def attaquer(self):
        pass

    def attaquer_speciale(self):
        pass


class Garde(Personnage):
    def __init__(self, position: tuple, cooldown: int, nom: str, inventaire={}, niveau=1):
        super().__init__("Garde_lvl.txt", position, cooldown, nom, inventaire, niveau)

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
    def __init__(self, path: str, position: tuple, cooldown: int, niveau):
        self.niveau = niveau
        super().__init__(path, position, cooldown, niveau)

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

class Squelette(Ennemi):
    compteur = 0
    total_compteur = 0

    def __init__(self, position: tuple, niveau):
        super().__init__("Squelette_lvl.txt", position, cooldown=5, niveau=niveau)
        Squelette.compteur += 1
        Squelette.total_compteur += 1

    def mort(self):
        Squelette.compteur -= 1


if __name__ == '__main__':
    pass