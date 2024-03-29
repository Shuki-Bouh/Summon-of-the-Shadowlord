import os
import numpy as np
import time
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import Code.tableau as tableau
import Code.personnage as perso
from Code.GameScreen import *
from Code.Demarrage import *
from Code.Credits import *
from Code.StartScreen import *
from Code.MultiScreen import *
from Code.PauseScreen import *
from Code.NewGameScreen import *
from Code.StatsScreen import *
from Code.DeathScreen import *
from win32api import GetSystemMetrics


class MyWidget(QtWidgets.QMainWindow):

    width = int(GetSystemMetrics(0) * 1.25)
    height = int(GetSystemMetrics(1) * 1.18)

    def __init__(self):
        super().__init__()
        self.ui_demarrage()
        # Récupération des différents personnages jouables
        self.dataPerso = tableau.Tableau.lecture_perso()
        self.listPerso = []  # Récupération des personnages
        self.listNom = []  # Récupération de leur nom
        self.listId = []
        for data in self.dataPerso:
            nom, id, *other = data
            self.listPerso.append(list(data))
            self.listNom.append(nom)
            self.listId.append(id)
        self.personnage = []

    def keyPressEvent(self, event):
        """Gère l'accès aux touches du joueur"""
        t0_loop = time.time()
        for joueur in self.game.joueurs.values():
            if not joueur.vivant:
                del self.timer_refrech
                del self.timer_ennemi
                del self.musique
                self.deces()
            if not self.pause:
                if event.key() == QtCore.Qt.Key_Z:
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
            if event.key() == QtCore.Qt.Key_Escape:
                self.pause = not self.pause
                if self.pause:
                    self.musique.pause()
                else:
                    self.musique.play()
                self.timer_ennemi.start(1000)
            else:
                QWidget().keyPressEvent(event)
            # Sauvegarde automatique
            self.save(joueur)
        t1_loop = time.time()
        t_loop = t1_loop - t0_loop
        if t_loop < 1/10:  # Permet de mettre un cooldown sur le joueur
            time.sleep(1/10 - t_loop)

    def refresh(self):
        """Cette fonction permet de modifier l'affichage sur la fenêtre (et la suppression des ennemis aussi, car il a
        clock assez courte --> 24 Hz)"""
        self.ui.conteneur.update()  # On commence par rafraîchir la position de toutes les entités sur la map
        self.game.suppr_ennemi()  # On supprime tous les ennemis morts

        perso = list(self.game.joueurs.values())[0]  # Pour le perso joué, on met à jour sa vie, son mana et son xp

        update_vie = int(np.round(100 * (perso.vie / perso.vieMax), 0))
        self.ui.label_vie.setValue(update_vie)
        self.ui.label_vie.setFormat("Vie : " + str(perso.vie) + "/" + str(perso.vieMax))

        update_mana = int(np.round(100 * (perso.mana / perso.manaMax), 0))
        self.ui.label_mana.setValue(update_mana)
        self.ui.label_mana.setFormat("Mana : " + str(perso.mana) + "/" + str(perso.manaMax))

        xp_max = 10 * perso.niveau
        update_xp = int(np.round(100 * (perso.xp / xp_max), 0))
        self.ui.label_xp.setValue(update_xp)
        self.ui.label_xp.setFormat("xp : " + str(perso.xp) + "/" + str(10 * perso.niveau))

        self.ui.label_niveau.setText("Niveau : " + str(perso.niveau))

        if self.pause:
            self.timer_ennemi.stop()

    def ui_demarrage(self):
        try:
            self.ui.fermer()
        except AttributeError:
            pass
        # Démarrage fenêtre graphique du menu
        self.ui = Ui_Demarrage()
        self.ui.setup_Dem(self)
        # Connexion signaux/ bouton
        self.ui.bouton_jouer.clicked.connect(self.ui_play)
        self.ui.bouton_multi.clicked.connect(self.ui_multi)
        self.ui.bouton_stats.clicked.connect(self.ui_stats)
        self.ui.bouton_credits.clicked.connect(self.ui_credits)
        self.ui.bouton_quit.clicked.connect(self.close)

    def ui_play(self):
        try:
            self.ui.fermer()
        except AttributeError:
            pass
        # Démarrage fenêtre graphique de la fenêtre de choix de partie
        self.ui = Ui_Start()
        self.ui.setup_Start(self)
        for nom in self.listNom:
            self.ui.Choix_game.addItem(nom)
        # Connexion signaux/ bouton
        self.ui.bouton_jouer.clicked.connect(self.ui_game)
        self.ui.bouton_menu.clicked.connect(self.ui_demarrage)
        self.ui.bouton_com.clicked.connect(self.ui_new_game)

    def ui_new_game(self):
        try:
            self.ui.fermer()
        except AttributeError:
            pass
        # Démarrage fenêtre graphique de la fenêtre de nouveau personnage
        self.ui = Ui_NewGame()
        self.ui.setup_New(self)
        # Connexion signaux/ bouton
        self.ui.bouton_retour.clicked.connect(self.ui_play)
        self.ui.bouton_com.clicked.connect(self.new_game)

    def new_game(self):
        name = self.ui.choix_nom.text()
        classe = self.ui.choix_classe.currentText()
        if 0 < len(name) < 12 and name not in self.listNom:
            if classe == 'Épéiste':
                classe = 'epeiste'
            elif classe == 'Garde':
                classe = 'garde'
            elif classe == 'Sorcier':
                classe = 'sorcier'
            elif classe == 'Archer':
                classe = 'archer'
            self.personnage = [name, classe, 1, ()]
            self.ui_game()

    def ui_game(self):
        if len(self.personnage) == 0:
            if self.ui.Ref_game.text() in self.listNom:
                # On autorise la connexion et on récupère les infos du personnage sélectionné
                self.personnage = [liste for liste in self.listPerso if liste[0] == self.ui.Ref_game.text()][0]
            else:
                return  # Dans le cas où pn n'a pas sélectionné de personnage, on ne peut pas lancer de partie
        # -------Création du jeu-------
        self.create_Game()
        # ---Gestion de la connexion---
        if self.personnage[0] not in self.listNom:
            self.game.write_save(self.personnage[0])
        # -----------------------------
        self.timer_refrech = QTimer()
        self.timer_refrech.timeout.connect(self.refresh)
        self.timer_ennemi = QTimer()
        self.timer_ennemi.timeout.connect(self.game.action_mechant)
        self.pause = False  # Booléen
        # Création de la fenêtre graphique associée
        try:
            self.ui.fermer()
        except AttributeError:
            pass
        # Démarrage fenêtre graphique du jeu
        self.ui = Ui_GameScreen()
        self.ui.setup_Jeu(self)
        # Démarrage musique de fond
        self.musique = QMediaPlayer()
        audio_file = QMediaContent(QUrl.fromLocalFile("Let the battle begin.mp3"))
        self.musique.setMedia(audio_file)
        self.musique.setVolume(10)
        self.musique.play()
        # Démarrage interface graphique des entités
        self.painter = QtGui.QPainter()
        self.ui.conteneur.paintEvent = self.draw_game
        # Mise en place de la clock d'ennemi sur 24Hz
        self.timer_refrech.start(int(1/24 * 1000))
        self.timer_ennemi.start(1000)

    def save(self, joueur):
        self.game.write_save(joueur.nom)

    def ui_multi(self):
        try:
            self.ui.fermer()
        except AttributeError:
            pass
        # Démarrage fenêtre graphique des crédits
        self.ui = Ui_Multi()
        self.ui.setup_Multi(self)
        self.state = False
        # Création d'une barre de progression
        self.chargement = QProgressBar(self.ui.widget)
        self.chargement.setRange(0, 100)
        self.chargement.setValue(0)
        self.chargement.setFormat("Chargement")
        self.chargement.setAlignment(QtCore.Qt.AlignCenter)
        self.chargement.setGeometry(288, 248, 200, 20)
        self.chargement.setStyleSheet("QProgressBar"
                                      "{"
                                      "border : 1px solid black;"
                                      "background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0, stop: 1 );"
                                      "}")
        # Création d'un minuteur qui déclenchera la mise à jour de la barre de progression
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.updateProgressBar)
        # Lancement du minuteur pour une durée de 10 secondes
        self.timer.start(100)

    def ui_multi_attente(self):
        # Connexion signaux/ bouton
        self.ui.bouton_menu.clicked.connect(self.ui_demarrage)

    def updateProgressBar(self):
        currentValue = self.chargement.value()
        compteur = currentValue % 3
        if currentValue == 100:
            self.timer.stop()
            self.state = True
            self.chargement.deleteLater()
            self.ui.error418()
            self.ui.bouton_menu()
            self.ui_multi_attente()
        else:
            self.chargement.setValue(currentValue + 1)
            self.chargement.setFormat("Chargement"+compteur*'.')

    def ui_stats(self):
        try:
            self.ui.fermer()
        except AttributeError:
            pass
        # Démarrage fenêtre graphique des crédits
        self.ui = Ui_Stats()
        self.ui.setup_Stats(self)
        for nom in self.listNom:
            self.ui.comboBox.addItem(nom)
        # Connexion signaux/ bouton
        self.ui.bouton_menu.clicked.connect(self.ui_demarrage)
        self.ui.pushButton_3.clicked.connect(self.statistiques)

    def statistiques(self):
        name = self.ui.comboBox.currentText()
        if name in self.listNom:
            self.player = [liste for liste in self.listPerso if liste[0] == name][0]
            stats = tableau.Tableau.lecture_perso(name=name)
            temps_jeu = int(stats[0][1])
            hour, min, sec = 0, 0, 0
            if temps_jeu >= 60:
                min = temps_jeu//60
                sec = temps_jeu%60
                if min > 60:
                    hour = min//60
                    min = min%60
            else:
                sec = temps_jeu
            time = "{}h {}min {}sec".format(hour, min, sec)
            stats = [self.player[0], self.player[2], self.player[3], time, stats[0][3], stats[0][4], stats[0][5],
                     stats[0][6], stats[0][7], stats[0][2]]
            for k in range(len(stats)):
                value = self.ui.tableWidget.item(k, 0)
                value.setText(str(stats[k]))

    def ui_credits(self):
        try:
            self.ui.fermer()
        except AttributeError:
            pass
        # Démarrage fenêtre graphique des crédits
        self.ui = Ui_Credits()
        self.ui.setup_Cred(self)
        # Connexion signaux/ bouton
        self.ui.bouton_menu.clicked.connect(self.ui_demarrage)

    def create_Game(self):
        """Test spawn et affichage"""
        perso.Entite.timer = time.time()
        self.game = tableau.Tableau(MyWidget.width // 40, MyWidget.height // 40)  # Pour créer des cases sur la map
        if len(self.personnage) == 4:
            nom, classe, niveau, pos = self.personnage[0], self.personnage[1], self.personnage[2], self.personnage[3]
        else:
            nom, classe, niveau, pos = self.personnage[0], self.personnage[2], self.personnage[3], (self.personnage[4], self.personnage[5])
        self.game.new_player(nom, classe, niveau, pos)  # Je suis d'accord, c'est assez restrictif pour le moment
        for k in range(5):
            self.game.spawn_ennemi()

    def draw_game(self, *args):
        self.painter.begin(self.ui.conteneur)
        qp = self.painter
        for player in self.game.joueurs.values():  # Affichage personnages
            x, y = player.position
            x_win = x * width // self.game.l
            y_win = y * height // self.game.h
            player.dessin_image(qp, x_win, y_win)
        for ennemy in self.game.ennemis.values():  # Affichage ennemis
            x, y = ennemy.position
            x_win = x * width // self.game.l
            y_win = y * height // self.game.h
            ennemy.dessin_image(qp, x_win, y_win)
        for arbre in self.game.arbres:
            x, y = arbre.x, arbre.y
            x_win = x * width // self.game.l
            y_win = y * height // self.game.h
            arbre.draw_obj(qp, x_win, y_win)
        for rocher in self.game.rochers:
            x, y = rocher.x, rocher.y
            x_win = x * width // self.game.l
            y_win = y * height // self.game.h
            rocher.draw_obj(qp, x_win, y_win)
        self.painter.end()

    def deces(self):
        try:
            self.ui.fermer()
        except AttributeError:
            pass
        # Démarrage fenêtre graphique des décès
        self.ui = Ui_DeathScreen()
        self.ui.setup_Mort(self)
        # Musique d'ambiance
        self.musique = QMediaPlayer()
        audio_file = QMediaContent(QUrl.fromLocalFile("Death screen.mp3"))
        self.musique.setMedia(audio_file)
        self.musique.setVolume(30)
        self.musique.play()
        # Connexion signaux/ bouton
        self.ui.bouton_quitter.clicked.connect(self.close)


if __name__ == "__main__":
    path = os.getcwd()
    os.chdir(os.path.join(path, "Data"))

    app = QtWidgets.QApplication.instance()
    if not app:
        app = QtWidgets.QApplication(sys.argv)

    window = MyWidget()
    window.show()  # Affichage fenêtre
    app.exec_()  # Execution fichier
