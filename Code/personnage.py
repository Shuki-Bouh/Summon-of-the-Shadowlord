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
        if self.game[x2][y2] is None:
            self.__position = x2, y2
            self.game[x1][y1] = None
            self.game[x2][y2] = self

    @property
    def niveau(self):
        return self.__niveau

    @niveau.setter
    def niveau(self, niveau):
        self.__niveau = niveau
        with open(self.path, 'r') as lvl:
            lvl = lvl.readlines()
            lvl = lvl[self.niveau].split()  # On récupère la ligne correspondant aux stats du niveau
            for k in range(len(lvl)):
                lvl[k] = int(lvl[k])
            self.__viemax, self.attaque, self.defense, self.mana = lvl[:]
            self.__vie = self.__viemax

    @staticmethod
    @abstractmethod
    def coup(attaquant, cible):
        pass

    @staticmethod
    def norm(vect1, vect2):
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
        if x <= 0:
            self.__vie = 0
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
        self.xp = 0
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
        if self.xp > self.niveau * 10:  # C'est un peu arbitraire pour le moment
            self.niveau += 1

    @staticmethod
    def coup(attaquant, cible):
        if (attaquant.defense / cible.defense) < 1:
            vie = cible.vie - np.floor(attaquant.attaque * (attaquant.defense / cible.defense))
        else:
            vie = cible.vie - attaquant.attaque
        if not vie:
            attaquant.xp += cible.xp
            attaquant.levelup()
        cible.vie = vie

    def mort(self):
        """Bon il faut faire quoi là ?"""
        # Si multi : multi va probablement devenir une variable de classe Partie
        # Donc s'il est solo, c'est un game over, comment on fait ?
        # Changement d'image, suppression des ennemis
        # Possibilité de recommencer (par un load où on va modifier les vies)
        # Si multi : il meurt, possibilité de respawn ?
        # Une fois que tous les joueurs sont morts, même game over

        # S'il est solo et que le personnage meurt, on écrit une sauvegarde de l'état actuel de sa partie en mettant
        # une nouvelle variable dans la BDD du style mort=True, ce qui fait qu'au moment de respawn, si mort = True,
        # on lui impose une vie à 10 (vie max s'il est mort niveau 1 du coup), et il peut reprendre sa partie comme il
        # veut. NOTA : dans mort, il faut penser à incrémenter la BDD de 1 pour le compteur de mort aussi.
        # Pour le mutli, si le personnage meurt, le plus simple est quil respawn sur une plateforme prévue
        # (au hasard, en (0,0)), et il n'y a pas de game over à proprement parler.
        pass


class Epeiste(Personnage):
    def __init__(self, game, position: tuple, nom: str, inventaire={}, niveau=1):
        self.cooldown = 0
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
                entity.vie -= 2*self.attaque


class Garde(Personnage):
    def __init__(self, game, position: tuple, nom: str, inventaire={}, niveau=1):
        self.cooldown = 0
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



class Sorcier(Personnage):
    def __init__(self, game, position: tuple, nom: str, inventaire={}, niveau=1):
        self.cooldown = 0
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


class Druide(Personnage):
    def __init__(self, game, position: tuple, nom: str, inventaire={}, niveau=1):
        self.cooldown = 0
        super().__init__(game, "Druide_lvl.txt", position, self.cooldown, nom, inventaire, niveau)

    def attaquer(self):
        """Nota : attaque de druide est un simple coup dans la direction regardée"""
        x, y = self.position
        x_att, y_att = eval(Entite.direction[self.orientation])
        entity = self.game[x_att][y_att]
        if entity in self.game.ennemis.values():
            self.coup(self, entity)

    def attaque_speciale(self, direction=""):  # Pas besoin de direction dans celle-ci
        """
        Nota : attaque spéciale de druide agit sur tous les ennemis dont la distance est au maximum d'une case,
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


# ----------------------------------
# Développement des classes d'Ennemi

class Ennemi(Entite):
    compteur = 0

    def __init__(self, game, path: str, position: tuple, cooldown: int, niveau):
        super().__init__(game, path, position, cooldown, niveau)
        Ennemi.compteur += 1
        self.cible = None
        self.vision = 0

    @abstractmethod
    def attaquer(self):
        pass

    @abstractmethod
    def attaque_speciale(self):
        pass

    @abstractmethod
    def deplacement(self):
        pass

    @staticmethod
    def coup(attaquant, cible):
        if (attaquant.defense / cible.defense) < 1:
            cible.vie -= int(np.floor(attaquant.attaque * (attaquant.defense / cible.defense)))
        else:
            cible.vie -= attaquant.attaque

    def mort(self):
        pass

    def agro(self):
        """Vision : COURT (2 cases) / MOYEN (4 cases) / LONG (6 cases)"""
        dict_normes = {}
        for joueur in self.game.joueurs.values():
            if self.norm(self.position, joueur.position) < self.vision:
                dict_normes[joueur] = self.norm(self.position, joueur.position)
        dict_normes = sorted(dict_normes.items(), key=lambda t: t[1])
        self.cible = dict_normes[0][0]

class Squelette(Ennemi):
    compteur = 0
    total_compteur = 0

    def __init__(self, game, position: tuple, niveau):
        super().__init__(game, "Squelette_lvl.txt", position, cooldown=5, niveau=niveau)
        Squelette.compteur += 1
        Squelette.total_compteur += 1
        self.nom = "Squelette " + str(Squelette.total_compteur)
        self.game.ennemis[self.nom] = self
        self.xp = 10 * self.niveau / 3
        self.vision = 4

    def attaquer(self, direction=""):
        """Nota : attaque de squelette est un simple coup porté si un joueur se situe à une case adjacente"""
        self.coup(self, self.cible)

    def attaque_speciale(self, direction=""):
        """
        Nota : attaque spéciale de squelette est un coup de dégâts (x2), nécessairement réussi.
        Cooldown : COURT (5 sec)
        """
        self.cible.vie -= 2 * self.attaque

    def deplacement(self):
        """Déplacement aléatoire d'une case"""
        if self.cible:
            mechant = self.cible
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
        del self


