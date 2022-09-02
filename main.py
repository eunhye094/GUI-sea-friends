from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic,QtGui
from PyQt5.QtGui import QPixmap

import random

form_class1 = uic.loadUiType("ui_files/main.ui")[0]
form_class2 = uic.loadUiType("ui_files/rule.ui")[0]
form_class3 = uic.loadUiType("ui_files/game.ui")[0]
form_class4 = uic.loadUiType("ui_files/rank.ui")[0]
form_class5 = uic.loadUiType("ui_files/over.ui")[0]

class main(QtWidgets.QMainWindow,form_class1):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)

        self.setWindowTitle("main")
        self.setFixedSize(1200,700)

        clickable(self.start).connect(self.gameClick)
        clickable(self.rule).connect(self.ruleClick)
        clickable(self.rank).connect(self.rankClick)

    def gameClick(self):
        self.MainFrame3 = game()
        self.MainFrame3.show()

    def ruleClick(self):
        self.MainFrame2=rule()
        self.MainFrame2.show()

    def rankClick(self):
        self.MainFrame4 = rank()
        self.MainFrame4.show()

class rule(QtWidgets.QMainWindow,form_class2):
    def __init__(self):
        super(rule, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("rule")
        self.setFixedSize(650,800)
        clickable(self.start).connect(self.gameClick)

    def gameClick(self):
        self.MainFrame3_2 = game()
        self.MainFrame3_2.show()
        self.close()

class game(QtWidgets.QMainWindow,form_class3):
    def __init__(self):
        super(game, self).__init__()
        self.setupUi(self)

        self.setWindowTitle("game")
        self.setFixedSize(1200,700)

        self.bingo_25_state = []  # 빙고판
        for i in range(25):
            self.bingo_25_state.append('none')
        self.bingo_5_state = []  # 빙고후보

        self.bingo_5 = []  # 빙고판 라벨
        self.bingo_25 = []  # 빙고후보 라벨

        self.image = ['./images/starfish_black.png', './images/dolphin_white.png', './images/clownfish_white.png', './images/bluefish_white.png', './images/yellowtang_white.png', './images/seahorse_white.png', './images/turtle_white.png', './images/whale_white.png', './images/shrimp_white.png']
        self.image2 = ['./images/starfish_gray.png', './images/dolphin_gray.png', './images/clownfish_gray.png', './images/bluefish_gray.png', './images/yellowtang_gray.png', './images/seahorse_gray.png', './images/turtle_gray.png', './images/whale_gray.png', './images/shrimp_gray.png']
        self.image3 = ['./images/starfish_pink.png', './images/dolphin_pink.png', './images/clownfish_pink.png', './images/bluefish_pink.png', './images/yellowtang_pink.png', './images/seahorse_pink.png', './images/turtle_pink.png', './images/whale_pink.png', './images/shrimp_pink.png']
        for i in range(5):
            self.bingo_5_state.append(random.choices(self.image, weights=[1,3,3,3,3,3,3,3,3])[0])

        self.select = 'none'

        self.score_num = 0
        self.bingo_num = 0
        self.shark_num = 0
        self.tentacle_num = 0

        self.count = 0
        self.tentacle_count = 0
        self.tentacle_label = ''
        self.tentacle_index = -1

        self.select_label = ''

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
            self.shark_la.setPixmap(QPixmap('./images/shark_02.png'))
            self.shark_la.repaint()

    def tentacleClick(self):
        if (self.select == 'none' and self.tentacle_num > 0):
            self.select = 'tentacle'
            self.tentacle_la.setPixmap(QPixmap('./images/tentacles_02.png'))
            self.tentacle_la.repaint()

    def bingo5Click(self, label, index):
        if (self.select == 'none' and self.bingo_5_state[index]!='none'):
            self.select = self.bingo_5_state[index]
            label.setPixmap(QPixmap(self.image2[self.image.index(self.bingo_5_state[index])]))
            self.bingo_5_state[index] = 'none'
            self.select_label = label

    def bingo5Set(self):
        self.count = 0
        self.bingo_5_state=[]

        for i in range(5):
            self.bingo_5_state.append(random.choices(self.image, weights=[1,3,3,3,3,3,3,3,3])[0])
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
                self.shark_la.setPixmap(QPixmap('./images/shark_01.png'))
                self.shark_la.repaint()
            elif (self.select=='tentacle'):
                if (self.tentacle_count==0):
                    self.tentacle_label = label
                    self.tentacle_index = index
                    self.tentacle_count += 1
                    label.setPixmap(QPixmap(self.image3[self.image.index(self.bingo_25_state[index])]))
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
                    self.tentacle_la.setPixmap(QPixmap('./images/tentacles_01.png'))
                    self.tentacle_la.repaint()
                    self.tentacle_label = ''
                    self.tentacle_index = -1
                    self.tentacle_count = 0
        elif (self.select != 'none' and self.select != 'shark' and self.select != 'tentacle'):
            self.select_label.setPixmap(QPixmap(''))
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
            self.MainFrame5 = over(self.score_num, self)
            self.MainFrame5.show()

    def bingo25Check(self, index):
        bingo_count = 0

        row_bingo = [0, 0]; col_bingo = [0,0]; dia_bingo1=[0,0]; dia_bingo2=[0,0]
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
                    if (i==0):
                        dia_bingo1 = [1, i]
                    elif (i==1):
                        dia_bingo2 = [1, i]
                    bingo_count += 1

        for j in range(5):
            if (row_bingo[0] == 1):
                self.bingo_25_state[row[row_bingo[1]][j]] = 'none'
                self.bingo_25[row[row_bingo[1]][j]].setPixmap(QPixmap(''))
            if (col_bingo[0]==1):
                self.bingo_25_state[col[col_bingo[1]][j]] = 'none'
                self.bingo_25[col[col_bingo[1]][j]].setPixmap(QPixmap(''))
            if (dia_bingo1[0] == 1):
                self.bingo_25_state[dia[dia_bingo1[1]][j]] = 'none'
                self.bingo_25[dia[dia_bingo1[1]][j]].setPixmap(QPixmap(''))
            if (dia_bingo2[0] == 1):
                self.bingo_25_state[dia[dia_bingo2[1]][j]] = 'none'
                self.bingo_25[dia[dia_bingo2[1]][j]].setPixmap(QPixmap(''))

        if (bingo_count==1):
            self.score_num += 100
        elif (bingo_count==2):
            self.score_num += 300
        elif (bingo_count==3):
            self.score_num += 900
        elif (bingo_count==4):
            self.score_num += 1200

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

class rank(QtWidgets.QMainWindow,form_class4):
    def __init__(self):
        super(rank, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("rank")
        self.setFixedSize(650,800)

        name = [self.name1, self.name2, self.name3, self.name4, self.name5]
        score = [self.score1, self.score2, self.score3, self.score4, self.score5]

        f = open('./rank.txt', 'r', encoding='utf-8')
        lines = f.readlines()
        num = 0
        for line in lines:
            temp = line.split(',')
            name[num].setText(temp[0])
            temp2 = temp[1][:-1]+'점'
            score[num].setText(temp2)
            name[num].repaint()
            score[num].repaint()
            num+=1
        f.close()

class over(QtWidgets.QMainWindow,form_class5):
    def __init__(self, score, parent):
        super(over, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("over")
        self.setFixedSize(800,560)
        clickable(self.yes).connect(lambda score2 = score, parent2 = parent : self.yesClick(score2=score, parent2=parent))

    def yesClick(self, score2, parent2):
        parent2.close()
        self.close()

        f = open('./rank.txt', 'r', encoding='utf-8')
        lines = f.readlines()
        info_list = []
        score_list = []
        for line in lines:
            temp = line.split(',')
            info_list.append(temp)
            score_list.append(int(temp[1][:-1]))
        f.close()

        for i in range(1, 5):
            if (score_list[i - 1] >= score2 and score_list[i] < score2):
                info_list.insert(i, [self.input.text(), (str(score2)+"\n")])
                info_list.pop(5)

        f = open('./rank.txt', 'w', encoding='utf-8')
        for i in range(5):
            f.write(info_list[i][0] + "," + info_list[i][1])
        f.close()

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
MainFrame = main()
MainFrame.show()
app.exec_()