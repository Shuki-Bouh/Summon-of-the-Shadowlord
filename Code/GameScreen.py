from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QProgressBar
from win32api import GetSystemMetrics

width = int(GetSystemMetrics(0) * 1.25)
height = int(GetSystemMetrics(1) * 1.18)

class Ui_GameScreen(object):

    # List containing all the widgets of a current window, which able us to clean a window and show new things.
    list_widgets = []

    def setup_Jeu(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.move(0, 0)
        MainWindow.resize(width, height)
        MainWindow.setMinimumSize(QtCore.QSize(width, height))
        MainWindow.setMaximumSize(QtCore.QSize(width, height))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo_jeu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, width, height))
        self.centralwidget.setObjectName("centralwidget")
        self.conteneur = QtWidgets.QWidget(self.centralwidget)
        self.conteneur.setGeometry(QtCore.QRect(0, 0, width, height))
        self.conteneur.setObjectName("conteneur")
        MainWindow.setCentralWidget(self.centralwidget)

        self.bouton_save = QtWidgets.QPushButton(self.conteneur)
        self.bouton_save.setGeometry(0, 0, 150, 25)
        self.bouton_save.setObjectName("bouton_save")
        self.bouton_save_quit = QtWidgets.QPushButton(self.conteneur)
        self.bouton_save_quit.setGeometry(150, 0, 150, 25)
        self.bouton_save_quit.setObjectName("bouton_save_quit")
        self.retour_menu = QtWidgets.QPushButton(self.conteneur)
        self.retour_menu.setGeometry(300, 0, 150, 25)
        self.retour_menu.setObjectName("retour_menu")

        pixmap = QtGui.QPixmap("arriere_plan_jeu.png")
        pixmap = pixmap.scaled(self.centralwidget.size())
        pal = QtGui.QPalette()
        pal.setBrush(QtGui.QPalette.Background, QtGui.QBrush(pixmap))
        self.centralwidget.lower()
        self.centralwidget.stackUnder(self.centralwidget)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setPalette(pal)

        self.label_vie = QProgressBar(self.conteneur)
        self.label_vie.setValue(100)
        self.label_vie.setFormat("Vie")
        self.label_vie.setAlignment(QtCore.Qt.AlignCenter)
        self.label_vie.setGeometry(70, 70, 200, 20)
        self.label_vie.setStyleSheet("QProgressBar"
                                     "{"
                                     "border : 1px solid black;"
                                     "background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0, stop: 1 );"
                                     "}")

        self.label_mana = QProgressBar(self.conteneur)
        self.label_mana.setValue(100)
        self.label_mana.setFormat("Mana")
        self.label_mana.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mana.setGeometry(70, 100, 200, 20)
        self.label_mana.setStyleSheet("QProgressBar"
                                      "{"
                                      "border : 1px solid black;"
                                      "background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0, stop: 1);"
                                      "}")

        self.label_niveau_sh = QLabel("Niveau", self.conteneur)
        self.label_niveau_sh.setGeometry(71, 131, 150, 20)
        self.label_niveau_sh.setStyleSheet("color: black;")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_niveau_sh.setFont(font)

        self.label_niveau = QLabel("Niveau", self.conteneur)
        self.label_niveau.setGeometry(70, 130, 150, 20)
        self.label_niveau.setStyleSheet("color: white;")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_niveau.setFont(font)

        self.label_xp = QProgressBar(self.conteneur)
        self.label_xp.setValue(100)
        self.label_xp.setFormat("xp")
        self.label_xp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_xp.setGeometry(70, 160, 200, 20)
        self.label_xp.setStyleSheet("QProgressBar"
                                    "{"
                                    "border : 1px solid black;"
                                    "background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0, stop: 1);"
                                    "}")

        Ui_GameScreen.list_widgets.append([self.centralwidget, 1])
        Ui_GameScreen.list_widgets.append([self.conteneur, 2])
        Ui_GameScreen.list_widgets.append([self.label_vie, 3])
        Ui_GameScreen.list_widgets.append([self.label_mana, 4])
        Ui_GameScreen.list_widgets.append([self.label_niveau, 5])
        Ui_GameScreen.list_widgets.append([self.label_niveau_sh, 6])
        Ui_GameScreen.list_widgets.append([self.label_xp, 7])
        Ui_GameScreen.list_widgets.append([self.bouton_save, 8])
        Ui_GameScreen.list_widgets.append([self.bouton_save_quit, 9])
        Ui_GameScreen.list_widgets.append([self.retour_menu, 10])
        Ui_GameScreen.list_widgets.append([pixmap, 11])
        Ui_GameScreen.list_widgets.append([pal, 12])

        self.retranslate_Jeu(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_Jeu(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Summon_of_the_ShadowLand"))
        self.bouton_save.setText(_translate("MainWindow", "Sauvegarder"))
        self.bouton_save_quit.setText(_translate("MainWindow", "Sauvegarder et quitter"))
        self.retour_menu.setText(_translate("MainWindow", "Retour menu"))

    def fermer(self):
        for widget in Ui_GameScreen.list_widgets:
            del widget[0]
        Ui_GameScreen.list_widgets = []
