# import time
import sys
# import os
# from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QApplication, QMainWindow
# from PyQt5.QtGui import QPixmap
# from PyQt5 import uic
# import threading
import partie
import Launcher
import TestWindow
from win32api import GetSystemMetrics


class MyWidget(QMainWindow):
    def __init__(self, game):
        QMainWindow.__init__(self)
        self.launcher = Launcher.Ui_MainWindow()  # Récupérer la classe de launcher
        self.launcher.setupUi(self)  # Setup la fenêtre créer avec QtDesigner
        self.launcher.retranslateUi(self)  # Appliquer les modifications de nom
        self.gameWindow = TestWindow.Ui_Test_Window()
        self.game = game

        # Définition de la fenêtre de jeu
        self.height = GetSystemMetrics(0)  # Hauteur écran utilisateur
        self.width = GetSystemMetrics(1)  # Largeur écran utilisateur
        self.move(self.height//2 - 400, self.width//2 - 300)  # Fenêtre centrée sur l'écran

        self.main_loop()

    def main_loop(self):
        self.launcher.bouton_jouer.clicked.connect(self.start_partie)

    def start_partie(self):
        print("start")
        self.launcher.close()

        Test_Window = QMainWindow()
        Test_Window.setObjectName("Test_Window")
        Test_Window.resize(800, 600)
        self.centralwidget = QWidget(Test_Window)
        self.centralwidget.setObjectName("centralwidget")
        Test_Window.setCentralWidget(self.centralwidget)

        Test_Window.show()





if __name__=="__main__":

    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    game = partie.Partie(20,10)
    game.new_player('link', "epeiste")
    window = MyWidget(game)

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