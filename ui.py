# -*- coding: utf-8 -*-
from PyQt5 import QtCore, uic, QtWidgets
from getTakmingPage import auto_click_takming_page
import sys

UIClass, QtBaseClass = uic.loadUiType("login.ui")


class MyApp(UIClass, QtBaseClass):
    def __init__(self):
        UIClass.__init__(self)
        QtBaseClass.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_click)

    def button_click(self):
        account = self.account.text()
        passwd = self.passwd.text()
        local = self.localOfDriver.text()
        auto_click_takming_page(account, passwd, local)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())