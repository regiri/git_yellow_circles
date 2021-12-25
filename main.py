import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_MainWindow


def log_uncought_exeptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls._name_, ex)
    import traceback
    text += "".join(traceback.format_tb(tb))

    print(text)
    QMessageBox.critical(None, 'Error', text)
    quit()


sys.excepthook = log_uncought_exeptions


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
            radius = randint(10, 50)
            for _ in range(randint(5, 11)):
                qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
                x = randint(50, 750)
                y = randint(50, 400)
                qp.drawEllipse(x, y, radius, radius)
            qp.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
