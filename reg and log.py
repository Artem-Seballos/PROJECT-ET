import sys
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.QtCore import  Qt
from PyQt5 import  QtGui
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWinExtras import QtWin
import main
import regonl
import ctypes

db = sqlite3.connect('datelog.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users(
    login TEXT,
    password TEXT
)''')
db.commit()

#чек аккаунтов

for i in cursor.execute('SELECT * FROM users'):
    print(i)

class LoginW(QtWidgets.QMainWindow, main.Ui_MainWindow):
    def __init__(self):
        super(LoginW, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('iconET.png'))

        self.pushButton.pressed.connect(self.login)
        self.pushButton_2.pressed.connect(self.reg)

    def reg(self):
        self.reg = RegW()
        self.reg.show()
        self.hide()

    def login(self):
        user_login = self.lineEdit.text()
        user_password = self.lineEdit_2.text()
        if len(user_login) == 0:
            return
        if len(user_password) == 0:
            return
        cursor.execute(f'SELECT password FROM users WHERE password="{user_password}"')
        check_pass = cursor.fetchall()
        cursor.execute(f'SELECT login FROM users WHERE login="{user_login}"')
        check_login = cursor.fetchall()
        if check_pass[0][0] == user_password and check_login[0][0] == user_login:
            self.label.setText('successful authorization')
        else:
            self.label.setText('Authorisation Error')

class RegW(QtWidgets.QMainWindow, regonl.Ui_RegWindow):
    def __init__(self):
        super(RegW, self).__init__()
        self.setupUi(self)

        self.pushButton.pressed.connect(self.regnow)
        self.pushButton_2.pressed.connect(self.log)

    def regnow(self):
        user_login = self.lineEdit.text()
        user_password = self.lineEdit_2.text()
        if len(user_login) == 0:
            return
        if len(user_password) == 0:
            return

        cursor.execute(f'SELECT login FROM users WHERE login="{user_login}"')
        if cursor.fetchone() is None:
            cursor.execute(f'INSERT INTO users VALUES("{user_login}", "{user_password}")')
            self.label.setText(f'account {user_login} successfully registered!')
            db.commit()
        else:
            self.label.setText('this account already exists')
    def log(self):
        self.log = LoginW()
        self.log.show()
        self.hide()

myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

App = QtWidgets.QApplication([])
App.setWindowIcon(QtGui.QIcon('iconET.png'))
window = LoginW()
window.show()
App.exec()