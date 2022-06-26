from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProfWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(397, 600)
        MainWindow.setStyleSheet("background-color: #0B0912\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 100, 181, 31))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    background-color: #344FA1;\n"
"    border-radius: 15px;\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 150, 181, 31))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    background-color: #344FA1;\n"
"    border-radius: 15px;\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 200, 101, 31))
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    background-color: #344FA1;\n"
"    border-radius: 15px;\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}\n"
"")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 300, 171, 31))
        self.comboBox.setStyleSheet("QComboBox {\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    background-color: #344FA1;\n"
"    border-radius: 15px;\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 370, 111, 151))
        self.label.setStyleSheet("background: #218457")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"    color: #9400D3;}")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 450, 93, 28))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    font: 10pt;\n"
"    background-color: #344FA1;\n"
"    border-radius: 10px;\n"
"    border: 2px solid;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RaccoonTail"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "FirstName"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "LastName"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Age"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Buyer"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Seller"))
        self.label.setText(_translate("MainWindow", "     Your Photo"))
        self.label_2.setText(_translate("MainWindow", "           Create A Profile"))
        self.pushButton.setText(_translate("MainWindow", "CREATE"))


if __name__ == "__main__":
    import sys
    import ctypes

    myappid = 'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    App = QtWidgets.QApplication([])
    App.setWindowIcon(QtGui.QIcon('iconET.png'))
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ProfWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
