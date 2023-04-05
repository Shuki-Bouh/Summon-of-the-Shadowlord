import time
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import partie
from Demarrage import *
from GameScreen import *
from win32api import GetSystemMetrics


class MyWidget(QtWidgets.QMainWindow):

    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)

    def __init__(self):
        super().__init__()
        self.launch_Dem()
        self.create_Game()
        print(self.game.ennemis, self.game.joueurs)
        self.ui.bouton_jouer.clicked.connect(self.launch_Game)

    # def keyPressEvent(self, event):
    #     t0_loop = time.time()
    #     for joueur in self.game.joueurs.values():
    #         self.game.mutex.acquire()
    #         if event.key() == Qt.Key_Z:
    #             joueur.deplacement('up')
    #             print("Z")
    #         elif event.key() == Qt.QMouseEvent
    #         elif event.key() == Qt.Key_S:
    #             joueur.deplacement('down')
    #         elif event.key() == Qt.Key_Q:
    #             joueur.deplacement('left')
    #         elif event.key() == Qt.Key_D:
    #             joueur.deplacement('right')
    #         elif event.key() == Qt.Key_Space:
    #             joueur.attaquer()
    #         else:
    #             QWidget().keyPressEvent(event)
    #         self.game.mutex.release()
    #     t1_loop = time.time()
    #     t_loop = t1_loop - t0_loop
    #     print(t_loop)
    #     if t_loop < 1/24:
    #         time.sleep(1/24 - t_loop)
    #     else:
    #         print("Too much computation in this loop")

    def launch_Dem(self):
        try:
            self.ui.close()
        except AttributeError:
            pass
        self.ui = Ui_Demarrage()
        self.ui.setup_Dem(self)
        self.ui.retranslate_Dem(self)

    def launch_Game(self):
        self.ui.close()
        self.ui = Ui_GameScreen()
        self.ui.setup_Jeu(self)
        self.ui.retranslate_Jeu(self)
        # self.painter = QtGui.QPainter()
        # self.ui.conteneur.paintEvent = self.drawEcosysteme

    def create_Game(self):
        """Test spawn et affichage"""
        self.game = partie.Partie(MyWidget.width, MyWidget.height)
        self.game.new_player('Link', 'epeiste')
        self.game.new_player('Impa', 'garde')
        self.game.new_player('Koume', 'sorcier')
        self.game.new_player('Zelda', 'archer')
        self.game.spawn_squelette(1)

    def drawGame(self, *args):
        print("entree fonction")
        self.painter.begin(self.ui.conteneur)
        qp = self.painter
        for player in self.game.joueurs:
            player.draw_perso(qp)
        for ennemy in self.game.ennemis:
            ennemy.dra_ennemi(qp)
        self.painter.end()


if __name__=="__main__":

    app = QtWidgets.QApplication.instance()
    if not app:
        app = QtWidgets.QApplication(sys.argv)

    window = MyWidget()
    window.show()  # Affichage fenêtre
    app.exec_()  # Execution fichier







    # def keyPressEvent(self, event):
    #     t0_loop = time.time()
    #     for joueur in self.game.joueurs.values():
    #         self.game.mutex.acquire()
    #         if event.key() == Qt.Key_Z:
    #             joueur.deplacement('up')
    #             print("Z")
    #         elif event.key() == Qt.QMouseEvent
    #         elif event.key() == Qt.Key_S:
    #             joueur.deplacement('down')
    #         elif event.key() == Qt.Key_Q:
    #             joueur.deplacement('left')
    #         elif event.key() == Qt.Key_D:
    #             joueur.deplacement('right')
    #         elif event.key() == Qt.Key_Space:
    #             joueur.attaquer()
    #         else:
    #             QWidget().keyPressEvent(event)
    #         self.game.mutex.release()
    #     t1_loop = time.time()
    #     t_loop = t1_loop - t0_loop
    #     print(t_loop)
    #     if t_loop < 1/24:
    #         time.sleep(1/24 - t_loop)
    #     else:
    #         print("Too much computation in this loop")

    # aff = threading.Thread(target=printgame)
    # aff.start()