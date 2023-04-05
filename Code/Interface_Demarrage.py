# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_LauncherScreen.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import numpy as np


class Ui_MainProgram(object):

    # List containing all the widgets of a current window, which able us to clean a window and show new things.
    list_widgets = []

    def setup_Dem(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setMouseTracking(False)
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        Ui_MainProgram.list_widgets.append(self.centralwidget)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        Ui_MainProgram.list_widgets.append(self.verticalLayoutWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(200, 220, 400, 284))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        Ui_MainProgram.list_widgets.append(self.verticalLayout_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        Ui_MainProgram.list_widgets.append(self.horizontalLayout)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bouton_jouer = QtWidgets.QPushButton(self.verticalLayoutWidget)
        Ui_MainProgram.list_widgets.append(self.bouton_jouer)
        self.bouton_jouer.setObjectName("bouton_jouer")
        self.horizontalLayout.addWidget(self.bouton_jouer)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.bouton_start = QtWidgets.QPushButton(self.verticalLayoutWidget)
        Ui_MainProgram.list_widgets.append(self.bouton_start)
        self.bouton_start.setObjectName("bouton_start")
        self.horizontalLayout.addWidget(self.bouton_start)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.bouton_multi = QtWidgets.QPushButton(self.verticalLayoutWidget)
        Ui_MainProgram.list_widgets.append(self.bouton_multi)
        self.bouton_multi.setObjectName("bouton_multi")
        self.verticalLayout_2.addWidget(self.bouton_multi)
        spacerItem2 = QtWidgets.QSpacerItem(13, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.bouton_credits = QtWidgets.QPushButton(self.verticalLayoutWidget)
        Ui_MainProgram.list_widgets.append(self.bouton_credits)
        self.bouton_credits.setObjectName("bouton_credits")
        self.verticalLayout_2.addWidget(self.bouton_credits)
        spacerItem3 = QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.bouton_quit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        Ui_MainProgram.list_widgets.append(self.bouton_quit)
        self.bouton_quit.setObjectName("bouton_quit")
        self.verticalLayout_2.addWidget(self.bouton_quit)
        self.titre_jeu = QtWidgets.QLabel(self.centralwidget)
        Ui_MainProgram.list_widgets.append(self.titre_jeu)
        self.titre_jeu.setGeometry(QtCore.QRect(95, 95, 610, 60))
        font = QtGui.QFont()
        font.setFamily("Viner Hand ITC")
        font.setPointSize(28)
        self.titre_jeu.setFont(font)
        self.titre_jeu.setObjectName("titre_jeu")
        self.nom_createurs = QtWidgets.QLabel(self.centralwidget)
        Ui_MainProgram.list_widgets.append(self.nom_createurs)
        self.nom_createurs.setGeometry(QtCore.QRect(660, 540, 120, 20))
        self.nom_createurs.setObjectName("nom_createurs")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        Ui_MainProgram.list_widgets.append(self.menubar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.retranslate_Dem(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.bouton_jouer, self.bouton_start)
        MainWindow.setTabOrder(self.bouton_start, self.bouton_multi)
        MainWindow.setTabOrder(self.bouton_multi, self.bouton_credits)
        MainWindow.setTabOrder(self.bouton_credits, self.bouton_quit)

    def retranslate_Dem(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Summon_of_the_ShadowLord"))
        self.bouton_jouer.setText(_translate("MainWindow", "Jouer"))
        self.bouton_start.setText(_translate("MainWindow", "Commencer"))
        self.bouton_multi.setText(_translate("MainWindow", "Multijoueur"))
        self.bouton_credits.setText(_translate("MainWindow", "Crédits"))
        self.bouton_quit.setText(_translate("MainWindow", "Quitter"))
        self.titre_jeu.setText(_translate("MainWindow", "Summon of the ShadowLord"))
        self.nom_createurs.setText(_translate("MainWindow", "@Shuki // @Melinda"))

    def setup_Jeu(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.move(0, 0)
        MainWindow.setMinimumSize(QtCore.QSize(1920, 1080))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        Ui_MainProgram.list_widgets.append((self.centralwidget))
        self.centralwidget.setObjectName("centralwidget")

        self.retranslate_Jeu(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_Jeu(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Summon_of_the_ShadowLord"))

    def launcherToGame(self, MainWindow):
        for widget in Ui_MainProgram.list_widgets:
            widget.deleteLater()
        Ui_MainProgram.list_widgets = []
        self.setup_Jeu(MainWindow)
        self.retranslate_Jeu(MainWindow)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainProgram()
    ui.setup_Dem(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
