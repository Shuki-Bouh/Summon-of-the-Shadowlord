import personnage as perso
import numpy as np


class Partie(list):
    """dans self sera contenu les ennemis avec les joueurs (à la position prévue)"""

    def __init__(self, h, l):
        super().__init__()
        self.__h = h + 2 # Pour compenser les False qui apparaissent
        self.__l = l + 2
        self.__generation_map()
        self.map = self.get_map()
        self.entites = {}

    def __generation_map(self):
        for k in range(self.h+3):
            self.append([])
            for j in range(self.l+3):
                if k == 0 or k == self.h-1 or j == 0 or j == self.l-1:
                    self[k].append(False)
                else:
                    self[k].append(None)

    @property
    def h(self):
        return self.__h

    @property
    def l(self):
        return self.__l

    def get_map(self):
        """Ca permet de faire le lien entre personnage et partie (en appelant la map dans personnage)"""
        return self

    def rien_autour_position(self, pos, direction):
        x, y = pos # x corespond au self.l et y au self.h
        if direction == 'up' and self[y-1][x] == None:
            return True
        elif direction == 'down' and self[y+1][x] == None:
            return True
        elif direction == 'left' and self[y][x-1] == None:
            return True
        elif direction == 'right' and self[y][x+1] == None:
            return True
        return False

    def spawn_ennemi(self):
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
            return (x,y)

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
    a._l = 11
    print(a.l)
