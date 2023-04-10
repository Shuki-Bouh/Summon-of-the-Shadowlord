from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Demarrage(object):

    # List containing all the widgets of a current window, which able us to clean a window and show new things.
    list_widgets = []

    def setup_Dem(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo_jeu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        MainWindow.setAnimated(True)
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
        self.bouton_jouer = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bouton_jouer.setObjectName("bouton_jouer")
        self.horizontalLayout.addWidget(self.bouton_jouer)
        self.widget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        self.bouton_start = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bouton_start.setObjectName("bouton_start")
        self.horizontalLayout.addWidget(self.bouton_start)
        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 10)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.widget_4 = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2.addWidget(self.widget_4)
        self.bouton_multi = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bouton_multi.setObjectName("bouton_multi")
        self.verticalLayout_2.addWidget(self.bouton_multi)
        self.widget_3 = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2.addWidget(self.widget_3)
        self.bouton_credits = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bouton_credits.setObjectName("bouton_credits")
        self.verticalLayout_2.addWidget(self.bouton_credits)
        self.widget_2 = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2.addWidget(self.widget_2)
        self.bouton_quit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bouton_quit.setObjectName("bouton_quit")
        self.verticalLayout_2.addWidget(self.bouton_quit)
        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 10)
        self.verticalLayout_2.setStretch(3, 50)
        self.verticalLayout_2.setStretch(4, 10)
        self.verticalLayout_2.setStretch(5, 1)
        self.verticalLayout_2.setStretch(6, 10)
        self.titre_jeu = QtWidgets.QLabel(self.centralwidget)
        self.titre_jeu.setGeometry(QtCore.QRect(95, 95, 610, 60))
        font = QtGui.QFont()
        font.setFamily("Viner Hand ITC")
        font.setPointSize(28)
        self.titre_jeu.setFont(font)
        self.titre_jeu.setObjectName("titre_jeu")
        self.nom_createurs = QtWidgets.QLabel(self.centralwidget)
        self.nom_createurs.setGeometry(QtCore.QRect(670, 570, 120, 20))
        self.nom_createurs.setObjectName("nom_createurs")
        MainWindow.setCentralWidget(self.centralwidget)

        Ui_Demarrage.list_widgets.append([self.widget, 1])
        Ui_Demarrage.list_widgets.append([self.widget_2, 2])
        Ui_Demarrage.list_widgets.append([self.widget_3, 3])
        Ui_Demarrage.list_widgets.append([self.widget_4, 4])
        Ui_Demarrage.list_widgets.append([self.centralwidget, 5])
        Ui_Demarrage.list_widgets.append([self.verticalLayoutWidget, 6])
        Ui_Demarrage.list_widgets.append([self.verticalLayout_2, 7])
        Ui_Demarrage.list_widgets.append([self.horizontalLayout, 8])
        Ui_Demarrage.list_widgets.append([self.bouton_start, 9])
        Ui_Demarrage.list_widgets.append([self.bouton_multi, 10])
        Ui_Demarrage.list_widgets.append([self.bouton_jouer, 11])
        Ui_Demarrage.list_widgets.append([self.bouton_credits, 12])
        Ui_Demarrage.list_widgets.append([self.bouton_quit, 13])
        Ui_Demarrage.list_widgets.append([self.titre_jeu, 14])
        Ui_Demarrage.list_widgets.append([self.nom_createurs, 15])

        self.retranslate_Dem(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.bouton_jouer, self.bouton_start)
        MainWindow.setTabOrder(self.bouton_start, self.bouton_multi)
        MainWindow.setTabOrder(self.bouton_multi, self.bouton_credits)
        MainWindow.setTabOrder(self.bouton_credits, self.bouton_quit)

    def retranslate_Dem(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Summon_of_the_ShadowLand"))
        self.bouton_jouer.setText(_translate("MainWindow", "Jouer"))
        self.bouton_start.setText(_translate("MainWindow", "Commencer"))
        self.bouton_multi.setText(_translate("MainWindow", "Multijoueur"))
        self.bouton_credits.setText(_translate("MainWindow", "Crédits"))
        self.bouton_quit.setText(_translate("MainWindow", "Quitter"))
        self.titre_jeu.setText(_translate("MainWindow", "Summon of the ShadowLord"))
        self.nom_createurs.setText(_translate("MainWindow", "@Shuki // @Melinda"))

    def fermer(self):
        for widget in Ui_Demarrage.list_widgets:
            widget[0].deleteLater()
        Ui_Demarrage.list_widgets = []
