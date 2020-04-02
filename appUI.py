# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dict.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from WordHandle import WordHandler

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLineEdit


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 300)
        MainWindow.setMinimumSize(QtCore.QSize(400, 200))
        MainWindow.setMaximumSize(QtCore.QSize(600, 300))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(150, 100, 311, 75))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 30, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 200, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")

        self.pushButton.clicked.connect(self.showMessageBox)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enter a word and click the button"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.actionNew.setText(_translate("MainWindow", "New"))

    def showMessageBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Window Title")
        msg.setText("You typed:")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)  # TODO: while press "Enter" - exit from message box

        self.word = self.lineEdit.text()
        msg.setInformativeText(self.word)  # TODO: make the bold font

        word_handler = WordHandler(self.word)
        word_handler.update()
        self.lineEdit.clear()

        msg.exec_()  # TODO: what does it mean ?
