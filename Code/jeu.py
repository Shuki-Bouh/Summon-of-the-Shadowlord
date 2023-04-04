import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import partie
import Launcher
from win32api import GetSystemMetrics


class MyWidget(QMainWindow):
    def __init__(self, game):
        QMainWindow.__init__(self)
        self.launcher = Launcher.Ui_MainWindow()  # Récupérer la classe de launcher
        self.launcher.setupUi(self)  # Setup la fenêtre créer avec QtDesigner
        self.launcher.retranslateUi(self)  # Appliquer les modifications de nom
        self.game = game

        # Définition de la fenêtre de jeu
        self.height = GetSystemMetrics(0)  # Hauteur écran utilisateur
        self.width = GetSystemMetrics(1)  # Largeur écran utilisateur
        self.move(self.height//2 - 400, self.width//2 - 300)  # Fenêtre centrée sur l'écran

        self.main_loop()

    def main_loop(self):
        self.launcher.bouton_jouer.clicked.connect(self.start_partie)

    def start_partie(self):
        print("Click !")
        self.launcher.close(self)


if __name__ == "__main__":

    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    game = partie.Partie(20, 10)
    game.new_player('link', "epeiste")
    window = MyWidget(game)

    window.show()  # Affichage fenêtre
    app.exec_()  # Execution fichier
