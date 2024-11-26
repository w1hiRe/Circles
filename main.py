import sys
import io
import random
from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtWidgets import QApplication, QMainWindow


class Draw(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Текстовый редактор')
        self.do_paint = False
        self.drawButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        diameter = random.randint(30, 150)
        qp.setBrush(QColor(255, 186, 0))
        qp.drawEllipse(100, 100, diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Draw()
    ex.show()
    sys.exit(app.exec())