from PyQt5 import QtCore, QtGui
from abc import abstractmethod, ABCMeta


class Decors(metaclass=ABCMeta):
    def __init__(self, nom: str, path: str):
        self.nom = nom
        self.path = path

    @abstractmethod
    def draw_obj(self, qp, x_win, y_win):
        pass


class Arbre(Decors):
    def __init__(self):
        nom = 'Arbre'
        path = './Arbre/Idle/Idle.jpg'
        super().__init__(nom, path)
        self.image = QtGui.QImage("./Arbre/Idle/idle.jpg")

    def draw_obj(self, qp, x_win, y_win):
        qp.drawImage(QtCore.QRect(x_win, y_win, 50, 50), self.image)


class Rocher(Decors):
    def __init__(self):
        nom = 'Rocher'
        path = './Rocher/Idle/Idle.jpg'
        super().__init__(nom, path)
        self.image = QtGui.QImage("./Rocher/Idle/idle.jpg")

    def draw_obj(self, qp, x_win, y_win):
        qp.drawImage(QtCore.QRect(x_win, y_win, 50, 50), self.image)


if __name__ == '__main__':
    pass
