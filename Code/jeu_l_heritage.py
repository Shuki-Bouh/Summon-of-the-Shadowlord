import time
import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import partie
from GameScreen import *
from Demarrage import *
from Credits import *
from StartScreen import *
from MultiScreen import *
from win32api import GetSystemMetrics
import numpy as np

class MyWidget(QtWidgets.QMainWindow):

    width = int(GetSystemMetrics(0) * 1.25)
    height = int(GetSystemMetrics(1) * 1.18)

    def __init__(self):
        super().__init__()
        self.ui_demarrage()
        self.create_Game()

    def keyPressEvent(self, event):
        """Gère l'accès aux touches du joueur"""
        t0_loop = time.time()
        for joueur in self.game.joueurs.values():
            if not joueur.vivant:
                # Dans l'idée, c'est là qu'on lance la sauvegarde automatique et qu'on fait
                # apparaitre l'écran de game over, là ou dans la méthode mort, mais ici
                # serait plus simple, car on a directement accès à l'interface graphique.
                break  # Permet d'arrêter plus ou moins le jeu quand on meurt
            elif event.key() == QtCore.Qt.Key_Z:
                joueur.deplacement('up')
            elif event.key() == QtCore.Qt.Key_S:
                joueur.deplacement('down')
            elif event.key() == QtCore.Qt.Key_Q:
                joueur.deplacement('left')
            elif event.key() == QtCore.Qt.Key_D:
                joueur.deplacement('right')
            elif event.key() == QtCore.Qt.Key_Space:
                joueur.attaquer()
            elif event.key() == QtCore.Qt.Key_E:
                joueur.attaque_speciale()
            else:
                QWidget().keyPressEvent(event)
        t1_loop = time.time()
        t_loop = t1_loop - t0_loop
        if t_loop < 1/10:  # Permet de mettre un cooldown sur le joueur
            time.sleep(1/10 - t_loop)

    def refresh(self):
        """Cette fonction permet de modifier l'affichage sur la fenêtre (et la suppression des ennemis aussi car il a
        clock assez courte --> 24 Hz)"""
        self.ui.conteneur.update()  # On commence par rafraîchir la position de toutes les entitées sur la map
        self.game.suppr_ennemi()  # On supprime tous les ennemis morts

        perso = list(self.game.joueurs.values())[0]  # Pour le perso occurent, on met à jour sa vie, son mana et son xp

        update_vie = int(np.round(100 * (perso.vie / perso.viemax), 0))
        self.ui.label_vie.setValue(update_vie)
        self.ui.label_vie.setFormat("Vie : " + str(perso.vie) + "/" + str(perso.viemax))

        update_mana = int(np.round(100 * (perso.mana / perso.manamax), 0))
        self.ui.label_mana.setValue(update_mana)
        self.ui.label_mana.setFormat("Mana : " + str(perso.mana) + "/" + str(perso.manamax))

        xp_max = 10 * perso.niveau
        update_xp = int(np.round(100 * (perso.xp / xp_max), 0))
        self.ui.label_xp.setValue(update_xp)
        self.ui.label_xp.setFormat("xp : " + str(perso.xp) + "/" + str(10 * perso.niveau))

        self.ui.label_niveau.setText("Niveau : " + str(perso.niveau))

    def ui_demarrage(self):
        try:
            self.ui.fermer()
        except AttributeError:
            pass
        # Démarrage fenêtre graphique du menu
        self.ui = Ui_Demarrage()
        self.ui.setup_Dem(self)
        self.ui.retranslate_Dem(self)
        # Connexion signaux/ bouton
        self.ui.bouton_jouer.clicked.connect(self.ui_game)
        self.ui.bouton_quit.clicked.connect(self.close)
        self.ui.bouton_credits.clicked.connect(self.ui_credits)
        self.ui.bouton_multi.clicked.connect(self.ui_multi)
        self.ui.bouton_start.clicked.connect(self.ui_newgame)

    def ui_game(self):
        try:
            self.ui.fermer()
        except AttributeError:
            pass
        # Démarrage fenêtre graphique du jeu
        self.ui = Ui_GameScreen()
        self.ui.setup_Jeu(self)
        self.ui.retranslate_Jeu(self)
        # Démarrage musique de fond
        self.player = QMediaPlayer()
        audio_file = QMediaContent(QUrl.fromLocalFile("Let the battle begin.mp3"))
        self.player.setMedia(audio_file)
        self.player.play()
        # Démarrage interface graphique des entités
        self.painter = QtGui.QPainter()
        self.ui.conteneur.paintEvent = self.drawGame
        # Mise en place de la clock d'ennemi sur 24Hz
        self.timer = QTimer()
        self.timer.timeout.connect(self.refresh)
        self.timer.start(int(1/24 * 1000))
        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.game.action_mechant)
        self.timer2.start(1000)

    def ui_credits(self):
        try:
            self.ui.fermer()
        except AttributeError:
            pass
        # Démarrage fenêtre graphique des crédits
        self.ui = Ui_Credits()
        self.ui.setup_Cred(self)
        self.ui.retranslate_Cred(self)
        # Connexion signaux/ bouton
        self.ui.bouton_menu.clicked.connect(self.ui_demarrage)

    def ui_multi(self):
        try:
            self.ui.fermer()
        except AttributeError:
            pass
        # Démarrage fenêtre graphique des crédits
        self.ui = Ui_Multi()
        self.ui.setup_Multi(self)
        self.ui.retranslate_Multi(self)
        # Connexion signaux/ bouton
        self.ui.bouton_menu.clicked.connect(self.ui_demarrage)

    def ui_newgame(self):
        try:
            self.ui.fermer()
        except AttributeError:
            pass
        # Démarrage fenêtre graphique de la fenêtre de nouveau jeu
        self.ui = Ui_Start()
        self.ui.setup_Start(self)
        self.ui.retranslate_Start(self)
        # Connexion signaux/ bouton
        self.ui.bouton_menu.clicked.connect(self.ui_demarrage)
        self.ui.bouton_jouer.clicked.connect(self.ui_game)

    def create_Game(self):
        """Test spawn et affichage"""
        self.game = partie.Partie(MyWidget.width//40, MyWidget.height//40)  # Pour créer des cases sur la map
        self.game.new_player('Link', 'epeiste')  # Je suis d'accord, c'est assez restrictif pour le moment
        for k in range(5):
            self.game.spawn_ennemi()

    def drawGame(self, *args):
        self.painter.begin(self.ui.conteneur)
        qp = self.painter
        for player in self.game.joueurs.values():  # Affichage personnages
            x, y = player.position
            x_win = x * MyWidget.width // self.game.l
            y_win = y * MyWidget.height // self.game.h
            player.dessinImage(qp, x_win, y_win)
        for ennemy in self.game.ennemis.values():  # Affichage ennemis
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