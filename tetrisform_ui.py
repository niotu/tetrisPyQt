# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tetrisform.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TetrisForm(object):
    def setupUi(self, TetrisForm):
        TetrisForm.setObjectName("TetrisForm")
        TetrisForm.resize(332, 401)
        self.verticalLayout = QtWidgets.QVBoxLayout(TetrisForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.l2 = Pic(TetrisForm)
        self.l2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.l2.setText("")
        self.l2.setPixmap(QtGui.QPixmap("nth.png"))
        self.l2.setScaledContents(True)
        self.l2.setObjectName("l2")
        self.gridLayout.addWidget(self.l2, 0, 1, 1, 1)
        self.l6 = Pic(TetrisForm)
        self.l6.setText("")
        self.l6.setPixmap(QtGui.QPixmap("nth.png"))
        self.l6.setScaledContents(True)
        self.l6.setObjectName("l6")
        self.gridLayout.addWidget(self.l6, 2, 2, 1, 1)
        self.l4 = Pic(TetrisForm)
        self.l4.setText("")
        self.l4.setPixmap(QtGui.QPixmap("nth.png"))
        self.l4.setScaledContents(True)
        self.l4.setObjectName("l4")
        self.gridLayout.addWidget(self.l4, 2, 0, 1, 1)
        self.l7 = Pic(TetrisForm)
        self.l7.setText("")
        self.l7.setPixmap(QtGui.QPixmap("nth.png"))
        self.l7.setScaledContents(True)
        self.l7.setObjectName("l7")
        self.gridLayout.addWidget(self.l7, 8, 0, 1, 1)
        self.l3 = Pic(TetrisForm)
        self.l3.setText("")
        self.l3.setPixmap(QtGui.QPixmap("nth.png"))
        self.l3.setScaledContents(True)
        self.l3.setObjectName("l3")
        self.gridLayout.addWidget(self.l3, 0, 2, 1, 1)
        self.l9 = Pic(TetrisForm)
        self.l9.setText("")
        self.l9.setPixmap(QtGui.QPixmap("nth.png"))
        self.l9.setScaledContents(True)
        self.l9.setObjectName("l9")
        self.gridLayout.addWidget(self.l9, 8, 2, 1, 1)
        self.l5 = Pic(TetrisForm)
        self.l5.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.l5.setText("")
        self.l5.setPixmap(QtGui.QPixmap("nth.png"))
        self.l5.setScaledContents(True)
        self.l5.setObjectName("l5")
        self.gridLayout.addWidget(self.l5, 2, 1, 1, 1)
        self.l8 = Pic(TetrisForm)
        self.l8.setText("")
        self.l8.setPixmap(QtGui.QPixmap("nth.png"))
        self.l8.setScaledContents(True)
        self.l8.setObjectName("l8")
        self.gridLayout.addWidget(self.l8, 8, 1, 1, 1)
        self.l1 = Pic(TetrisForm)
        self.l1.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.l1.setText("")
        self.l1.setPixmap(QtGui.QPixmap("nth.png"))
        self.l1.setScaledContents(True)
        self.l1.setObjectName("l1")
        self.gridLayout.addWidget(self.l1, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.newGame = QtWidgets.QPushButton(TetrisForm)
        self.newGame.setObjectName("newGame")
        self.horizontalLayout.addWidget(self.newGame)
        self.soloGame = QtWidgets.QPushButton(TetrisForm)
        self.soloGame.setObjectName("soloGame")
        self.horizontalLayout.addWidget(self.soloGame)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.playerSign = QtWidgets.QLabel(TetrisForm)
        self.playerSign.setObjectName("playerSign")
        self.verticalLayout.addWidget(self.playerSign)
        self.msg = QtWidgets.QLabel(TetrisForm)
        self.msg.setText("")
        self.msg.setObjectName("msg")
        self.verticalLayout.addWidget(self.msg)

        self.retranslateUi(TetrisForm)
        QtCore.QMetaObject.connectSlotsByName(TetrisForm)

    def retranslateUi(self, TetrisForm):
        _translate = QtCore.QCoreApplication.translate
        TetrisForm.setWindowTitle(_translate("TetrisForm", "Form"))
        self.newGame.setText(_translate("TetrisForm", "?????????? ????????"))
        self.soloGame.setText(_translate("TetrisForm", "?????????? ???????? ?? ??????????????????????"))
        self.playerSign.setText(_translate("TetrisForm", "TextLabel"))
from pic import Pic
