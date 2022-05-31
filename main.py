from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)
        MainWindow.setStyleSheet("background-color: #0B0912;\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 50, 281, 91))
        self.label.setStyleSheet("background-color:#02000C;\n"
"color: white;\n"
"border: 2px sold #19170B;\n"
"border-radius: 12;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 480, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: #02000C;\n"
"    color: white;\n"
"     border: 2px;\n"
"    border-radius: 9\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #605118;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(70, 450, 131, 20))
        self.radioButton.setStyleSheet("QRadioButton{\n"
"    color: white\n"
"}\n"
"QRadioButton:hover{\n"
"    color: #605118;\n"
"}")
        self.radioButton.setObjectName("radioButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 300, 271, 22))
        self.lineEdit.setStyleSheet("background-color: #09051F;\n"
"color: white;\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 370, 271, 22))
        self.lineEdit_2.setStyleSheet("background-color: #09051F;\n"
"color: white;\n"
"")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 450, 81, 21))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color: transparent;\n"
"    color: white;\n"
"     border: 2px;\n"
"    border-radius: 9\n"
"}\n"
"QPushButton:hover{\n"
"    color: #605118;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RaccoonTail"))
        self.label.setText(_translate("MainWindow", "Glad to welcome you! Sign up if you\'re here for the first time or login to your account"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.radioButton.setText(_translate("MainWindow", "I accept the terms"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "login..."))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "password..."))
        self.pushButton_2.setText(_translate("MainWindow", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
