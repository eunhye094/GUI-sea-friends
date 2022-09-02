from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic,QtGui
from PyQt5.QtGui import QPixmap

import random

form_class3 = uic.loadUiType("ui_files/game.ui")[0]

class game(QtWidgets.QMainWindow,form_class3):
    bingo_25_state = [] #빙고판
    for i in range(25):
        bingo_25_state.append('none')
    bingo_5_state = [] #빙고후보

    bingo_5 = [] #빙고판 라벨
    bingo_25 = [] #빙고후보 라벨

    image = ['./images/starfish_black.png', './images/dolphin_white.png', './images/clownfish_white.png', './images/bluefish_white.png', './images/yellowtang_white.png', './images/seahorse_white.png', './images/turtle_white.png', './images/whale_white.png', './images/shrimp_white.png']
    for i in range(5):
        bingo_5_state.append(random.choice(image))

    select = 'none'

    score_num = 0
    bingo_num = 0
    shark_num = 0
    tentacle_num = 0

    count = 0
    tentacle_count = 0; tentacle_label = ''; tentacle_index = -1

    def __init__(self):
        super(game, self).__init__()
        self.setupUi(self)

        self.setWindowTitle("game")
        self.setFixedSize(1200,700)

        self.bingo_5.extend([self.bingo_5_1, self.bingo_5_2, self.bingo_5_3, self.bingo_5_4, self.bingo_5_5])
        self.bingo_25.extend([self.bingo_25_1, self.bingo_25_2, self.bingo_25_3, self.bingo_25_4, self.bingo_25_5,
                             self.bingo_25_6, self.bingo_25_7, self.bingo_25_8, self.bingo_25_9, self.bingo_25_10,
                             self.bingo_25_11, self.bingo_25_12, self.bingo_25_13, self.bingo_25_14, self.bingo_25_15,
                             self.bingo_25_16, self.bingo_25_17, self.bingo_25_18, self.bingo_25_19, self.bingo_25_20,
                             self.bingo_25_21, self.bingo_25_22, self.bingo_25_23, self.bingo_25_24, self.bingo_25_25])

        score_text = '{}'.format(self.score_num)
        self.score.setText(score_text)
        bingo_text = '{}'.format(self.bingo_num)
        self.bingo.setText(bingo_text)
        shark_text = '{}'.format(self.shark_num)
        self.shark.setText(shark_text)
        tentacle_text = '{}'.format(self.tentacle_num)
        self.tentacle.setText(tentacle_text)

        for i in range(5):
            self.bingo_5[i].setPixmap(QPixmap(self.bingo_5_state[i]))

        self.setEvent()

    def sharkClick(self):
        if (self.select == 'none' and self.shark_num > 0):
            self.select = 'shark'

    def tentacleClick(self):
        if (self.select == 'none' and self.tentacle_num > 0):
            self.select = 'tentacle'

    def bingo5Click(self, label, index):
        if (self.select == 'none'):
            self.select = self.bingo_5_state[index]
            label.setPixmap(QPixmap(''))

    def bingo5Set(self):
        self.count = 0
        self.bingo_5_state=[]

        for i in range(5):
            self.bingo_5_state.append(random.choice(self.image))
            self.bingo_5[i].setPixmap(QPixmap(self.bingo_5_state[i]))
            self.bingo_5[i].repaint()

    def bingo25Click(self, label, index):
        if (self.bingo_25_state[index]!='none'):
            if (self.select == 'shark'):
                self.bingo_25_state[index]='none'
                self.select='none'
                label.setPixmap(QPixmap(''))
                label.repaint()
                self.shark_num -= 1
                shark_text = '{}'.format(self.shark_num)
                self.shark.setText(shark_text)
                self.shark.repaint()
            elif (self.select=='tentacle'):
                if (self.tentacle_count==0):
                    self.tentacle_label = label
                    self.tentacle_index = index
                    self.tentacle_count += 1
                else:
                    self.select = 'none'
                    temp = self.bingo_25_state[index]
                    self.bingo_25_state[index] = self.bingo_25_state[self.tentacle_index]
                    self.bingo_25_state[self.tentacle_index] = temp
                    label.setPixmap(QPixmap(self.bingo_25_state[index]))
                    self.tentacle_label.setPixmap(QPixmap(self.bingo_25_state[self.tentacle_index]))
                    label.repaint()
                    self.tentacle_label.repaint()
                    self.bingo25Check(self.tentacle_index)
                    self.bingo25Check(index)
                    self.tentacle_num -= 1
                    tentacle_text = '{}'.format(self.tentacle_num)
                    self.tentacle.setText(tentacle_text)
                    self.tentacle.repaint()
                    self.tentacle_label = ''
                    self.tentacle_index = -1
                    self.tentacle_count = 0
        elif (self.select != 'none' and self.select != 'shark' and self.select != 'tentacle'):
            self.count += 1
            self.score_num += 30
            self.bingo_25_state[index] = self.select
            label.setPixmap(QPixmap(self.select))
            label.repaint()
            score_text = '{}'.format(self.score_num)
            self.score.setText(score_text)
            self.score.repaint()
            self.select = 'none'
            self.bingo25Check(index)

        if self.count == 5:
            self.bingo5Set()

        if not('none' in self.bingo_25_state):
            print("끝") #구현 : 게임 끝 처리

    def bingo25Check(self, index):
        bingo_count = 0

        row_bingo = [0, 0]; col_bingo = [0,0]; dia_bingo=[0,0]
        row = [[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]]
        col = [[0,5,10,15,20],[1,6,11,16,21],[2,7,12,17,22],[3,8,13,18,23],[4,9,14,19,24]]
        dia = [[0,6,12,18,24], [4,8,12,16,20]]

        for i in range(5):
            if (index in row[i]):
                bingo_check = 0; temp = ''
                for j in range(5):
                    if (self.bingo_25_state[row[i][j]]!='./images/starfish_black.png' and self.bingo_25_state[row[i][j]]!='none'):
                        temp = self.bingo_25_state[row[i][j]]
                        break
                for j in range(5):
                    if (self.bingo_25_state[row[i][j]]=='./images/starfish_black.png' or temp == self.bingo_25_state[row[i][j]]):
                        bingo_check += 1
                if (bingo_check==5):
                    row_bingo = [1, i]
                    bingo_count += 1

            if (index in col[i]):
                bingo_check = 0; temp = ''
                for j in range(5):
                    if (self.bingo_25_state[col[i][j]] != './images/starfish_black.png' and self.bingo_25_state[col[i][j]] != 'none'):
                        temp = self.bingo_25_state[col[i][j]]
                        break
                for j in range(5):
                    if (self.bingo_25_state[col[i][j]] == './images/starfish_black.png' or temp == self.bingo_25_state[col[i][j]]):
                        bingo_check += 1
                if (bingo_check == 5):
                    col_bingo = [1, i]
                    bingo_count += 1
        for i in range(2):
            if (index in dia[i]):
                bingo_check = 0; temp = ''
                for j in range(5):
                    if (self.bingo_25_state[dia[i][j]] != './images/starfish_black.png' and self.bingo_25_state[dia[i][j]] != 'none'):
                        temp = self.bingo_25_state[dia[i][j]]
                        break
                for j in range(5):
                    if (self.bingo_25_state[dia[i][j]] == './images/starfish_black.png' or temp == self.bingo_25_state[dia[i][j]]):
                        bingo_check += 1
                if (bingo_check == 5):
                    dia_bingo = [1, i]
                    bingo_count += 1

        for j in range(5):
            if (row_bingo[0] == 1):
                self.bingo_25_state[row[row_bingo[1]][j]] = 'none'
                self.bingo_25[row[row_bingo[1]][j]].setPixmap(QPixmap(''))
            if (col_bingo[0]==1):
                self.bingo_25_state[col[col_bingo[1]][j]] = 'none'
                self.bingo_25[col[col_bingo[1]][j]].setPixmap(QPixmap(''))
            if (dia_bingo[0]==1):
                self.bingo_25_state[dia[dia_bingo[1]][j]] = 'none'
                self.bingo_25[dia[dia_bingo[1]][j]].setPixmap(QPixmap(''))

        self.score_num += 100*bingo_count
        score_text = '{}'.format(self.score_num)
        self.score.setText(score_text)
        self.score.repaint()
        self.bingo_num += bingo_count
        bingo_text = '{}'.format(self.bingo_num)
        self.bingo.setText(bingo_text)
        self.bingo.repaint()

        if (self.shark_num<3 and bingo_count>0):
            self.shark_num+=1
            shark_text = '{}'.format(self.shark_num)
            self.shark.setText(shark_text)
            self.shark.repaint()
        if (self.tentacle_num < 3 and bingo_count>1):
            self.tentacle_num += 1
            tentacle_text = '{}'.format(self.tentacle_num)
            self.tentacle.setText(tentacle_text)
            self.tentacle.repaint()

    def setEvent(self):
        clickable(self.shark_la).connect(self.sharkClick)
        clickable(self.tentacle_la).connect(self.tentacleClick)

        clickable(self.bingo_5_1).connect(
            lambda label = self.bingo_5_1, index = 0 : self.bingo5Click(label=self.bingo_5_1, index = 0))
        clickable(self.bingo_5_2).connect(
            lambda label = self.bingo_5_2, index = 1: self.bingo5Click(label=self.bingo_5_2, index = 1))
        clickable(self.bingo_5_3).connect(
            lambda label = self.bingo_5_3, index = 2: self.bingo5Click(label=self.bingo_5_3, index = 2))
        clickable(self.bingo_5_4).connect(
            lambda label = self.bingo_5_4, index = 3: self.bingo5Click(label=self.bingo_5_4, index = 3))
        clickable(self.bingo_5_5).connect(
            lambda label = self.bingo_5_5, index = 4: self.bingo5Click(label=self.bingo_5_5, index = 4))

        clickable(self.bingo_25_1).connect(
            lambda label=self.bingo_25_1, index=0: self.bingo25Click(label=self.bingo_25_1, index=0))
        clickable(self.bingo_25_2).connect(
            lambda label=self.bingo_25_2, index=1: self.bingo25Click(label=self.bingo_25_2, index=1))
        clickable(self.bingo_25_3).connect(
            lambda label=self.bingo_25_3, index=2: self.bingo25Click(label=self.bingo_25_3, index=2))
        clickable(self.bingo_25_4).connect(
            lambda label=self.bingo_25_4, index=3: self.bingo25Click(label=self.bingo_25_4, index=3))
        clickable(self.bingo_25_5).connect(
            lambda label=self.bingo_25_5, index=4: self.bingo25Click(label=self.bingo_25_5, index=4))
        clickable(self.bingo_25_6).connect(
            lambda label=self.bingo_25_6, index=5: self.bingo25Click(label=self.bingo_25_6, index=5))
        clickable(self.bingo_25_7).connect(
            lambda label=self.bingo_25_7, index=6: self.bingo25Click(label=self.bingo_25_7, index=6))
        clickable(self.bingo_25_8).connect(
            lambda label=self.bingo_25_8, index=7: self.bingo25Click(label=self.bingo_25_8, index=7))
        clickable(self.bingo_25_9).connect(
            lambda label=self.bingo_25_9, index=8: self.bingo25Click(label=self.bingo_25_9, index=8))
        clickable(self.bingo_25_10).connect(
            lambda label=self.bingo_25_10, index=9: self.bingo25Click(label=self.bingo_25_10, index=9))
        clickable(self.bingo_25_11).connect(
            lambda label=self.bingo_25_11, index=10: self.bingo25Click(label=self.bingo_25_11, index=10))
        clickable(self.bingo_25_12).connect(
            lambda label=self.bingo_25_12, index=11: self.bingo25Click(label=self.bingo_25_12, index=11))
        clickable(self.bingo_25_13).connect(
            lambda label=self.bingo_25_13, index=12: self.bingo25Click(label=self.bingo_25_13, index=12))
        clickable(self.bingo_25_14).connect(
            lambda label=self.bingo_25_14, index=13: self.bingo25Click(label=self.bingo_25_14, index=13))
        clickable(self.bingo_25_15).connect(
            lambda label=self.bingo_25_15, index=14: self.bingo25Click(label=self.bingo_25_15, index=14))
        clickable(self.bingo_25_16).connect(
            lambda label=self.bingo_25_16, index=15: self.bingo25Click(label=self.bingo_25_16, index=15))
        clickable(self.bingo_25_17).connect(
            lambda label=self.bingo_25_17, index=16: self.bingo25Click(label=self.bingo_25_17, index=16))
        clickable(self.bingo_25_18).connect(
            lambda label=self.bingo_25_18, index=17: self.bingo25Click(label=self.bingo_25_18, index=17))
        clickable(self.bingo_25_19).connect(
            lambda label=self.bingo_25_19, index=18: self.bingo25Click(label=self.bingo_25_19, index=18))
        clickable(self.bingo_25_20).connect(
            lambda label=self.bingo_25_20, index=19: self.bingo25Click(label=self.bingo_25_20, index=19))
        clickable(self.bingo_25_21).connect(
            lambda label=self.bingo_25_21, index=20: self.bingo25Click(label=self.bingo_25_21, index=20))
        clickable(self.bingo_25_22).connect(
            lambda label=self.bingo_25_22, index=21: self.bingo25Click(label=self.bingo_25_22, index=21))
        clickable(self.bingo_25_23).connect(
            lambda label=self.bingo_25_23, index=22: self.bingo25Click(label=self.bingo_25_23, index=22))
        clickable(self.bingo_25_24).connect(
            lambda label=self.bingo_25_24, index=23: self.bingo25Click(label=self.bingo_25_24, index=23))
        clickable(self.bingo_25_25).connect(
            lambda label=self.bingo_25_25, index=24: self.bingo25Click(label=self.bingo_25_25, index=24))

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



app = QtWidgets.QApplication([])
MainFrame = game()
MainFrame.show()
app.exec_()