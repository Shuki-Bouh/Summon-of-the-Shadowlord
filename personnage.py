from abc import abstractmethod, ABCMeta

class Entite(metaclass=ABCMeta):
    """Tous les personnages qui existent dans le jeu"""

    def __init__(self):
        self.vie = 0
        self.attaque = 0
        self.defense = 0
        self.mana = 0
        self.position = 0
        self.vitesse = 0

    @abstractmethod
    def attaque(self):
        pass

    @abstractmethod
    def attaque_speciale(self):
        pass

    @abstractmethod
    def deplacement(self):
        pass

    @abstractmethod
    def mort(self):
        pass


class Ennemi(Entite):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def attaque(self):
        pass

    @abstractmethod
    def attaque_speciale(self):
        pass

    def deplacement(self):
        pass

    def mort(self):
        pass


class Personnage(Entite):
    def __init__(self):
        super().__init__()
        self.lvl = 0
        self.invent = 0 # Objet item

    @abstractmethod
    def attaque(self):
        pass

    @abstractmethod
    def attaque_speciale(self):
        pass

    def deplacement(self):
        def interagir(self):
            """Permet d'utiliser objet"""
            pass

    def levelup(self):
        pass

    def mort(self):
        pass


class Epeiste(Personnage):
    def __init__(self):
        super().__init__()

    def attaque(self):
        pass

    def attaque_speciale(self):
        pass


class Garde(Personnage):
    def __init__(self):
        super().__init__()

    def attaque(self):
        pass

    def attaque_speciale(self):
        pass


class Sorcier(Personnage):
    def __init__(self):
        super().__init__()

    def attaque(self):
        pass

    def attaque_speciale(self):
        pass


class Druide(Personnage):
    def __init__(self):
        super().__init__()

    def attaque(self):
        pass

    def attaque_speciale(self):
        pass
