from PyQt5 import QtCore, QtGui, QtWidgets
from win32api import GetSystemMetrics
from PyQt5.QtWidgets import QLabel, QProgressBar

width = int(GetSystemMetrics(0) * 1.25)
height = int(GetSystemMetrics(1) * 1.18)


class Ui_Multi(object):

    # List containing all the widgets of a current window, which able us to clean a window and show new things.
    list_widgets = []

    def setup_Multi(self, MainWindow):
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
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        Ui_Multi.list_widgets.append([self.centralwidget, 1])
        Ui_Multi.list_widgets.append([self.horizontalLayout_2, 2])
        Ui_Multi.list_widgets.append([self.horizontalLayout_3, 3])
        Ui_Multi.list_widgets.append([self.verticalLayout_2, 4])
        Ui_Multi.list_widgets.append([self.widget, 5])
        Ui_Multi.list_widgets.append([self.widget_2, 6])
        Ui_Multi.list_widgets.append([self.widget_3, 7])

        self.retranslate_Multi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_Multi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Summon_of_the_ShadowLand"))

    def fermer(self):
        for widget in Ui_Multi.list_widgets:
            del widget[0]
        Ui_Multi.list_widgets = []

    def error418(self):
        pixmap = QtGui.QPixmap("error418.png")
        pal = QtGui.QPalette()
        pal.setBrush(QtGui.QPalette.Background, QtGui.QBrush(pixmap))
        self.centralwidget.lower()
        self.centralwidget.stackUnder(self.centralwidget)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setPalette(pal)
        Ui_Multi.list_widgets.append([pixmap, 9])
        Ui_Multi.list_widgets.append([pal, 10])

    def bouton_menu(self):
        self.bouton_menu = QtWidgets.QPushButton(self.centralwidget)
        self.bouton_menu.setObjectName("bouton_menu")
        self.horizontalLayout_2.addWidget(self.bouton_menu)
        Ui_Multi.list_widgets.append([self.bouton_menu, 8])
