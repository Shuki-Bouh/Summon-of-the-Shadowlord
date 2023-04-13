from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys


class Ui_PauseScreen(QMainWindow):

    # List containing all the widgets of a current window, which able us to clean a window and show new things.
    list_widgets = []

    def setup_Pause(self):
        self.setObjectName("MainWindow")
        self.resize(400, 250)
        self.setMinimumSize(QtCore.QSize(400, 250))
        self.setMaximumSize(QtCore.QSize(400, 250))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")

        self.label_vie = QtWidgets.QProgressBar(self.widget)
        self.label_vie.setValue(100)
        self.label_vie.setFormat("Vie")
        self.label_vie.setAlignment(QtCore.Qt.AlignCenter)
        self.label_vie.setGeometry(250, 70, 118, 23)
        self.label_vie.setStyleSheet("QProgressBar::chunk "
                                     "{"
                                     "background-color: red;"
                                     "}")

        self.label_mana = QtWidgets.QProgressBar(self.widget)
        self.label_mana.setValue(100)
        self.label_mana.setFormat("Mana")
        self.label_mana.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mana.setGeometry(250, 100, 118, 23)
        self.label_mana.setStyleSheet("QProgressBar::chunk "
                                      "{"
                                      "background-color: green;"
                                      "}")

        self.label_xp = QtWidgets.QProgressBar(self.widget)
        self.label_xp.setValue(100)
        self.label_xp.setFormat("xp")
        self.label_xp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_xp.setGeometry(250, 155, 118, 23)
        self.label_xp.setStyleSheet("QProgressBar::chunk "
                                    "{"
                                    "background-color: blue;"
                                    "}")

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(300, 135, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 131, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 111, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 111, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 131, 16))
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(108, 10, 160, 50))
        font = QtGui.QFont()
        font.setFamily("Viner Hand ITC")
        font.setPointSize(26)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout.addWidget(self.widget_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout.addWidget(self.widget_3)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.setCentralWidget(self.centralwidget)

        Ui_PauseScreen.list_widgets.append([self.widget, 1])
        Ui_PauseScreen.list_widgets.append([self.widget_2, 2])
        Ui_PauseScreen.list_widgets.append([self.widget_3, 3])
        Ui_PauseScreen.list_widgets.append([self.horizontalLayout, 4])
        Ui_PauseScreen.list_widgets.append([self.horizontalLayout_2, 5])
        Ui_PauseScreen.list_widgets.append([self.pushButton, 6])
        Ui_PauseScreen.list_widgets.append([self.verticalLayout, 7])
        Ui_PauseScreen.list_widgets.append([self.label, 8])
        Ui_PauseScreen.list_widgets.append([self.label_2, 9])
        Ui_PauseScreen.list_widgets.append([self.label_3, 10])
        Ui_PauseScreen.list_widgets.append([self.label_4, 11])
        Ui_PauseScreen.list_widgets.append([self.label_5, 12])
        Ui_PauseScreen.list_widgets.append([self.label_5, 13])
        Ui_PauseScreen.list_widgets.append([self.label_6, 14])
        Ui_PauseScreen.list_widgets.append([self.label_7, 15])
        Ui_PauseScreen.list_widgets.append([self.label_mana, 16])
        Ui_PauseScreen.list_widgets.append([self.label_xp, 17])
        Ui_PauseScreen.list_widgets.append([self.label_xp, 18])
        Ui_PauseScreen.list_widgets.append([self.centralwidget, 19])

        self.retranslate_Pause(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_Pause(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Summon_of_the_ShadowLand"))
        self.label.setText(_translate("MainWindow", "Niveau :"))
        self.label_2.setText(_translate("MainWindow", "Ennemis vaincus :"))
        self.label_3.setText(_translate("MainWindow", "Squelettes vaincus :"))
        self.label_4.setText(_translate("MainWindow", "Crânes vaincus :"))
        self.label_5.setText(_translate("MainWindow", "Armures vaincus :"))
        self.label_6.setText(_translate("MainWindow", "Invocateurs vaincus :"))
        self.label_7.setText(_translate("MainWindow", "PAUSE"))
        self.pushButton.setText(_translate("MainWindow", "Reprendre"))

    def fermer(self):
        for widget in Ui_PauseScreen.list_widgets:
            widget[0].deleteLater()
        Ui_PauseScreen.list_widgets = []


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window1 = Ui_PauseScreen()
    window1.setup_Pause()
    window1.show()
    sys.exit(app.exec_())