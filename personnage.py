from abc import abstractmethod, ABCMeta
import numpy as np

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
    def __init__(self, game, position: tuple, cooldown: int, niveau = 1): # En réalité, on peut ne pas mettre tout ça en argument, mais juster générer les stats avec niveau
        self.vie = 0
        self.attaque = 0
        self.defense = 0
        self.mana = 0
        self.path = ''
        self.game = game  # game permet de faire le lien avec la class Partie de partie
        self.h = self.game.h
        self.l = self.game.l
        self.map = self.game.get_map()
        self.__position = position
        self.cooldown = cooldown
        self.__niveau = niveau
        self.niveau = niveau

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

    def deplacement(self, direction):
        if self.game.rien_autour_position(self.position, direction):
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
    def __init__(self, position, cooldown, nom, niveau = 1, inventaire = {}): # Pour position, à voir comment on génère ça, ptet pas en arg
        super().__init__(position, cooldown, niveau, inventaire, nom)
        self.niveau = niveau
        self.path = "Epeiste_lvl.txt"

    def attaquer(self):
        pass

    def attaquer_speciale(self):
        pass

class Garde(Personnage):
    def __init__(self, position, cooldown, nom, niveau=1, inventaire={}):
        super().__init__(position, cooldown, niveau, inventaire, nom)
        self.niveau = niveau
        self.path = "Garde_lvl.txt"

    def attaquer(self):
        pass

    def attaquer_speciale(self):
        pass


class Sorcier(Personnage):
    def __init__(self, position, cooldown, nom, niveau=1, inventaire={}):
        super().__init__(position, cooldown, niveau, inventaire, nom)
        self.niveau = niveau
        self.path = "Sorcier_lvl.txt"

    def attaquer(self):
        pass

    def attaquer_speciale(self):
        pass


class Druide(Personnage):
    def __init__(self, position, cooldown, nom, niveau=1, inventaire={}):
        super().__init__(position, cooldown, niveau, inventaire, nom)
        self.niveau = niveau
        self.path = "Druide_lvl.txt"

    def attaquer(self):
        pass

    def attaquer_speciale(self):
        pass


# ----------------------------------
# Développement des classes d'Ennemi

class Ennemi(Entite):
    def __init__(self, game, niveau):
        """problème avec le init... Soucis avec l'héritage, il ne faudrait peut etre pas le garder, car ici, on fait un spawn aléatoire sur les cases non vides, il n'y a donc pas interet à conserver l'héritage
        Ou alors, il faudrait modifier les arguments du init de entite pour les penser differemment
        D'ailleurs, il y a beaucoup d'aguments dans le init de entite, c'est normal ?"""
        self.vie = 5 * niveau
        self.attaque = 5 * niveau
        self.defense = 5 * niveau
        self.mana = 5
        self.cooldown = 5
        self.map = game.get_map()
        self.position = self.spawn()
        super().__init__(game, self.position, self.cooldown)





    def attaquer(self):
        pass


    def attaquer_speciale(self):
        pass

    def spawn(self):
        list_pos = []
        for k in range(len(self.map)):
            for j in range(len(self.map[0])):
                if self.map[k][j] == None:
                    list_pos.append([k,j])
        if len(list_pos) != 0:
            a = 0
            b = len(list_pos)
            n = np.random.randint(a, b)
            pos = list_pos[n]
            x, y = pos[0], pos[1]
            self.map[x][y] = 'Ennemi'



    def deplacement(self):
        pass

    def mort(self):
        pass