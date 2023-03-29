import numpy as np
from random import randrange, choice, random
import personnage as perso
import os

class Partie(list):
    """dans self sera contenu les ennemis avec les joueurs (à la position prévue)"""

    def __init__(self, h, l):
        super().__init__()
        self.__h = h + 2 # Pour compenser les False qui apparaissent
        self.__l = l + 2
        self.__generation_map()
        self.map = self.get_map()
        self.joueurs = {}
        self.ennemis = {}

    def __generation_map(self):
        for k in range(self.h):
            self.append([])
            for j in range(self.l):
                if k == 0 or k == self.h-1 or j == 0 or j == self.l-1:
                    self[k].append(False)
                else:
                    self[k].append(None)

    def new_player(self, player):
        x, y = player.position
        self[y][x] = player

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

    def __str__(self):
        canvas = ""
        for k in range(self.h):
            for j in range(self.l-1):
                canvas += str(self[k][j]) + ", "
            canvas += str(self[k][self.l-1])
            canvas += "\n"
        return canvas

if __name__ == '__main__':
    a = Partie(10, 10)
    print(a)
