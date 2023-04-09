import threading
import time
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import partie
from GameScreen import *
from Demarrage import *
from win32api import GetSystemMetrics
import numpy as np

class MyWidget(QtWidgets.QMainWindow):

    width = int(GetSystemMetrics(0) * 1.25)
    height = int(GetSystemMetrics(1) * 1.18)

    def __init__(self):
        super().__init__()
        print("beginning")
        self.ui_demarrage()
        self.create_Game()
        self.ui.bouton_jouer.clicked.connect(self.ui_game)

    def keyPressEvent(self, event):
        t0_loop = time.time()
        for joueur in self.game.joueurs.values():
            self.game.mutex.acquire()
            if event.key() == QtCore.Qt.Key_Z:
                joueur.deplacement('up')
            #elif event.key() == Qt.QMouseEvent
            elif event.key() == QtCore.Qt.Key_S:
                joueur.deplacement('down')
            elif event.key() == QtCore.Qt.Key_Q:
                joueur.deplacement('left')
            elif event.key() == QtCore.Qt.Key_D:
                joueur.deplacement('right')
            elif event.key() == QtCore.Qt.Key_Space:
                joueur.attaquer()
            # elif event.key() == QtCore.Qt.Key_E:  # Ca bug, mais je sais pas pourquoi...
            #     joueur.attaque_speciale()
            else:
                QWidget().keyPressEvent(event)
            self.game.mutex.release()
        t1_loop = time.time()
        t_loop = t1_loop - t0_loop
        if t_loop < 1/24:
            time.sleep(1/24 - t_loop)
        else:
            print("Too much computation in this loop")

    def refresh(self):
        while True:
            t0 = time.time()

            self.ui.conteneur.update()
            perso = list(self.game.joueurs.values())[0]
            xp_max = 10 * perso.niveau
            update_vie = int(np.round(100*(perso.vie/perso.viemax), 0))
            update_mana = int(np.round(100*(perso.mana/perso.manamax), 0))
            update_xp = int(np.round(100*(perso.xp/xp_max), 0))

            self.ui.label_vie.setValue(update_vie)
            self.ui.label_vie.setFormat("Vie : " + str(perso.vie) + "/" + str(perso.viemax))

            self.ui.label_mana.setValue(update_mana)
            self.ui.label_mana.setFormat("Mana : " + str(perso.mana) + "/" + str(perso.manamax))

            self.ui.label_xp.setValue(update_xp)
            self.ui.label_xp.setFormat("xp : " + str(perso.xp) + "/" + str(10*perso.niveau))

            self.ui.label_niveau.setText("Niveau : " + str(perso.niveau))

            t1 = time.time()
            if t1 - t0 < 1/10:
                time.sleep(1/10 - t1 + t0)
            else:
                print("c'est cassé")

    def ui_demarrage(self):
        try:
            self.ui.fermer()
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

        maj = threading.Thread(target=self.refresh)
        maj.start()

    def create_Game(self):
        """Test spawn et affichage"""
        self.game = partie.Partie(MyWidget.width//40, MyWidget.height//40)
        self.game.new_player('Link', 'epeiste')
        for k in range(5):
            self.game.spawn_ennemi(1)
        self.game.start()

    def drawGame(self, *args):
        self.painter.begin(self.ui.conteneur)
        qp = self.painter
        for player in self.game.joueurs.values():
            x, y = player.position
            x_win = x * MyWidget.width // self.game.l
            y_win = y * MyWidget.height // self.game.h
            player.dessinImage(qp, x_win, y_win)
        for ennemy in self.game.ennemis.values():
            x, y = ennemy.position
            x_win = x * MyWidget.width // self.game.l
            y_win = y * MyWidget.height // self.game.h
            ennemy.dessinImage(qp, x_win, y_win)
        self.painter.end()


if __name__ == "__main__":

    app = QtWidgets.QApplication.instance()
    if not app:
        app = QtWidgets.QApplication(sys.argv)

    window = MyWidget()
    window.show()  # Affichage fenêtre
    app.exec_()  # Execution fichier