from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
import sys


class MyWindow(QWidget):
    def __init__(self, win):
        super().__init__()
        self.win = win

    def build(self):
        self.win.setWindowTitle("Example of QPixmap")
        self.win.setGeometry(100, 100, 500, 300)

        # create a QPixmap object
        self.img = QPixmap("1003880.png")

        # create a QLabel for image
        self.lbl_img = QLabel(self.win)
        self.lbl_img.setScaledContents(True)

        # set the QPximap object to the label image
        self.lbl_img.setPixmap(self.img)
        self.lbl_img.resize(75, 75)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = QWidget()
    mywin = MyWindow(root)
    mywin.build()
    root.show()
    sys.exit(app.exec_())