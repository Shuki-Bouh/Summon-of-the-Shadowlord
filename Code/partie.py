import numpy as np
from random import randrange, choice, random
import Code.personnage as perso
import threading
import os

path = os.getcwd()
path = path.split("\\Code")[0] + "\\Data"
os.chdir("C:\\Users\\cyril\\OneDrive\\Documents\\Workspace\\Summon-of-the-Shadowlord\\Data")

class Partie(list):
    """dans self sera contenu les ennemis avec les joueurs (à la position prévue)"""

    def __init__(self, l, h):
        super().__init__()
        self.__h = h + 2 # Pour compenser les False qui apparaissent
        self.__l = l + 2
        self.__generation_map()
        self.map = self.get_map()
        self.joueurs = {}
        self.ennemis = {}

    def __generation_map(self):
        for x in range(self.l):
            self.append([])
            for y in range(self.h):
                if x == 0 or x == self.l-1 or y == 0 or y == self.h-1:
                    self[x].append(False)
                else:
                    self[x].append(None)

    def new_player(self, nom, classe, multi = False):
        differentes_classes = {'epeiste': perso.Epeiste,
                               'garde': perso.Garde,
                               'sorcier': perso.Sorcier,
                               'druide': perso.Druide}
        classe = differentes_classes[classe]
        if not multi:
            joueur = classe(self, (self.l - self.l // 4, self.h // 2), nom)
        else:
            pass # On l'implémentera plus tard
        return

    @property
    def h(self):
        return self.__h

    @property
    def l(self):
        return self.__l

    def get_map(self):
        """Ca permet de faire le lien entre personnage et partie (en appelant la map dans personnage)"""
        return self

    def spawn_ennemi(self, niveau):
        if perso.Ennemi.compteur < 15:
            if random() < 0.8:
                self.spawn_squelette(niveau)
    def spawn_squelette(self, niveau):
        cases_possibles = []
        for i in range(self.h):
            for j in range(self.l):
                if self[j][i] == None:
                    cases_possibles.append((i, j))
        x, y = choice(cases_possibles)
        ennemi = perso.Squelette(self, (x, y), niveau)


    def open_save(self):
        pass

    @staticmethod
    def write_save():
        pass

    def action_mechant(self):
        """Cette fonction va tourner sur une thread avec une clock spécifique qui ralentira la cadence
        (comme dans bca en fait)"""
        while True:
            for mechant in self.ennemis.values():
                if mechant.cible:
                    xs, ys = mechant.position
                    xo, yo = mechant.cible.position

                    # ça c'est nul : je dois reprendre pour qu'il attaque s'il se retrouve à côté... Reflexion reflexion !!
                else:
                    mechant.deplacement()
                    mechant.agro()

    def __str__(self):
        canvas = ""
        for y in range(self.h):
            for x in range(self.l-1):
                canvas += str(self[x][y]) + ", "
            canvas += str(self[x][self.h-1])
            canvas += "\n"
        return canvas

if __name__ == '__main__':
    pass
