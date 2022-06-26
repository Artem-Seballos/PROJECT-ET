from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MyAccountWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(397, 600)
        MainWindow.setStyleSheet("background-color: #0B0912\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background: transparent;\n"
"    color: #9400D3;}\n"
"")
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 95, 100))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayoutWidget.hide()
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    background: transparent;\n"
"    color: #9400D3;}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    background: transparent;\n"
"    color: #9400D3;}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background: transparent;\n"
"    color: #9400D3;}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 10, 151, 41))
        font = QtGui.QFont()
        font.setFamily("courier")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("QLabel{\n"
"    color:#8B008B;\n"
"    background: transparent;\n"
"    font-family: courier;\n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 121, 41))
        font = QtGui.QFont()
        font.setFamily("courier")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"    color:#8B008B;\n"
"    background: transparent;\n"
"    font-family: courier;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 60, 121, 41))
        font = QtGui.QFont()
        font.setFamily("courier")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"    color:#8B008B;\n"
"    background: transparent;\n"
"    font-family: courier;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 50, 101, 121))
        self.label_4.setStyleSheet("QLabel{background: #031319;}")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(150, 110, 121, 41))
        font = QtGui.QFont()
        font.setFamily("courier")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel{\n"
"    color:#8B008B;\n"
"    background: transparent;\n"
"    font-family: courier;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 170, 241, 41))
        font = QtGui.QFont()
        font.setFamily("courier")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel{\n"
"    color:#8B008B;\n"
"    background: transparent;\n"
"    font-family: courier;\n"
"}")
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RaccoonTail"))
        self.pushButton.setText(_translate("MainWindow", "≡"))
        self.pushButton_4.setText(_translate("MainWindow", "My Account"))
        self.pushButton_3.setText(_translate("MainWindow", "Bulletin Board"))
        self.pushButton_2.setText(_translate("MainWindow", "News"))
        self.label.setText(_translate("MainWindow", "My Account"))
        self.label_2.setText(_translate("MainWindow", "FirstName"))
        self.label_3.setText(_translate("MainWindow", "LastName"))
        self.label_5.setText(_translate("MainWindow", "Age"))
        self.label_6.setText(_translate("MainWindow", "Buyer or seller"))


if __name__ == "__main__":
    import sys
    import ctypes

    myappid = 'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    App = QtWidgets.QApplication([])
    App.setWindowIcon(QtGui.QIcon('iconET.png'))
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MyAccountWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
