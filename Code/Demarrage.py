from PyQt5 import QtCore, QtGui, QtWidgets
from win32api import GetSystemMetrics

width = int(GetSystemMetrics(0) * 1.25)
height = int(GetSystemMetrics(1) * 1.18)


class Ui_Demarrage(object):

    # List containing all the widgets of a current window, which able us to clean a window and show new things.
    list_widgets = []

    def setup_Dem(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.move(width//2-400, height//2-300)
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
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.widget_4 = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2.addWidget(self.widget_4)
        self.bouton_multi = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bouton_multi.setObjectName("bouton_multi")
        self.verticalLayout_2.addWidget(self.bouton_multi)
        self.widget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2.addWidget(self.widget)
        self.bouton_stats = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bouton_stats.setObjectName("bouton_stats")
        self.verticalLayout_2.addWidget(self.bouton_stats)
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
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 10)
        self.verticalLayout_2.setStretch(5, 50)
        self.verticalLayout_2.setStretch(6, 10)
        self.verticalLayout_2.setStretch(7, 1)
        self.verticalLayout_2.setStretch(8, 10)

        self.titre_jeu_sh = QtWidgets.QLabel(self.centralwidget)
        self.titre_jeu_sh.setGeometry(QtCore.QRect(98, 133, 610, 60))
        self.titre_jeu_sh.setStyleSheet("color: black;")
        font = QtGui.QFont()
        font.setFamily("Viner Hand ITC")
        font.setPointSize(28)
        self.titre_jeu_sh.setFont(font)
        self.titre_jeu_sh.setObjectName("titre_jeu_sh")

        self.titre_jeu = QtWidgets.QLabel(self.centralwidget)
        self.titre_jeu.setGeometry(QtCore.QRect(95, 130, 610, 60))
        self.titre_jeu.setStyleSheet("color: white;")
        font = QtGui.QFont()
        font.setFamily("Viner Hand ITC")
        font.setPointSize(28)
        self.titre_jeu.setFont(font)
        self.titre_jeu.setObjectName("titre_jeu")

        self.nom_createurs = QtWidgets.QLabel(self.centralwidget)
        self.nom_createurs.setGeometry(QtCore.QRect(670, 570, 120, 20))
        self.nom_createurs.setObjectName("nom_createurs")
        MainWindow.setCentralWidget(self.centralwidget)

        pixmap = QtGui.QPixmap("accueil_jeu.jpg")
        pal = QtGui.QPalette()
        pal.setBrush(QtGui.QPalette.Background, QtGui.QBrush(pixmap))
        self.centralwidget.lower()
        self.centralwidget.stackUnder(self.centralwidget)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setPalette(pal)

        Ui_Demarrage.list_widgets.append([self.widget_2, 1])
        Ui_Demarrage.list_widgets.append([self.widget_3, 2])
        Ui_Demarrage.list_widgets.append([self.widget_4, 3])
        Ui_Demarrage.list_widgets.append([self.centralwidget, 4])
        Ui_Demarrage.list_widgets.append([self.verticalLayoutWidget, 5])
        Ui_Demarrage.list_widgets.append([self.verticalLayout_2, 6])
        Ui_Demarrage.list_widgets.append([self.horizontalLayout, 7])
        Ui_Demarrage.list_widgets.append([self.bouton_jouer, 8])
        Ui_Demarrage.list_widgets.append([self.bouton_multi, 9])
        Ui_Demarrage.list_widgets.append([self.bouton_stats, 10])
        Ui_Demarrage.list_widgets.append([self.bouton_credits, 11])
        Ui_Demarrage.list_widgets.append([self.bouton_quit, 12])
        Ui_Demarrage.list_widgets.append([self.titre_jeu, 13])
        Ui_Demarrage.list_widgets.append([self.titre_jeu_sh, 14])
        Ui_Demarrage.list_widgets.append([self.nom_createurs, 15])
        Ui_Demarrage.list_widgets.append([pixmap, 16])
        Ui_Demarrage.list_widgets.append([pal, 17])

        self.retranslate_Dem(MainWindow)
        self.bouton_quit.clicked.connect(MainWindow.close)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.bouton_jouer, self.bouton_multi)
        MainWindow.setTabOrder(self.bouton_multi, self.bouton_stats)
        MainWindow.setTabOrder(self.bouton_stats, self.bouton_credits)
        MainWindow.setTabOrder(self.bouton_credits, self.bouton_quit)

    def retranslate_Dem(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Summon_of_the_ShadowLand"))
        self.bouton_jouer.setText(_translate("MainWindow", "Jouer"))
        self.bouton_multi.setText(_translate("MainWindow", "Multijoueur"))
        self.bouton_stats.setText(_translate("MainWindow", "Statistiques"))
        self.bouton_credits.setText(_translate("MainWindow", "Crédits"))
        self.bouton_quit.setText(_translate("MainWindow", "Quitter"))
        self.titre_jeu.setText(_translate("MainWindow", "Summon of the ShadowLord"))
        self.titre_jeu_sh.setText(_translate("MainWindow", "Summon of the ShadowLord"))
        self.nom_createurs.setText(_translate("MainWindow", "@Shuki // @Melinda"))

    def fermer(self):
        for widget in Ui_Demarrage.list_widgets:
            del widget[0]
        Ui_Demarrage.list_widgets = []
