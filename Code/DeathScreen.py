from PyQt5 import QtCore, QtGui, QtWidgets
from win32api import GetSystemMetrics

width = int(GetSystemMetrics(0) * 1.25)
height = int(GetSystemMetrics(1) * 1.18)


class Ui_DeathScreen(object):

    # List containing all the widgets of a current window, which able us to clean a window and show new things.
    list_widgets = []

    def setup_Mort(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.move(width//2-400, height//2-300)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_6 = QtWidgets.QWidget(self.centralwidget)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_2.addWidget(self.widget_6)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("color: white;")
        font = QtGui.QFont()
        font.setFamily("Viner Hand ITC")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)

        self.widget_7 = QtWidgets.QWidget(self.centralwidget)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_2.addWidget(self.widget_7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout.addWidget(self.widget_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)

        self.bouton_quitter = QtWidgets.QPushButton(self.centralwidget)
        self.bouton_quitter.setObjectName("bouton_quitter")
        self.bouton_quitter.setStyleSheet('QPushButton {'
                                          'color: white;'
                                          'background-color: transparent;'
                                          '}')
        self.horizontalLayout.addWidget(self.bouton_quitter)

        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout.addWidget(self.widget_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout.addWidget(self.widget_3)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 5)
        self.verticalLayout.setStretch(2, 15)
        self.verticalLayout.setStretch(3, 3)
        self.verticalLayout.setStretch(4, 2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        pixmap = QtGui.QPixmap("ecran_mort.jpg")
        pal = QtGui.QPalette()
        pal.setBrush(QtGui.QPalette.Background, QtGui.QBrush(pixmap))
        self.centralwidget.lower()
        self.centralwidget.stackUnder(self.centralwidget)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setPalette(pal)

        Ui_DeathScreen.list_widgets.append([self.centralwidget, 1])
        Ui_DeathScreen.list_widgets.append([self.verticalLayout, 2])
        Ui_DeathScreen.list_widgets.append([self.verticalLayout_2, 3])
        Ui_DeathScreen.list_widgets.append([self.horizontalLayout, 4])
        Ui_DeathScreen.list_widgets.append([self.horizontalLayout_2, 5])
        Ui_DeathScreen.list_widgets.append([self.widget, 6])
        Ui_DeathScreen.list_widgets.append([self.widget_2, 7])
        Ui_DeathScreen.list_widgets.append([self.widget_3, 8])
        Ui_DeathScreen.list_widgets.append([self.widget_4, 9])
        Ui_DeathScreen.list_widgets.append([self.widget_5, 10])
        Ui_DeathScreen.list_widgets.append([self.widget_6, 11])
        Ui_DeathScreen.list_widgets.append([self.widget_7, 12])
        Ui_DeathScreen.list_widgets.append([self.label, 13])
        Ui_DeathScreen.list_widgets.append([self.bouton_quitter, 14])
        Ui_DeathScreen.list_widgets.append([pixmap, 15])
        Ui_DeathScreen.list_widgets.append([pal, 16])

        self.retranslate_Mort(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_Mort(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Vous êtes mort...?"))
        self.bouton_quitter.setText(_translate("MainWindow", "Quitter"))

    def fermer(self):
        for widget in Ui_DeathScreen.list_widgets:
            del widget[0]
        Ui_DeathScreen.list_widgets = []