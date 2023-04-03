import time

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
import threading
import partie
from win32api import GetSystemMetrics

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



x = GetSystemMetrics (0)
y = GetSystemMetrics (1)
caseH = x/20
caseL = y/20
#window.resize(x, y)
aff = threading.Thread(target=printgame)
aff.start()
window.show()
app.exec_()