from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from random import choice
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.button)

    def button(self):
        self.update()

    def paintEvent(self, QPaintEvent):
        qp = QPainter()
        qp.begin(self)
        self.circles(qp)
        qp.end()

    def circles(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        for i in range(2):
            size = choice(range(300))
            qp.drawEllipse(choice(range(300)), choice(range(300)),
                           size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())