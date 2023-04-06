import time
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import partie
from GameScreen import *
from Demarrage import *
from win32api import GetSystemMetrics


class MyWidget(QtWidgets.QMainWindow):

    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)

    def __init__(self):
        super().__init__()
        print("beginning")
        self.ui_demarrage()
        self.create_Game()
        self.ui.bouton_jouer.clicked.connect(self.ui_game)

    def keyPressEvent(self, event):
        t0_loop = time.time()
        print(self.game)
        for joueur in self.game.joueurs.values():
            print(joueur.position)
            self.game.mutex.acquire()
            if event.key() == QtCore.Qt.Key_Z:
                joueur.deplacement('up')
                print("Z")
            #elif event.key() == Qt.QMouseEvent
            elif event.key() == QtCore.Qt.Key_S:
                joueur.deplacement('down')
            elif event.key() == QtCore.Qt.Key_Q:
                joueur.deplacement('left')
            elif event.key() == QtCore.Qt.Key_D:
                joueur.deplacement('right')
            elif event.key() == QtCore.Qt.Key_Space:
                joueur.attaquer()
            else:
                QWidget().keyPressEvent(event)
            self.game.mutex.release()
        t1_loop = time.time()
        t_loop = t1_loop - t0_loop
        print(t_loop)
        self.ui.conteneur.update()
        if t_loop < 1/24:
            time.sleep(1/24 - t_loop)
        else:
            print("Too much computation in this loop")


    def ui_demarrage(self):
        try:
            self.ui.close()
        except AttributeError:
            pass
        self.ui = Ui_Demarrage()
        self.ui.setup_Dem(self)
        self.ui.retranslate_Dem(self)

    def ui_game(self):
        try:
            self.ui.close()
        except AttributeError:
            pass
        self.ui = Ui_GameScreen()
        self.ui.setup_Jeu(self)
        self.ui.retranslate_Jeu(self)

        self.painter = QtGui.QPainter()
        self.ui.conteneur.paintEvent = self.drawGame

    def create_Game(self):
        """Test spawn et affichage"""
        self.game = partie.Partie(MyWidget.width//10, MyWidget.height//10)
        self.game.new_player('Link', 'epeiste')

    def drawGame(self, *args):
        print("entrée")
        self.painter.begin(self.ui.conteneur)
        qp = self.painter
        for player in self.game.joueurs.values():
            print(player)
            qp.setPen(QtCore.Qt.blue)
            x, y = player.position
            x_win = x * 1920 // self.game.l
            y_win = y * 1080 // self.game.h
            print(x_win)
            qp.drawEllipse(x_win, y_win, 20, 20)
        for ennemy in self.game.ennemis.values():
            print(ennemy)
            qp.setPen(QtCore.Qt.red)
            qp.drawRect(ennemy.position[0], ennemy.position[1], 20, 20)
        self.painter.end()


if __name__ == "__main__":

    app = QtWidgets.QApplication.instance()
    if not app:
        app = QtWidgets.QApplication(sys.argv)

    window = MyWidget()
    window.show()  # Affichage fenêtre
    app.exec_()  # Execution fichier