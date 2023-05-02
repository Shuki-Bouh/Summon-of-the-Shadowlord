from PyQt5 import QtCore, QtGui
from abc import abstractmethod, ABCMeta


class Decors(metaclass=ABCMeta):
    def __init__(self, nom: str, path: str, x_pos: int, y_pos: int):
        self.nom = nom
        self.path = path
        self.x = x_pos
        self.y = y_pos

    def __str__(self) -> str:
        return self.nom

    @abstractmethod
    def draw_obj(self, qp, x_win: int, y_win: int) -> None:
        pass


class Arbre(Decors):
    def __init__(self, x_pos: int, y_pos: int):
        nom = 'Arbre'
        path = './Arbre/Idle/Idle.jpg'
        super().__init__(nom, path, x_pos, y_pos)
        self.image = QtGui.QImage("./Arbre/Idle/idle.jpg")

    def draw_obj(self, qp, x_win: int, y_win: int) -> None:
        qp.drawImage(QtCore.QRect(x_win, y_win, 50, 50), self.image)


class Rocher(Decors):
    def __init__(self, x_pos: int, y_pos: int):
        nom = 'Rocher'
        path = './Rocher/Idle/Idle.jpg'
        super().__init__(nom, path, x_pos, y_pos)
        self.image = QtGui.QImage("./Rocher/Idle/idle.jpg")

    def draw_obj(self, qp, x_win: int, y_win: int) -> None:
        qp.drawImage(QtCore.QRect(x_win, y_win, 50, 50), self.image)


if __name__ == '__main__':
    pass
