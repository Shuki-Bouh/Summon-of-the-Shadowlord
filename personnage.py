from abc import abstractmethod, ABCMeta


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
    def niveau(self):
        return(self.__niveau)
    @niveau.setter
    def niveau(self, niv):
        self.__niveau = niv

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
        super().__init__(10, 20, 12, 5, position, 15, niveau, inventaire)
        self.niveau = niveau

    def attaquer(self):
        pass

    def attaquer_speciale(self):
        pass

    @property
    def niveau(self):
        return self.__niveau
    @niveau.setter
    def niveau(self, niveau):
        self.vie = 5 * niveau
        self.attaque = 5
        self.defense = 5
        self.mana = 5
        self.vitesse = 5
        self.__niveau = niveau



class Garde(Personnage):
    def __init__(self, vie, attaque, defense, mana, position, vitesse, niveau, inventaire):
        super().__init__(vie, attaque, defense, mana, position, vitesse, niveau, inventaire)

    def attaquer(self):
        pass

    def attaquer_speciale(self):
        pass


class Sorcier(Personnage):
    def __init__(self, vie, attaque, defense, mana, position, vitesse, niveau, inventaire):
        super().__init__(vie, attaque, defense, mana, position, vitesse, niveau, inventaire)

    def attaquer(self):
        pass

    def attaquer_speciale(self):
        pass


class Druide(Personnage):
    def __init__(self, vie, attaque, defense, mana, position, vitesse, niveau, inventaire):
        super().__init__(vie, attaque, defense, mana, position, vitesse, niveau, inventaire)

    def attaquer(self):
        pass

    def attaquer_speciale(self):
        pass


# ----------------------------------
# Développement des classes d'Ennemi

class Ennemi(Entite):
    def __init__(self, niveau, position):
        vie = 5 * niveau
        attaque = 5
        defense = 5
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