from PyQt5 import QtWidgets, QtCore, QtGui
from interface import Window
from logic import Engine

app = QtWidgets.QApplication([])
logic = Engine(1)
window = Window()
window.clear()
window.drawProjection(logic.get_projection())

app.exec_()