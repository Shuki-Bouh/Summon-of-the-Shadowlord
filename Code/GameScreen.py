from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QProgressBar
from win32api import GetSystemMetrics

width = int(GetSystemMetrics(0) * 1.25)
height = int(GetSystemMetrics(1) * 1.18)

class Ui_GameScreen(object):

    # List containing all the widgets of a current window, which able us to clean a window and show new things.
    list_widgets = []

    # Screen resolution

    def setup_Jeu(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.move(0, 0)
        MainWindow.resize(width, height)
        MainWindow.setMinimumSize(QtCore.QSize(width, height))
        MainWindow.setMaximumSize(QtCore.QSize(width, height))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, width, height))
        self.centralwidget.setObjectName("centralwidget")
        self.conteneur = QtWidgets.QWidget(self.centralwidget)
        self.conteneur.setGeometry(QtCore.QRect(0, 0, width, height))
        self.conteneur.setObjectName("conteneur")
        MainWindow.setCentralWidget(self.centralwidget)

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
        self.label_vie.setGeometry(50, 50, 200, 20)
        self.label_vie.setStyleSheet("QProgressBar::chunk "
                                     "{"
                                     "background-color: red;"
                                     "}")

        self.label_mana = QProgressBar(self.conteneur)
        self.label_mana.setValue(100)
        self.label_mana.setFormat("Mana")
        self.label_mana.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mana.setGeometry(50, 80, 200, 20)
        self.label_mana.setStyleSheet("QProgressBar::chunk "
                                      "{"
                                      "background-color: green;"
                                      "}")

        self.label_niveau = QLabel("Niveau", self.conteneur)
        self.label_niveau.setGeometry(60, 120, 100, 20)

        self.label_xp = QProgressBar(self.conteneur)
        self.label_xp.setValue(100)
        self.label_xp.setFormat("xp")
        self.label_xp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_xp.setGeometry(50, 140, 200, 20)
        self.label_xp.setStyleSheet("QProgressBar::chunk "
                                    "{"
                                    "background-color: blue;"
                                    "}")

        Ui_GameScreen.list_widgets.append(self.centralwidget)
        Ui_GameScreen.list_widgets.append(self.conteneur)
        Ui_GameScreen.list_widgets.append(self.label_vie)
        Ui_GameScreen.list_widgets.append(self.label_mana)
        Ui_GameScreen.list_widgets.append(self.label_niveau)
        Ui_GameScreen.list_widgets.append(self.label_xp)

        self.retranslate_Jeu(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_Jeu(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def fermer(self):
        for widget in Ui_GameScreen.list_widgets:
            widget[0].deleteLater()
        Ui_GameScreen.list_widgets = []
