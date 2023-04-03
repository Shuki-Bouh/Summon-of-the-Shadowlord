import time

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
import partie

class MyWidget(QWidget):
    def __init__(self, game):
        super().__init__()
        self.game = game

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
                joueur.deplacement('down')
            elif event.key() == Qt.Key_Space:
                joueur.attaquer()
            else:
                QWidget().keyPressEvent(event)
            self.game.mutex.release()
        t1_loop = time.time()
        t_loop = t1_loop - t0_loop
        if t_loop < 1/24:
            time.sleep(1/24 - t_loop)
        else:
            print("Too much computation in this loop")

app = QApplication([])

game = partie.Partie(10,10)
game.new_player('link', "epeiste")
window = MyWidget(game)
window.show()
app.exec_()