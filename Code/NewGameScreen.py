from PyQt5 import QtCore, QtGui, QtWidgets
from win32api import GetSystemMetrics

width = int(GetSystemMetrics(0) * 1.25)
height = int(GetSystemMetrics(1) * 1.18)


class Ui_NewGame(object):

    # List containing all the widgets of a current window, which able us to clean a window and show new things.
    list_widgets = []

    def setup_New(self, MainWindow):
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
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.conteneur = QtWidgets.QVBoxLayout()
        self.conteneur.setObjectName("conteneur")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget_9 = QtWidgets.QWidget(self.centralwidget)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_4.addWidget(self.widget_9)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2.addWidget(self.widget)
        self.nom_perso = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Viner Hand ITC")
        font.setPointSize(14)
        self.nom_perso.setFont(font)
        self.nom_perso.setAlignment(QtCore.Qt.AlignCenter)
        self.nom_perso.setObjectName("Nom_perso")
        self.verticalLayout_2.addWidget(self.nom_perso)
        self.choix_nom = QtWidgets.QLineEdit(self.centralwidget)
        self.choix_nom.setText("")
        self.choix_nom.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.choix_nom.setObjectName("choix_nom")
        self.verticalLayout_2.addWidget(self.choix_nom)
        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.widget_11 = QtWidgets.QWidget(self.centralwidget)
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_4.addWidget(self.widget_11)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3.addWidget(self.widget_3)
        self.nom_classe = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Viner Hand ITC")
        font.setPointSize(14)
        self.nom_classe.setFont(font)
        self.nom_classe.setAlignment(QtCore.Qt.AlignCenter)
        self.nom_classe.setObjectName("Nom_classe")
        self.verticalLayout_3.addWidget(self.nom_classe)
        self.choix_classe = QtWidgets.QComboBox(self.centralwidget)
        self.choix_classe.setObjectName("Choix_classe")
        self.choix_classe.addItem("")
        self.choix_classe.addItem("")
        self.choix_classe.addItem("")
        self.choix_classe.addItem("")
        self.choix_classe.addItem("")
        self.verticalLayout_3.addWidget(self.choix_classe)
        self.verticalLayout_3.setStretch(0, 10)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.widget_10 = QtWidgets.QWidget(self.centralwidget)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_4.addWidget(self.widget_10)
        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 8)
        self.horizontalLayout_4.setStretch(2, 1)
        self.horizontalLayout_4.setStretch(3, 8)
        self.horizontalLayout_4.setStretch(4, 2)
        self.conteneur.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3.addWidget(self.widget_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_6 = QtWidgets.QWidget(self.centralwidget)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_4.addWidget(self.widget_6)
        self.bouton_com = QtWidgets.QPushButton(self.centralwidget)
        self.bouton_com.setObjectName("bouton_com")
        self.verticalLayout_4.addWidget(self.bouton_com)
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_4.addWidget(self.widget_5)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 2)
        self.verticalLayout_4.setStretch(2, 3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3.addWidget(self.widget_4)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 1)
        self.conteneur.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_7 = QtWidgets.QWidget(self.centralwidget)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout.addWidget(self.widget_7)
        self.bouton_retour = QtWidgets.QPushButton(self.centralwidget)
        self.bouton_retour.setObjectName("bouton_retour")
        self.horizontalLayout.addWidget(self.bouton_retour)
        self.widget_8 = QtWidgets.QWidget(self.centralwidget)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout.addWidget(self.widget_8)
        self.conteneur.addLayout(self.horizontalLayout)
        self.conteneur.setStretch(0, 3)
        self.conteneur.setStretch(1, 2)
        self.conteneur.setStretch(2, 1)
        self.horizontalLayout_2.addLayout(self.conteneur)
        MainWindow.setCentralWidget(self.centralwidget)

        pixmap = QtGui.QPixmap("menu_jouer.jpg")
        pal = QtGui.QPalette()
        pal.setBrush(QtGui.QPalette.Background, QtGui.QBrush(pixmap))
        self.centralwidget.lower()
        self.centralwidget.stackUnder(self.centralwidget)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setPalette(pal)

        Ui_NewGame.list_widgets.append([self.centralwidget, 1])
        Ui_NewGame.list_widgets.append([self.verticalLayout_2, 2])
        Ui_NewGame.list_widgets.append([self.verticalLayout_3, 3])
        Ui_NewGame.list_widgets.append([self.verticalLayout_4, 4])
        Ui_NewGame.list_widgets.append([self.horizontalLayout, 5])
        Ui_NewGame.list_widgets.append([self.horizontalLayout_3, 6])
        Ui_NewGame.list_widgets.append([self.horizontalLayout_3, 7])
        Ui_NewGame.list_widgets.append([self.horizontalLayout_4, 8])
        Ui_NewGame.list_widgets.append([self.widget, 9])
        Ui_NewGame.list_widgets.append([self.widget_2, 10])
        Ui_NewGame.list_widgets.append([self.widget_3, 11])
        Ui_NewGame.list_widgets.append([self.widget_4, 12])
        Ui_NewGame.list_widgets.append([self.widget_5, 13])
        Ui_NewGame.list_widgets.append([self.widget_6, 14])
        Ui_NewGame.list_widgets.append([self.widget_7, 15])
        Ui_NewGame.list_widgets.append([self.widget_8, 16])
        Ui_NewGame.list_widgets.append([self.widget_9, 17])
        Ui_NewGame.list_widgets.append([self.widget_10, 18])
        Ui_NewGame.list_widgets.append([self.widget_11, 19])
        Ui_NewGame.list_widgets.append([self.bouton_com, 20])
        Ui_NewGame.list_widgets.append([self.bouton_retour, 21])
        Ui_NewGame.list_widgets.append([self.conteneur, 22])
        Ui_NewGame.list_widgets.append([self.choix_nom, 23])
        Ui_NewGame.list_widgets.append([self.choix_classe, 24])
        Ui_NewGame.list_widgets.append([self.nom_perso, 25])
        Ui_NewGame.list_widgets.append([self.nom_classe, 26])
        Ui_NewGame.list_widgets.append([pixmap, 16])
        Ui_NewGame.list_widgets.append([pal, 17])

        self.retranslate_New(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_New(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Summon_of_the_ShadowLand"))
        self.nom_perso.setText(_translate("MainWindow", "Nom du personnage\n"
                                                                    "(12 caractères max.)"))
        self.nom_classe.setText(_translate("MainWindow", "Classe du personnage\n"
                                                                    " "))
        self.choix_classe.setItemText(0, _translate("MainWindow", " - Classe du personnage"))
        self.choix_classe.setItemText(1, _translate("MainWindow", "Épéiste"))
        self.choix_classe.setItemText(2, _translate("MainWindow", "Garde"))
        self.choix_classe.setItemText(3, _translate("MainWindow", "Sorcier"))
        self.choix_classe.setItemText(4, _translate("MainWindow", "Archer"))
        self.bouton_com.setText(_translate("MainWindow", "Commencer"))
        self.bouton_retour.setText(_translate("MainWindow", "Retour"))

    def fermer(self):
        for widget in Ui_NewGame.list_widgets:
            del widget[0]
        Ui_NewGame.list_widgets = []
