import time
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import threading
import partie
from MonAppli import Ui_MainWindow
from win32api import GetSystemMetrics


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self, game):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.game = game

        # Définition de la fenêtre de jeu
        self.height = GetSystemMetrics(0)  # Hauteur écran utilisateur
        self.width = GetSystemMetrics(1)  # Largeur écran utilisateur
        self.move(self.height//2 - 400, self.width//2 - 300)  # Fenêtre centrée sur l'écran




    def keyPressEvent(self, event):
        t0_loop = time.time()
        for joueur in self.game.joueurs.values():
            self.game.mutex.acquire()
            if event.key() == Qt.Key_Z:
                joueur.deplacement('up')
            elif event.key() == Qt.Key_S:
                joueur.deplacement('down')
            elif event.key() == Qt.Key_Q:
                joueur.deplacement('left')
            elif event.key() == Qt.Key_D:
                joueur.deplacement('right')
            elif event.key() == Qt.Key_Space:
                joueur.attaquer()
            else:
                QWidget().keyPressEvent(event)
            self.game.mutex.release()
        t1_loop = time.time()
        t_loop = t1_loop - t0_loop
        print(t_loop)
        if t_loop < 1/24:
            time.sleep(1/24 - t_loop)
        else:
            print("Too much computation in this loop")




def printgame():
    while True:
        print(game)
        time.sleep(1/24)

app = QApplication([])

game = partie.Partie(20,10)
game.new_player('link', "epeiste")
window = MyWidget(game)



window.show()  # Affichage fenêtre
app.exec_()




# aff = threading.Thread(target=printgame)
# aff.start()