from PyQt5 import QtWidgets, QtCore, QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.setGeometry(300, 300, 250, 150)
        self.show()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Q:
            print "Killing"
            self.deleteLater()
        elif event.key() == QtCore.Qt.Key_Enter:
            self.proceed()
        event.accept()

    def proceed(self):
        print "Call Enter Key"

app = QtWidgets.QApplication([])
label = QtWidgets.QLabel('Hello World!')
label.show()
app.exec_()