from PyQt5 import QtCore, QtGui, QtWidgets

import pandas as pd
import xlsxwriter
from pathlib import Path
import os
import sqlite3
from db import Ui_Form


class Ui_Form_2(object):

    def end(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()

    def clear(self):
        self.db.setText("")

    def update_message(self,title="Test",message="Please select an item to be updated "):
        QtWidgets.QMessageBox.information(None,title,message)

    def exportToExcel(self ):
        db = self.db.text()
        con = sqlite3.connect('blessed.db')
        cursor = con.execute('select rowid, dx, icd, male_less_than_1, female_less_than_1, male_1_14, female_1_14, male_15_44, female_15_44, male_45_64, female_45_64, male_greater_65, female_greater_65, total_male, total_female, g_total from pattern')

        all_data = cursor.fetchall()
        with pd.ExcelWriter(os.path.join(Path.home(), db + ".xlsx"), engine="xlsxwriter", options = {'strings_to_numbers': True, 'strings_to_formulas': False}) as writer:

            try:
                df = pd.read_sql("select rowid, dx, icd, male_less_than_1, female_less_than_1, male_1_14, female_1_14, male_15_44, female_15_44, male_45_64, female_45_64, male_greater_65, female_greater_65, total_male, total_female, g_total from pattern", con)
                df.to_excel(writer, sheet_name = "Sheet1", header = True, index = False)

                self.update_message('Success', 'File  successfully CREATED!! ')
                self.clear()
                self.end()

            except:
                self.update_message('Error', 'There is an error! ')



    def setupUi(self, Form_2):
        Form_2.setObjectName("Form_2")
        Form_2.resize(760, 537)
        Form_2.setFixedSize(760, 537)
        Form_2.setWindowIcon(QtGui.QIcon("uchhib.png"))
        self.label = QtWidgets.QLabel(Form_2)
        self.label.setGeometry(QtCore.QRect(0, -20, 811, 431))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("1.jpeg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form_2)
        self.label_2.setGeometry(QtCore.QRect(100, 440, 91, 31))
        self.label_2.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"color: rgb(0, 85, 0);\n"
"font: 87 16pt \"Arial Black\";")
        self.label_2.setObjectName("label_2")
        self.db = QtWidgets.QLineEdit(Form_2)
        self.db.setGeometry(QtCore.QRect(190, 440, 381, 31))
        self.db.setObjectName("db")
        self.db_btn = QtWidgets.QPushButton(Form_2)
        self.db_btn.setGeometry(QtCore.QRect(320, 480, 101, 31))
        self.db_btn.setStyleSheet("background-color: rgb(170, 0, 255);\n"
"selection-background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 18pt \"Arial Black\";")
        self.db_btn.setObjectName("db_btn")
        self.label_3 = QtWidgets.QLabel(Form_2)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 141, 101))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("78.png"))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form_2)
        QtCore.QMetaObject.connectSlotsByName(Form_2)

        #################################################################################
        self.db_btn.clicked.connect(self.exportToExcel)

        #################################################################################

    def retranslateUi(self, Form_2):
        _translate = QtCore.QCoreApplication.translate
        Form_2.setWindowTitle(_translate("Form_2", "HEALTH INFORMATION MANAGEMENT DEPARTMENT" ))
        self.label_2.setText(_translate("Form_2", "CLINIC"))
        self.db.setPlaceholderText(_translate("Form_2", "                                              CLINIC NAME HERE"))
        self.db_btn.setText(_translate("Form_2", "ENTER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_2 = QtWidgets.QWidget()
    ui = Ui_Form_2()
    ui.setupUi(Form_2)
    Form_2.show()
    sys.exit(app.exec_())

