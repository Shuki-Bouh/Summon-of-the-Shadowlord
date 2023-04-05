import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from win32api import GetSystemMetrics


class Ui_GameScreen(object):

    # List containing all the widgets of a current window, which able us to clean a window and show new things.
    list_widgets = []

    # Screen resolution
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)

    def setup_Jeu(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.move(0, 0)
        MainWindow.resize(Ui_GameScreen.width, Ui_GameScreen.height)
        MainWindow.setMinimumSize(QtCore.QSize(Ui_GameScreen.width, Ui_GameScreen.height))
        MainWindow.setMaximumSize(QtCore.QSize(Ui_GameScreen.width, Ui_GameScreen.height))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, Ui_GameScreen.width, Ui_GameScreen.height))
        self.centralwidget.setObjectName("centralwidget")
        self.conteneur = QtWidgets.QWidget(self.centralwidget)
        self.conteneur.setGeometry(QtCore.QRect(0, 0, Ui_GameScreen.width, Ui_GameScreen.height))
        self.conteneur.setObjectName("conteneur")
        MainWindow.setCentralWidget(self.centralwidget)

        pixmap = QtGui.QPixmap("1003880.png")
        pixmap = pixmap.scaled(self.centralwidget.size())
        pal = QtGui.QPalette()
        pal.setBrush(QtGui.QPalette.Background, QtGui.QBrush(pixmap))
        self.centralwidget.lower()
        self.centralwidget.stackUnder(self.centralwidget)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setPalette(pal)

        Ui_GameScreen.list_widgets.append(self.centralwidget)

        self.retranslate_Jeu(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_Jeu(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def close(self):
        for widget in Ui_GameScreen.list_widgets:
            widget[0].deleteLater()
        Ui_GameScreen.list_widgets = []