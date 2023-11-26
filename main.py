from PyQt5 import QtWidgets, uic
import sys
import random

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import Qt
from PyQt5 import QtGui


class generate_circles(QtWidgets.QMainWindow):
    def __init__(self):
        super(generate_circles, self).__init__()
        uic.loadUi('UI.ui', self)
        self.show()
        self.event_draw = 0
        self.create_circl.clicked.connect(self.paintcircle)
        self.should_paint_circle = False

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.should_paint_circle:
            painter = QtGui.QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
            for a in range(random.randint(1, 10)):
                first_point = random.randint(-100, 400)
                second_point = random.randint(-100, 400)
                lenght = random.randint(0, 400)
                painter.drawEllipse(first_point, second_point, lenght, lenght)

    def paintcircle(self):
        self.should_paint_circle = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = generate_circles()
    ex.show()
    sys.exit(app.exec())