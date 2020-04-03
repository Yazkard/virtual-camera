from PyQt5 import QtGui, QtCore, QtWidgets

#from PyQt5.QtWidgets import QApplication, QMainWindow

#import sys

class Window(QtWidgets.QMainWindow):

    def __init__(self):

        super().__init__()

        self.title = "PyQt5 Drawing Tutorial"

        self.top= 150

        self.left= 150

        self.width = 1000

        self.height = 1000

        self.setWindowTitle(self.title)

        self.setGeometry(self.top, self.left, self.width, self.height)

        self.image = QtGui.QImage(self.size(), QtGui.QImage.Format_RGB32)
        self.image.fill(QtCore.Qt.white)

        self.show()

    def drawProjection(self, projection_dict):
        used_apex = []
        painter = QtGui.QPainter(self.image)
        painter.setPen(QtGui.QPen(QtCore.Qt.red, 2))
        print(projection_dict)
        for apex in projection_dict.values():
            for apex2 in apex.neighbours:
                if apex2 not in used_apex:
                    apex.print_all()
                    apex2.print_all()
                    print("drawing", apex.x, apex.y, "   to   ",apex2.x, apex2.y)
                    painter.drawLine(apex.x, apex.y, apex2.x, apex2.y)
            used_apex.append(apex)
        self.update()

    def paintEvent(self, event):
        canvasPainter  = QtGui.QPainter(self)
        canvasPainter.drawImage(self.rect(),self.image, self.image.rect() )
    
    def clear(self):
        self.image.fill(QtCore.Qt.white)
        self.update()
        
#     def keyPressEvent(self, event):
#         if event.key() == QtCore.Qt.Key_Q:
#             print("Killing")
#             self.deleteLater()
#         elif event.key() == QtCore.Qt.Key_Enter:
#             self.proceed()
#         event.accept()

#     def proceed(self):
#         print("Call Enter Key")


