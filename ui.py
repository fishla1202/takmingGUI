# -*- coding: utf-8 -*-
from PyQt5 import QtCore, uic, QtWidgets
from getTakmingPage import auto_click_takming_page
from login import Ui_Form
import sys

class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.button_click)

    def button_click(self):
        account = self.ui.account.text()
        passwd = self.ui.passwd.text()
        local = self.ui.localOfDriver.text()
        auto_click_takming_page(account, passwd, local)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())