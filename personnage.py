from abc import abstractmethod, ABCMeta

## ESPACES COMMENTAIRES
# Il faudrait mettre en place la representation des personnages et ennemis, pour pas nous confondre en les manipulant
# plus tard, ie, faire une methode pour ou bien utliser __repr__







# --------------------------------------------------------------------------
# Classe mère abstraite Entite, où Personnages et Ennemis héritent de Entite

class Entite(metaclass=ABCMeta):
    """Tous les personnages qui existent dans le jeu"""

    def __init__(self, vie: int, attaque: int, defense: int, mana: int, position: tuple, vitesse: int, niveau = 1):
        self.vie = vie
        self.attaque = attaque
        self.defense = defense
        self.mana = mana
        self.__position = position
        self.vitesse = vitesse
        self.__niveau = niveau

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
    def __init__(self, vie: int, attaque: int, defense: int, mana: int, position: tuple, vitesse: int, niveau: int, inventaire: dict):
        super().__init__(vie, attaque, defense, mana, position, vitesse, niveau)
        self.inventory = inventaire  # Objet item

    @abstractmethod
    def attaquer(self):
        pass

    @abstractmethod
    def attaquer_speciale(self):
        pass

    @property
    def position(self):
        return(self.__position)
    @position.setter
    def position(self, pos):
        "valeur correspond à une liste [x, y]"
        self.__position = pos

    def deplacement(self, x, y):
        pos = self.position
        x_pos, y_pos = pos[0], pos[1]
        x_nouv, y_nouv = x_pos + x, y_pos + y
        self.position = [x_nouv, y_nouv]

    def interagir(self):
        """Permet d'utiliser objet"""
        pass

    def levelup(self):
        self.niveau += 1

    def mort(self):
        assert (self.vie == 0)  #Vérifie la mort du personnage
        pass


class Epeiste(Personnage):
    def __init__(self, position, niveau = 1, inventaire = {}):
        super().__init__(10, 7, 4, 5, position, 15, niveau, inventaire)
        self.__niveau = niveau

    def attaquer(self):
        pass

    def attaquer_speciale(self):
        pass

    @property
    def niveau(self):
        return(self.__niveau)

    @niveau.setter
    def niveau(self, niveau):
        #On peut penser à faire des palier de nuveau, avec des bonus supplémentaires (ex: de 5 en 5 jusqu'au niveau 30)
        self.vie = 5 * niveau
        self.attaque += 4
        self.defense += 2
        """self.mana = 5""" #Mana ne peut pas évoluer, c'est l'équivalent d'endurance, donc elle est fixée pour chaque
        # perso... A la limite, on pourra l'augmenter pour des palier de niveaux
        """self.vitesse = 5""" #Je suis pas convaincu par cette stat
        self.__niveau = niveau



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
        super().__init__(self, vie, attaque, defense, mana, position, vitesse, niveau)

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