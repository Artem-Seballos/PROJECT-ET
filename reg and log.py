import sys
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.QtCore import  Qt
import main
import regonl

db = sqlite3.connect('datelog.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users(
    login TEXT,
    password TEXT
)''')
db.commit()

class Registration(QtWidgets.QMainWindow, regonl.Ui_RegWindow):
    def __init__(self):
        super(Registration, self).__init__()
        self.setupUi(self)

class MainW(QtWidgets.QMainWindow, main.Ui_MainWindow, regonl.Ui_RegWindow):
    def __init__(self):
        super(MainW, self).__init__()
        self.setupUi(self)
    def show_main(self):
        self.m = MainW()
        self.m.pushButton_2.clicked.connect(self.show_reg)
        self.m.pushButton_2.clicked.connect(self.m.close)
    def show_reg(self):
        self.reg = Registration()
        self.reg.show()



App = QtWidgets.QApplication([])
window = MainW()
window.show()
App.exec()