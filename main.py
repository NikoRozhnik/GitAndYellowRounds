import sys
import random


from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 800, 570)
        self.setWindowTitle("Случайные окружности")
        self.btn = QPushButton("Окружность", self)
        self.btn.resize(750, 30)
        self.btn.move(25, 520)
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
        qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
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
