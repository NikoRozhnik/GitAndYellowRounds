import sys
import random


from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi("UI.ui", self)
        self.setFixedSize(800, 570)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellipse(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_ellipse(self, qp):
        qp.setBrush(QColor("yellow"))
        w = h = random.randint(50, 350)
        x = random.randint(0, 800)
        y = random.randint(0, 570)
        if x + w > 800:
            x = x - ((x + w) - 800)
        if y + h > 570:
            y = y - ((y + h) - 570)
        qp.drawEllipse(x, y, w, h)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mn = Main()
    mn.show()
    sys.exit(app.exec())
