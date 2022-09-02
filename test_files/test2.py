from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import Qt


def canvas_mouseMoveEvent(e):
    painter = QtGui.QPainter(canvas.pixmap())
    pos = '{0:04d} {1:04d}'.format(e.x(), e.y())
    print(pos)
    # 글자영역을 현재 배경색인 흰색으로 칠한다.
    painter.setPen(Qt.NoPen)
    painter.setBrush(Qt.white)
    painter.drawRect(0, 0, 9 * 16, 32)

    # 좌표 그리기
    painter.setPen(Qt.black)
    painter.drawText(0, 32, pos)

    # 페인터 닫기
    painter.end()

    # 그림판 갱신
    canvas.update()


app = QtWidgets.QApplication([])
window = QtWidgets.QWidget()
window.resize(1280, 800)
# window.setFixedSize(1280, 800)
window.setWindowTitle('MyFirstQt')
window.show()
width = window.width()
height = window.height()

# 그림판 준비
canvas = QtWidgets.QLabel(window)
canvas.setGeometry(0, 300, width, height - 300)
pixmap = QtGui.QPixmap(canvas.width(), canvas.height())
pixmap.fill(Qt.white)
canvas.setPixmap(pixmap)
canvas.show()

canvas.setMouseTracking(True)
canvas.mouseMoveEvent = canvas_mouseMoveEvent

app.exec_()