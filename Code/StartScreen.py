from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Start(object):

    # List containing all the widgets of a current window, which able us to clean a window and show new things.
    list_widgets = []

    def setup_Start(self, MainWindow):
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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout.addWidget(self.widget_4)
        self.bouton_jouer = QtWidgets.QPushButton(self.centralwidget)
        self.bouton_jouer.setObjectName("bouton_start")
        self.horizontalLayout.addWidget(self.bouton_jouer)
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout.addWidget(self.widget_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
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
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 10)
        self.verticalLayout_2.setStretch(2, 1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        Ui_Start.list_widgets.append([self.horizontalLayout_2, 1])
        Ui_Start.list_widgets.append([self.horizontalLayout_3, 2])
        Ui_Start.list_widgets.append([self.verticalLayout_2, 3])
        Ui_Start.list_widgets.append([self.widget, 4])
        Ui_Start.list_widgets.append([self.widget_2, 5])
        Ui_Start.list_widgets.append([self.widget_3, 6])
        Ui_Start.list_widgets.append([self.centralwidget, 7])
        Ui_Start.list_widgets.append([self.bouton_menu, 8])
        Ui_Start.list_widgets.append([self.horizontalLayout, 9])
        Ui_Start.list_widgets.append([self.widget_4, 10])
        Ui_Start.list_widgets.append([self.widget_5, 11])
        Ui_Start.list_widgets.append([self.bouton_jouer, 12])

        self.retranslate_Start(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_Start(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Summon_of_the_ShadowLand"))
        self.bouton_jouer.setText(_translate("MainWindow", "Jouer"))
        self.bouton_menu.setText(_translate("MainWindow", "Menu"))

    def fermer(self):
        for widget in Ui_Start.list_widgets:
            widget[0].deleteLater()
        Ui_Start.list_widgets = []
