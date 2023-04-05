import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import partie
import Interface_Demarrage as I_Dem
from win32api import GetSystemMetrics
import numpy as np


class MyWidget(QMainWindow):
    def __init__(self, game):
        QMainWindow.__init__(self)
        self.window = I_Dem.Ui_MainProgram()  # Récupérer la classe de Interface_Demarrage
        self.window.setup_Dem(self)  # Setup la fenêtre créer avec QtDesigner
        self.window.retranslate_Dem(self)  # Appliquer les modifications de nom
        self.game = game

        # Définition de la fenêtre de jeu
        self.height = GetSystemMetrics(0)  # Hauteur écran utilisateur
        self.width = GetSystemMetrics(1)  # Largeur écran utilisateur
        self.move(self.height//2 - 400, self.width//2 - 300)  # Fenêtre centrée sur l'écran

        self.main_loop()

    def main_loop(self):
        self.window.bouton_jouer.clicked.connect(self.start_partie)

    def start_partie(self):
        self.window.launcherToGame(self)


if __name__ == "__main__":

    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    game = partie.Partie(20, 10)
    game.new_player('link', "epeiste")
    window = MyWidget(game)

    window.show()  # Affichage fenêtre
    app.exec_()  # Execution fichier
