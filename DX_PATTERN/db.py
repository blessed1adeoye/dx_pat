from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3


# from b import Ui_MainWindow

import sys


class Ui_Form(object):

    def DTB(self):
        con = sqlite3.connect('blessed.db')
        bhuwah = (''' Drop pattern ''')
        con.execute(bhuwah)
        con.commit()


    # def ade(self):
    #     self.Ui_MainWindow = QtWidgets.QWidget()
    #     self.ui = Ui_MainWindow()
    #     self.ui.setupUi(self.MainWindow)
    #     self.MainWindow.show()




    def me(self):
        app = QtWidgets.QApplication(sys.argv)
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.DTB()
        self.Form.close()
        # self.ade()


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(912, 592)
        Form.setFixedSize(912, 592)
        Form.setWindowIcon(QtGui.QIcon("him.jpg"))
        self.home = QtWidgets.QLabel(Form)
        self.home.setGeometry(QtCore.QRect(10, 0, 931, 581))
        self.home.setText("")
        self.home.setPixmap(QtGui.QPixmap("2.jpg"))
        self.home.setObjectName("home")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 30, 141, 151))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("78.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(220, 360, 411, 191))
        self.label_2.setObjectName("label_2")
        self.r_btn = QtWidgets.QPushButton(Form)
        self.r_btn.setGeometry(QtCore.QRect(300, 500, 251, 41))
        self.r_btn.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 255);\n"
"background-color: rgb(194, 200, 193);")
        self.r_btn.setObjectName("r_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        #################################################################################
        self.r_btn.clicked.connect(self.me)
        #################################################################################
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ONLY HEALTH INFORMATION MANAGEMENT PROFESSIONAL IS ALLOWED HERE "))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">THANK YOU  </span></p></body></html>"))
        self.r_btn.setText(_translate("Form", "CLICK ME"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
