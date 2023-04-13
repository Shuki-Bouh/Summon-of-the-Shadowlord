from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont


class Ui_Credits(object):

    # List containing all the widgets of a current window, which able us to clean a window and show new things.
    list_widgets = []

    def setup_Cred(self, MainWindow):
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
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2.addWidget(self.widget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.bouton_menu = QtWidgets.QPushButton(self.centralwidget)
        self.bouton_menu.setObjectName("bouton_menu")
        self.horizontalLayout_2.addWidget(self.bouton_menu)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        # Partie définition des crédits
        self.credit_list = [
            "CRÉDITS",
            "",
            "",
            "----- Développement -----",
            "Cyril MAISANI",
            "David MELIN",
            "",
            "----- Programmation -----",
            "Cyril MAISANI",
            "David MELIN",
            "",
            "----- Musique -----",
            "Cyril MAISANI",
            "",
            "----- Graphismes -----",
            "David MELIN",
            "",
            "----- Testeurs -----",
            "Cyril MAISANI",
            "David MELIN",
            "",
            "",
            "Merci d'avoir jouer à notre jeu ! (^_^)"]

        # Convertit la liste de crédits en un texte avec des sauts de ligne
        self.credit_text = "\n".join(self.credit_list)
        self.scroll_label = QLabel(self.centralwidget)
        self.scroll_label.setAlignment(Qt.AlignCenter)
        self.scroll_label.setGeometry(100, 100, 600, 400)
        self.font = QFont()
        self.font.setPointSize(8)  # ajuster la taille de la police en fonction de vos besoins
        self.scroll_label.setFont(self.font)  # définir la police du QLabel
        self.scroll_label.setText(self.credit_text)
        self.scroll_position = 0  # position initiale de l'étiquette
        self.scroll_defilement = True  # permet de stopper le défilement

        self.timer = QTimer(self.centralwidget)
        self.timer.timeout.connect(self.scroll_credit)
        self.timer.start(24)  # ajuster l'intervalle de temps en fonction de vos besoins

        Ui_Credits.list_widgets.append([self.horizontalLayout_2, 1])
        Ui_Credits.list_widgets.append([self.horizontalLayout_3, 2])
        Ui_Credits.list_widgets.append([self.verticalLayout_2, 3])
        Ui_Credits.list_widgets.append([self.widget, 4])
        Ui_Credits.list_widgets.append([self.widget_2, 5])
        Ui_Credits.list_widgets.append([self.widget_3, 6])
        Ui_Credits.list_widgets.append([self.centralwidget, 7])
        Ui_Credits.list_widgets.append([self.bouton_menu, 8])
        Ui_Credits.list_widgets.append([self.credit_text, 9])
        Ui_Credits.list_widgets.append([self.credit_list, 10])
        Ui_Credits.list_widgets.append([self.scroll_label, 11])
        Ui_Credits.list_widgets.append([self.scroll_position, 12])
        Ui_Credits.list_widgets.append([self.scroll_defilement, 13])
        Ui_Credits.list_widgets.append([self.timer, 14])
        Ui_Credits.list_widgets.append([self.font, 15])

        self.retranslate_Cred(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_Cred(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Summon_of_the_ShadowLand"))
        self.bouton_menu.setText(_translate("MainWindow", "Menu"))

    def scroll_credit(self):
        if self.scroll_defilement:
            self.scroll_position -= 1  # décrémente la position de défilement
            self.scroll_label.move(100, 100 + self.scroll_position)  # met à jour la position de l'étiquette

            if self.scroll_position <= -450:  # ajuster la limite inférieure en fonction de vos besoins
                self.scroll_defilement = False  # réinitialise la position de défilement

    def fermer(self):
        for widget in Ui_Credits.list_widgets:
            widget[0].deleteLater()
        Ui_Credits.list_widgets = []
