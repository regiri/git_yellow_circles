import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


def log_uncought_exeptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls._name_, ex)
    import traceback
    text += "".join(traceback.format_tb(tb))

    print(text)
    QMessageBox.critical(None, 'Error', text)
    quit()


sys.excepthook = log_uncought_exeptions


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.do_paint = False
        self.initUI()

    def initUI(self):
        self.setFixedSize(self.size())
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            from random import randint
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor("yellow"))
            radius = randint(1, 50)
            for _ in range(randint(5, 11)):
                x = randint(50, 750)
                y = randint(50, 400)
                qp.drawEllipse(x, y, radius, radius)
            qp.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
