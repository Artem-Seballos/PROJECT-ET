import sys
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import  Qt
from PyQt5 import  QtGui
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWinExtras import QtWin
import main
import regonl
import ctypes
import news
import myaccount
import bb
import createaprof

db = sqlite3.connect('datelog.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users(
    login TEXT,
    password TEXT,
    firstname TEXT,
    lastname TEXT,
    age INTEGER,
    status TEXT
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

        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

    def reg(self):
        self.reg = RegW()
        self.reg.show()
        self.hide()


    def login(self):

        def acc(self):
            self.acc = Myaccount()
            self.acc.show()
            self.hide()
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
        if check_pass[0][0] == user_password and check_login[0][0] == user_login and self.radioButton.isChecked():
            acc(self)
        else:
            self.label.setText('Authorisation Error')

class RegW(QtWidgets.QMainWindow, regonl.Ui_RegWindow):
    def __init__(self):
        super(RegW, self).__init__()
        self.setupUi(self)

        self.pushButton.pressed.connect(self.regnow)
        self.pushButton_2.pressed.connect(self.log)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

    def regnow(self):

        def prof(self):
            self.prof = CrProf()
            self.prof.show()
            self.hide()

        user_login = self.lineEdit.text()
        user_password = self.lineEdit_2.text()

        if len(user_login) == 0:
            return
        if len(user_password) == 0:
            return

        cursor.execute(f'SELECT login FROM users WHERE login="{user_login}"')
        if cursor.fetchone() is None:
            cursor.execute(f'INSERT INTO users (login, password) VALUES(?, ?)', (user_login, user_password))
            self.label.setText(f'account {user_login} successfully registered!')
            db.commit()
            prof(self)
        else:
            self.label.setText('this account already exists')
    def log(self):
        self.log = LoginW()
        self.log.show()
        self.hide()

class News(QtWidgets.QMainWindow,news.Ui_NewsWindow):
    def __init__(self):
        super(News, self).__init__()
        self.setupUi(self)

class Myaccount(QtWidgets.QMainWindow, myaccount.Ui_MyAccountWindow):
    def __init__(self):
        super(Myaccount, self).__init__()
        self.setupUi(self)
        self.pushButton.pressed.connect(self.push)


class Bb(QtWidgets.QMainWindow, bb.Ui_BbWindow):
    def __init__(self):
        super(Bb, self).__init__()
        self.setupUi(self)

class CrProf(QtWidgets.QMainWindow, createaprof.Ui_ProfWindow):
    def __init__(self):
        super(CrProf, self).__init__()
        self.setupUi(self)
        self.pushButton.pressed.connect(self.createP)

    def createP(self):

        def acc(self):
            self.acc = Myaccount()
            self.acc.show()
            self.hide()

        user_firstname = self.lineEdit.text()
        user_lastname = self.lineEdit_2.text()
        user_age = self.lineEdit_3.text()
        #user_status = self.comboBox.currentText()

        if len(user_firstname) == 0:
            return
        if len(user_lastname) == 0:
            return
        if len(user_age) == 0:
            return

        cursor.execute(f'SELECT firstname FROM users WHERE firstname = "{user_firstname}"')
        cursor.execute(f'INSERT INTO users(firstname, lastname, age) VALUES(?, ?, ?)', (user_firstname, user_lastname,
                                                                                        user_age,))
        db.commit()
        acc(self)






myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

App = QtWidgets.QApplication([])
App.setWindowIcon(QtGui.QIcon('iconET.png'))
window = LoginW()
window.show()
App.exec()