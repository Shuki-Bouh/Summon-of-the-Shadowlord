# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_TestWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Test_Window(object):
    def setupUi(self, Test_Window):
        Test_Window.setObjectName("Test_Window")
        Test_Window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Test_Window)
        self.centralwidget.setObjectName("centralwidget")
        Test_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Test_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        Test_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Test_Window)
        self.statusbar.setObjectName("statusbar")
        Test_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Test_Window)
        QtCore.QMetaObject.connectSlotsByName(Test_Window)

    def retranslateUi(self, Test_Window):
        _translate = QtCore.QCoreApplication.translate
        Test_Window.setWindowTitle(_translate("Test_Window", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Test_Window = QtWidgets.QMainWindow()
    ui = Ui_Test_Window()
    ui.setupUi(Test_Window)
    Test_Window.show()
    sys.exit(app.exec_())
