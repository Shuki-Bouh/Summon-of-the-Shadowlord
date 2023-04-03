# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setMouseTracking(False)
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(200, 220, 400, 284))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setCheckable(False)
        self.pushButton_4.setChecked(False)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(13, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        spacerItem3 = QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.titre_jeu = QtWidgets.QLabel(self.centralwidget)
        self.titre_jeu.setGeometry(QtCore.QRect(95, 95, 610, 60))
        font = QtGui.QFont()
        font.setFamily("Viner Hand ITC")
        font.setPointSize(28)
        self.titre_jeu.setFont(font)
        self.titre_jeu.setObjectName("titre_jeu")
        self.nom_createurs = QtWidgets.QLabel(self.centralwidget)
        self.nom_createurs.setGeometry(QtCore.QRect(660, 520, 120, 20))
        self.nom_createurs.setObjectName("nom_createurs")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setItalic(True)
        self.statusBar.setFont(font)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton_5, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton_3)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Summon_of_the_ShadowLord.exe"))
        self.pushButton_5.setText(_translate("MainWindow", "Jouer"))
        self.pushButton_4.setText(_translate("MainWindow", "Commencer"))
        self.pushButton.setText(_translate("MainWindow", "Multijoueur"))
        self.pushButton_2.setText(_translate("MainWindow", "Crédits"))
        self.pushButton_3.setText(_translate("MainWindow", "Quitter"))
        self.titre_jeu.setText(_translate("MainWindow", "Summon of the ShadowLord"))
        self.nom_createurs.setText(_translate("MainWindow", "@Shuki // @Melinda"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
