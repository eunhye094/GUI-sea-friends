from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic,QtGui
from PyQt5.QtGui import QPixmap

form_class = uic.loadUiType("test_files/test.ui")[0]


class test(QtWidgets.QMainWindow,form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("over")
        self.setFixedSize(800,560)

        self.setMouseTracking(True)
        self.mouseMoveEvent = self.mouse
        clickable(self.label).connect(self.click)

    def click(self):
        print("Right Turtle")
        #self.img = QtWidgets.QLabel()
        #pixmap = QtGui.QPixmap('../images/turtle_white.png')
        #self.img.setPixmap(pixmap)

    def mouse(self,e):
        print(e.x())

def clickable(widget):
    class Filter(QtCore.QObject):

        clicked = QtCore.pyqtSignal()

        def eventFilter(self, obj, event):

            if obj == widget:
                if event.type() == QtCore.QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        return True
            return False

    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    MainFrame = test()
    MainFrame.show()
    app.exec_()