from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QMessageBox
from tetrisform_ui import Ui_TetrisForm
import random
import time


class TetrisForm(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_TetrisForm()
        self.ui.setupUi(self)
        self.mas = []
        self.gameMode = 0
        self.ui.newGame.clicked.connect(lambda: self.newPlay())
        self.ui.soloGame.clicked.connect(lambda: self.soloPlay())
        self.c = 0
        self.ui.l1.click.connect(lambda: self.onClick(self.ui.l1, 0, 0))
        self.ui.l2.click.connect(lambda: self.onClick(self.ui.l2, 1, 0))
        self.ui.l3.click.connect(lambda: self.onClick(self.ui.l3, 2, 0))
        self.ui.l4.click.connect(lambda: self.onClick(self.ui.l4, 0, 1))
        self.ui.l5.click.connect(lambda: self.onClick(self.ui.l5, 1, 1))
        self.ui.l6.click.connect(lambda: self.onClick(self.ui.l6, 2, 1))
        self.ui.l7.click.connect(lambda: self.onClick(self.ui.l7, 0, 2))
        self.ui.l8.click.connect(lambda: self.onClick(self.ui.l8, 1, 2))
        self.ui.l9.click.connect(lambda: self.onClick(self.ui.l9, 2, 2))
        self.ui.l1.setStyleSheet('font: 16pt "MS Shell Dlg 2";')
        self.ui.l2.setStyleSheet('font: 16pt "MS Shell Dlg 2";')
        self.ui.l3.setStyleSheet('font: 16pt "MS Shell Dlg 2";')
        self.ui.l4.setStyleSheet('font: 16pt "MS Shell Dlg 2";')
        self.ui.l5.setStyleSheet('font: 16pt "MS Shell Dlg 2";')
        self.ui.l6.setStyleSheet('font: 16pt "MS Shell Dlg 2";')
        self.ui.l7.setStyleSheet('font: 16pt "MS Shell Dlg 2";')
        self.ui.l8.setStyleSheet('font: 16pt "MS Shell Dlg 2";')
        self.ui.l9.setStyleSheet('font: 16pt "MS Shell Dlg 2";')
        self.ui.playerSign.setStyleSheet('font: 16pt "MS Shell Dlg 2";')
        self.ui.playerSign.setText("ходит: 0")
        self.knstate = [["", "", ""],
                        ["", "", ""],
                        ["", "", ""]]

    def widget(self, x, y):
        s = {(0, 0): self.ui.l1,
             (0, 1): self.ui.l2,
             (0, 2): self.ui.l3,
             (1, 0): self.ui.l4,
             (1, 1): self.ui.l5,
             (1, 2): self.ui.l6,
             (2, 0): self.ui.l7,
             (2, 1): self.ui.l8,
             (2, 2): self.ui.l9}
        kords = (x, y)
        return s[kords]

    def makePole(self):
        self.c = 0
        self.knstate = [["", "", ""],
                        ["", "", ""],
                        ["", "", ""]]

        self.ui.playerSign.setText("ходит: 0")
        self.ui.l1.setPixmap(QPixmap("nth.png"))
        self.ui.l1.setScaledContents(True)
        self.ui.l2.setPixmap(QPixmap("nth.png"))
        self.ui.l2.setScaledContents(True)
        self.ui.l3.setPixmap(QPixmap("nth.png"))
        self.ui.l3.setScaledContents(True)
        self.ui.l4.setPixmap(QPixmap("nth.png"))
        self.ui.l4.setScaledContents(True)
        self.ui.l5.setPixmap(QPixmap("nth.png"))
        self.ui.l5.setScaledContents(True)
        self.ui.l6.setPixmap(QPixmap("nth.png"))
        self.ui.l6.setScaledContents(True)
        self.ui.l7.setPixmap(QPixmap("nth.png"))
        self.ui.l7.setScaledContents(True)
        self.ui.l8.setPixmap(QPixmap("nth.png"))
        self.ui.l8.setScaledContents(True)
        self.ui.l9.setPixmap(QPixmap("nth.png"))
        self.ui.l9.setScaledContents(True)

    def onClick(self, wl, x, y):
        if self.knstate[y][x] != "":
            return
        self.c += 1
        if self.c % 2 == 0:
            self.knstate[y][x] = "X"
            self.ui.playerSign.setText("ходит: 0")
            wl.setPixmap(QPixmap("krest.png"))
            wl.setScaledContents(True)
        else:
            self.knstate[y][x] = "0"
            self.ui.playerSign.setText("ходит: X")
            wl.setPixmap(QPixmap("null.png"))
            wl.setScaledContents(True)
        self.winline()
        if self.gameMode == 0:
            self.computerMove()

# -нет, я не брал еду. в столовой еды тоже хватает.

# -а мне это нужно? у меня все есть.

# -я уже ничего не ищу.


    def computerMove(self):
        while True:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if self.knstate[x][y] == "":
                break
        wl = self.widget(x, y)
        self.c += 1
        self.knstate[x][y] = "X"
        self.ui.playerSign.setText("ходит: 0")
        wl.setPixmap(QPixmap("krest.png"))
        wl.setScaledContents(True)
        self.winline()

    def soloPlay(self):
        self.makePole()
        self.gameMode = 0

    def newPlay(self):
        self.makePole()
        self.gameMode = 1

    def winline(self):
        ll = [[self.knstate[0][0], self.knstate[0][1], self.knstate[0][2]],
              [self.knstate[1][0], self.knstate[1][1], self.knstate[1][2]],
              [self.knstate[2][0], self.knstate[2][1], self.knstate[2][2]],
              [self.knstate[0][0], self.knstate[1][0], self.knstate[2][0]],
              [self.knstate[0][1], self.knstate[1][1], self.knstate[2][1]],
              [self.knstate[0][2], self.knstate[1][2], self.knstate[2][2]],
              [self.knstate[2][0], self.knstate[1][1], self.knstate[0][2]],
              [self.knstate[0][0], self.knstate[1][1], self.knstate[2][2]],
              ]
        for i in ll:
            if i[0] == i[1] == i[2] == "X":
                QMessageBox.information(self, "x", "победил x")
                self.newPlay()
            elif i[0] == i[1] == i[2] == "0":
                QMessageBox.information(self, "0", "победил 0")
                self.newPlay()