class Crane(Ennemi):
    compteur = 0
    total_compteur = 0

    def __init__(self, game, position: tuple, niveau):
        super().__init__(game, "Crane_lvl.txt", position, cooldown=5, niveau=niveau)
        Crane.compteur += 1
        Crane.total_compteur += 1
        self.nom = "Crane " + str(Crane.total_compteur)
        self.xp = 10 * self.niveau / 3
        self.game.ennemis[self.nom] = self
        self.vision = 6

    def attaquer(self, direction=""):
        """Nota : attaque de crâne est un simple coup porté si un joueur se situe à une case adjacente"""
        self.coup(self, self.cible)

    def attaque_speciale(self, direction=""):
        """
        Nota : Bump le personnage de 2 cases en arrière (dans la mesure du possible),
        et lui vole 1/3 de sa vie pour se régénérer
        Cooldown : MOYEN (10 sec)
        """
        vol_vie = int(np.floor(self.cible.vie * (1 / 3)))
        self.cible.vie -= vol_vie
        self.vie += vol_vie
        x1, y1 = self.position
        x2, y2 = self.cible.position
        if x1 == x2 :
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

    def deplacement(self, direction=""):
        """Double déplacement"""
        k = 0
        while k != 2:
            k += 1
            if self.cible:
                mechant = self.cible
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


class Armure(Ennemi):
    compteur = 0
    total_compteur = 0

    def __init__(self, game, position: tuple, niveau):
        super().__init__(game, "Armure_lvl.txt", position, cooldown=5, niveau=niveau)
        Armure.compteur += 1
        Armure.total_compteur += 1
        self.nom = "Armure " + str(Armure.total_compteur)
        self.xp = 20 * self.niveau / 3
        self.game.ennemis[self.nom] = self
        self.vision = 2

    def attaquer(self, direction=""):
        """Nota : attaque d'armure est un simple coup porté si un joueur se situe à une case adjacente"""
        self.coup(self, self.cible)

    def attaque_speciale(self, direction=""):
        """
        Nota : Réduit son attaque de moitié pour se redonner 1/3 de sa vie,
        attaque sa cible à coup sûr et la fait reculer d'une case
        Cooldown : LONG (15 sec)
        """
        self.attaque //= 2
        self.vie = int(np.floor(self.vie*(4/3)))
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

    def deplacement(self, direction=""):
        """Déplacement aléatoire d'une case"""
        if self.cible:
            mechant = self.cible
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
            direction = random.choice(tuple(Entite.direction.keys()))
        x, y = self.position
        x, y = eval(Entite.direction[direction])
        self.position = (x, y)

    def mort(self):
        Armure.compteur -= 1
        Ennemi.compteur -= 1
        del self.game.ennemis[self.nom]
        x, y = self.position
        self.game[x][y] = None


class Invocateur(Ennemi):
    compteur = 0
    total_compteur = 0

    def __init__(self, game, position: tuple, niveau):
        super().__init__(game, "Invocateur_lvl.txt", position, cooldown=5, niveau=niveau)
        Invocateur.compteur += 1
        Invocateur.total_compteur += 1
        self.nom = "Invocateur " + str(Invocateur.total_compteur)
        self.xp = 30 * self.niveau / 3
        self.game.ennemis[self.nom] = self
        self.vision = 5

    def attaquer(self, direction=""):
        """Nota : attaque d'invocateur est un simple coup porté si un joueur se situe à une case adjacente"""
        self.coup(self, self.cible)

    def attaque_speciale(self, direction=""):
        """
        Nota : Fais spawn deux crânes à ses côtés pour combattre si cela est possible,
        sinon, il régénère entièrement sa vie. De plus, il porte un coup sûr au joueur.
        Cooldown : LONG (20 sec)
        """
        self.cible.vie -= self.attaque
        if self.game.limite_spawn - Ennemi.compteur >= 2:
            dir_joueur = self.cible.direction
            x, y = self.position
            if dir_joueur == 'up' or dir_joueur == 'down':
                x1, y1 = x - 1, y
                x2, y2 = x + 1, y
            else:
                x1, y1 = x, y - 1
                x2, y2 = x, y + 1
            self.game.spawn_crane(self.game, pos=(x1, y1))
            self.game.spawn_crane(self.game, pos=(x2, y2))
        else:
            self.vie = self.viemax

    def deplacement(self, direction=""):
        """Déplacement aléatoire d'une case"""
        if self.cible:
            mechant = self.cible
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
            direction = random.choice(tuple(Entite.direction.keys()))
        x, y = self.position
        x, y = eval(Entite.direction[direction])
        self.position = (x, y)

    def mort(self):
        Invocateur.compteur -= 1
        Ennemi.compteur -= 1
        del self.game.ennemis[self.nom]
        x, y = self.position
        self.game[x][y] = None


if __name__ == '__main__':
    a = np.sqrt((9-9)**2+(8-6)**2)
    print(a)
    a = np.linalg.norm([(9, 9), (8, 6)])
    print(a)
