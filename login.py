# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 50, 41, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(90, 100, 60, 16))
        self.label_2.setObjectName("label_2")
        self.account = QtWidgets.QLineEdit(Form)
        self.account.setGeometry(QtCore.QRect(150, 50, 181, 21))
        self.account.setObjectName("account")
        self.passwd = QtWidgets.QLineEdit(Form)
        self.passwd.setGeometry(QtCore.QRect(150, 100, 181, 21))
        self.passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwd.setObjectName("passwd")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 170, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 131, 31))
        self.label_3.setObjectName("label_3")
        self.localOfDriver = QtWidgets.QLineEdit(Form)
        self.localOfDriver.setGeometry(QtCore.QRect(150, 140, 181, 21))
        self.localOfDriver.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.localOfDriver.setObjectName("localOfDriver")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "帳號："))
        self.label_2.setText(_translate("Form", "密碼"))
        self.pushButton.setText(_translate("Form", "登入"))
        self.label_3.setText(_translate("Form", "網頁模擬器檔案位置"))


