from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from c import Ui_Form_2
import sqlite3


class Ui_MainWindow(object):

    ###############################################
    # FUNCTIONS
    ###############################################

    ########################################################################
    
    def oba(self):
        self.Form_2 = QtWidgets.QWidget()
        self.ui = Ui_Form_2()
        self.ui.setupUi(self.Form_2)
        self.Form_2.show()
        MainWindow.close()
        
        
    def createTable(self):
        con = sqlite3.connect('blessed.db')
        con.execute('''CREATE TABLE IF NOT EXISTS pattern
         (id INT PRIMARY KEY,
         
        dx TEXT,
        icd TEXT,
        male_less_than_1 TEXT,
        female_less_than_1 TEXT,
        male_1_14 TEXT,
        female_1_14 TEXT,
        male_15_44 TEXT,
        female_15_44 TEXT,
        male_45_64 TEXT,
        female_45_64 TEXT,
        male_greater_65 TEXT,
        female_greater_65 TEXT,
        total_male TEXT,
        total_female TEXT,
        g_total TEXT
    
        );

         ''')

    
    def loadData(self):
        con = sqlite3.connect('blessed.db')
        cursor = con.execute('select rowid, dx, icd, male_less_than_1, female_less_than_1, male_1_14, female_1_14, male_15_44, female_15_44, male_45_64, female_45_64, male_greater_65, female_greater_65, total_male, total_female, g_total from pattern')
        
        all_data = cursor.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(all_data):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        

    def getSelectedRowId(self):
        '''Returns current row number '''
        return self.tableWidget.currentRow()
        
    
    def getSelectionUserId(self):
        
        '''Returns id value '''
        return self.tableWidget.item(self.getSelectedRowId(),0).text()
    
    def selectionChanged(self):
        '''Returns item clicked on the table widget '''
        try:
            selected_row = self.getSelectedRowId()
            userId = self.getSelectionUserId()
            #name = self.tableWidget.item(selected_row,1).text()

            self.dx.setText(self.tableWidget.item(selected_row,1).text())
            self.icd_code.setText(self.tableWidget.item(selected_row,2).text())
            self.male_less_than_1_yr.setText(self.tableWidget.item(selected_row,3).text())
            self.female_less_than_1_yr.setText(self.tableWidget.item(selected_row,4).text())
            self.male_1_14_yrs.setText(self.tableWidget.item(selected_row,5).text())
            self.female_1_14_yrs.setText(self.tableWidget.item(selected_row,6).text())
            self.male_15_44_yrs.setText(self.tableWidget.item(selected_row,7).text())
            self.female_15_44_yrs.setText(self.tableWidget.item(selected_row,8).text())

            self.male_45_64_yrs.setText(self.tableWidget.item(selected_row,9).text())
            self.female_45_64_yrs.setText(self.tableWidget.item(selected_row,10).text())
            self.male_greater_65_yrs.setText(self.tableWidget.item(selected_row,11).text())
            self.female_greater_65_yrs.setText(self.tableWidget.item(selected_row,12).text())
            self.total_male.setText(self.tableWidget.item(selected_row,13).text())
            self.total_female.setText(self.tableWidget.item(selected_row,14).text())
            self.g_total.setText(self.tableWidget.item(selected_row,15).text())
           
##            print('selected_row ', selected_row)
##            print('userId ', userId)
##            print('name ', name)
        except:
            self.loadData()
            
            
    def add_it(self):
        dx = self.dx.text()
        icd = self.icd_code.text()
        male_less_than_1 = int(self.male_less_than_1_yr.text())
        female_less_than_1 = int(self.female_less_than_1_yr.text())
        male_1_14 = int(self.male_1_14_yrs.text())
        female_1_14 = int(self.female_1_14_yrs.text())
        male_15_44 = int(self.male_15_44_yrs.text())
        female_15_44 = int(self.female_15_44_yrs.text())
        male_45_64 = int(self.male_45_64_yrs.text())
        female_45_64 = int(self.female_45_64_yrs.text())
        male_greater_65 = int(self.male_greater_65_yrs.text())
        female_greater_65 = int(self.female_greater_65_yrs.text())
        total_male = int(male_less_than_1 + male_1_14 + male_15_44 + male_45_64 + male_greater_65)

        total_female = int(female_less_than_1 + female_1_14 + female_15_44 + female_45_64 + female_greater_65)
        g_total = total_male + total_female

        self.total_male.setText(str(total_male))
        self.total_female.setText(str(total_female))
        
        
        con = sqlite3.connect('blessed.db')
        sql = "INSERT INTO pattern(dx, icd, male_less_than_1, female_less_than_1, male_1_14, female_1_14, male_15_44, female_15_44, male_45_64, female_45_64, male_greater_65, female_greater_65, total_male, total_female, g_total) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) "
        

        data = (dx, icd, male_less_than_1, female_less_than_1, male_1_14, female_1_14, male_15_44, female_15_44, male_45_64, female_45_64, male_greater_65, female_greater_65, total_male, total_female, g_total)
        
        con.execute(sql, data)
        con.commit()
        self.loadData()
        self.update_message('Success', 'Successfully Added ..............')
        self.clear_items()

    def update_message(self,title="Test",message="Please select an item to be updated "):
        QtWidgets.QMessageBox.information(None,title,message)

    def update(self):
        rowid = self.tableWidget.item(self.getSelectedRowId(),0).text()
        dx = self.dx.text()
        icd = self.icd_code.text()
        male_less_than_1 = int(self.male_less_than_1_yr.text())
        female_less_than_1 = int(self.female_less_than_1_yr.text())
        male_1_14 = int(self.male_1_14_yrs.text())
        female_1_14 = int(self.female_1_14_yrs.text())
        male_15_44 = int(self.male_15_44_yrs.text())
        female_15_44 = int(self.female_15_44_yrs.text())
        male_45_64 = int(self.male_45_64_yrs.text())
        female_45_64 = int(self.female_45_64_yrs.text())
        male_greater_65 = int(self.male_greater_65_yrs.text())
        female_greater_65 = int(self.female_greater_65_yrs.text())
        total_male = int(male_less_than_1 + male_1_14 + male_15_44 + male_45_64 + male_greater_65)
        total_female = int(female_less_than_1 + female_1_14 + female_15_44 + female_45_64 + female_greater_65)
        g_total = total_male + total_female

        self.total_male.setText(str(total_male))
        self.total_female.setText(str(total_female))        
        con = sqlite3.connect('blessed.db')
        sql = "UPDATE pattern SET dx =?, icd=?, male_less_than_1 =?, female_less_than_1 =?, male_1_14 =?, female_1_14 =?, male_15_44 =?, female_15_44 =?, male_45_64 =?, female_45_64 =?, male_greater_65 =?, female_greater_65 =?, total_male =?, total_female =?, g_total =?  WHERE rowid =?"
        data = (dx, icd, male_less_than_1, female_less_than_1, male_1_14, female_1_14, male_15_44, female_15_44, male_45_64, female_45_64, male_greater_65, female_greater_65, total_male, total_female, g_total, rowid)

        con.execute(sql, data)
        con.commit()
        self.update_message('Success', 'Successfully Updated')
        self.clear_items()
        self.loadData()

    def delete(self):

        rowid = self.tableWidget.item(self.getSelectedRowId(),0).text()
        con = sqlite3.connect('blessed.db')
        sql = f"DELETE FROM pattern WHERE rowid ={rowid}"
        
        #print(sql)
        con.execute(sql)
        con.commit()
        self.update_message('Success', 'Successfully Deleted! ')
        con.close()
        self.refreshData()
        self.clear_items()

    def refreshData(self):

        '''Removes item from tablewidget and reloads them '''
        try:
            self.tableWidget.clearSelection()
            while(self.tableWidget.rowCount()>0):
                self.tableWidget.removeRow(0)
                self.tableWidget.clearSelection()
            self.loadData()
            self.update_message('Success', 'Successfully Refreshed! ')
        except:
            print("Error Inserting")
            
    def calculate(self):
        male_less_than_1 = int(self.male_less_than_1_yr.text())
        female_less_than_1 = int(self.female_less_than_1_yr.text())
        male_1_14 = int(self.male_1_14_yrs.text())
        female_1_14 = int(self.female_1_14_yrs.text())
        male_15_44 = int(self.male_15_44_yrs.text())
        female_15_44 = int(self.female_15_44_yrs.text())
        male_45_64 = int(self.male_45_64_yrs.text())
        female_45_64 = int(self.female_45_64_yrs.text())
        male_greater_65 = int(self.male_greater_65_yrs.text())
        female_greater_65 = int(self.female_greater_65_yrs.text())
        total_male = int(male_less_than_1 + male_1_14 + male_15_44 + male_45_64 + male_greater_65)

        total_female = int(female_less_than_1 + female_1_14 + female_15_44 + female_45_64 + female_greater_65)
        g_total = total_male + total_female

        self.total_male.setText(str(total_male))
        self.total_female.setText(str(total_female))
        self.g_total.setText(str(g_total))
        
        
    def clear_items(self):
        self.dx.setText("")
        self.icd_code.setText("")
        self.male_less_than_1_yr.setText("")
        self.female_less_than_1_yr.setText("")
        self.male_1_14_yrs.setText("")
        self.female_1_14_yrs.setText("")
        self.male_15_44_yrs.setText("")
        self.female_15_44_yrs.setText("")
        self.male_45_64_yrs.setText("")
        self.female_45_64_yrs.setText("")
        self.male_greater_65_yrs.setText("")
        self.female_greater_65_yrs.setText("")
        self.total_male.setText("")
        self.total_female.setText("")
        self.g_total.setText("")
        
        
        
    def auto_convert_texts(self, txt):
        case_text = txt.title()
        self.dx.setText(case_text)


    def kolorado(self, code):
        code_no = code.title()
        self.icd_code.setText(code_no)


        

    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(671, 696)
        MainWindow.setFixedSize(671, 696)
        MainWindow.setWindowIcon(QtGui.QIcon("78.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QWidget(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(10, 0, 1301, 691))
        self.background.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.background.setObjectName("background")
        self.form = QtWidgets.QWidget(self.background)
        self.form.setGeometry(QtCore.QRect(10, 80, 631, 341))
        self.form.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.form.setObjectName("form")
        self.dx = QtWidgets.QLineEdit(self.form)
        self.dx.setPlaceholderText('    DIAGNOSIS HERE  ')
        self.dx.textChanged.connect(self.auto_convert_texts)
        self.dx.setGeometry(QtCore.QRect(80, 10, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.dx.setFont(font)
        self.dx.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Arial\";")
        
        self.dx.setObjectName("dx")
        self.label = QtWidgets.QLabel(self.form)
        self.label.setGeometry(QtCore.QRect(0, 20, 81, 16))
        self.label.setObjectName("label")
        self.icd_code = QtWidgets.QLineEdit(self.form)
        self.icd_code.setPlaceholderText('CODE NO.')
        self.icd_code.textChanged.connect(self.kolorado)
        self.icd_code.setGeometry(QtCore.QRect(510, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.icd_code.setFont(font)
        self.icd_code.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Arial\";")
        
        
        self.icd_code.setObjectName("icd_code")
        self.label_8 = QtWidgets.QLabel(self.form)
        self.label_8.setGeometry(QtCore.QRect(440, 20, 71, 16))
        self.label_8.setObjectName("label_8")
        self.tableWidget = QtWidgets.QTableWidget(self.form)
        self.tableWidget.setGeometry(QtCore.QRect(-60, 430, 611, 192))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(16)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        self.label_3 = QtWidgets.QLabel(self.form)
        self.label_3.setGeometry(QtCore.QRect(300, 50, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.form)
        self.label_2.setGeometry(QtCore.QRect(180, 50, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_17 = QtWidgets.QLabel(self.form)
        self.label_17.setGeometry(QtCore.QRect(100, 70, 61, 20))
        self.label_17.setObjectName("label_17")
        self.male_less_than_1_yr = QtWidgets.QLineEdit(self.form)
        self.male_less_than_1_yr.setGeometry(QtCore.QRect(190, 70, 61, 21))
        self.male_less_than_1_yr.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 170, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.male_less_than_1_yr.setObjectName("male_less_than_1_yr")
        self.female_less_than_1_yr = QtWidgets.QLineEdit(self.form)
        self.female_less_than_1_yr.setGeometry(QtCore.QRect(310, 70, 61, 21))
        self.female_less_than_1_yr.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 170, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.female_less_than_1_yr.setObjectName("female_less_than_1_yr")
        self.label_18 = QtWidgets.QLabel(self.form)
        self.label_18.setGeometry(QtCore.QRect(100, 100, 71, 20))
        self.label_18.setObjectName("label_18")
        self.male_1_14_yrs = QtWidgets.QLineEdit(self.form)
        self.male_1_14_yrs.setGeometry(QtCore.QRect(190, 100, 61, 21))
        self.male_1_14_yrs.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 170, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.male_1_14_yrs.setObjectName("male_1_14_yrs")
        self.female_1_14_yrs = QtWidgets.QLineEdit(self.form)
        self.female_1_14_yrs.setGeometry(QtCore.QRect(310, 100, 61, 21))
        self.female_1_14_yrs.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 170, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.female_1_14_yrs.setObjectName("female_1_14_yrs")
        self.label_19 = QtWidgets.QLabel(self.form)
        self.label_19.setGeometry(QtCore.QRect(90, 130, 81, 20))
        self.label_19.setObjectName("label_19")
        self.male_15_44_yrs = QtWidgets.QLineEdit(self.form)
        self.male_15_44_yrs.setGeometry(QtCore.QRect(190, 130, 61, 21))
        self.male_15_44_yrs.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 170, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.male_15_44_yrs.setObjectName("male_15_44_yrs")
        self.female_15_44_yrs = QtWidgets.QLineEdit(self.form)
        self.female_15_44_yrs.setGeometry(QtCore.QRect(310, 130, 61, 21))
        self.female_15_44_yrs.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 170, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.female_15_44_yrs.setObjectName("female_15_44_yrs")
        self.label_20 = QtWidgets.QLabel(self.form)
        self.label_20.setGeometry(QtCore.QRect(100, 160, 81, 20))
        self.label_20.setObjectName("label_20")
        self.male_45_64_yrs = QtWidgets.QLineEdit(self.form)
        self.male_45_64_yrs.setGeometry(QtCore.QRect(190, 160, 61, 21))
        self.male_45_64_yrs.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 170, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.male_45_64_yrs.setObjectName("male_45_64_yrs")
        self.female_45_64_yrs = QtWidgets.QLineEdit(self.form)
        self.female_45_64_yrs.setGeometry(QtCore.QRect(310, 160, 61, 21))
        self.female_45_64_yrs.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 170, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.female_45_64_yrs.setObjectName("female_45_64_yrs")
        self.male_greater_65_yrs = QtWidgets.QLineEdit(self.form)
        self.male_greater_65_yrs.setGeometry(QtCore.QRect(190, 190, 61, 21))
        self.male_greater_65_yrs.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 170, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.male_greater_65_yrs.setObjectName("male_greater_65_yrs")
        self.label_21 = QtWidgets.QLabel(self.form)
        self.label_21.setGeometry(QtCore.QRect(100, 190, 81, 20))
        self.label_21.setObjectName("label_21")
        self.female_greater_65_yrs = QtWidgets.QLineEdit(self.form)
        self.female_greater_65_yrs.setGeometry(QtCore.QRect(310, 190, 61, 21))
        self.female_greater_65_yrs.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 170, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.female_greater_65_yrs.setObjectName("female_greater_65_yrs")
        self.cal_btn = QtWidgets.QPushButton(self.form, clicked=lambda: self.calculate())
        self.cal_btn.setGeometry(QtCore.QRect(220, 220, 121, 21))
        self.cal_btn.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 87 11pt \"Arial Black\";\n"
"color: rgb(255, 0, 0);")
        self.cal_btn.setObjectName("cal_btn")
        self.label_22 = QtWidgets.QLabel(self.form)
        self.label_22.setGeometry(QtCore.QRect(100, 250, 81, 20))
        self.label_22.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.label_22.setObjectName("label_22")
        self.total_male = QtWidgets.QLineEdit(self.form)
        self.total_male.setGeometry(QtCore.QRect(190, 250, 61, 21))
        self.total_male.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(170, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.total_male.setObjectName("total_male")
        self.g_total = QtWidgets.QLineEdit(self.form)
        self.g_total.setGeometry(QtCore.QRect(290, 280, 81, 21))
        self.g_total.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 170, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.g_total.setObjectName("g_total")
        self.label_23 = QtWidgets.QLabel(self.form)
        self.label_23.setGeometry(QtCore.QRect(150, 280, 111, 20))
        self.label_23.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.label_23.setObjectName("label_23")
        self.total_female = QtWidgets.QLineEdit(self.form)
        self.total_female.setGeometry(QtCore.QRect(310, 250, 61, 21))
        self.total_female.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(170, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.total_female.setObjectName("total_female")
        self.updatebtn = QtWidgets.QPushButton(self.form, clicked=lambda: self.update())
        self.updatebtn.setGeometry(QtCore.QRect(270, 310, 101, 23))
        self.updatebtn.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"color: rgb(0, 170, 0);\n"
"font: 16pt \"Eras Bold ITC\";")
        self.updatebtn.setObjectName("updatebtn")
        self.viewbtn = QtWidgets.QPushButton(self.form, clicked=lambda: self.refreshData())
        self.viewbtn.setGeometry(QtCore.QRect(170, 310, 81, 23))
        self.viewbtn.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"color: rgb(0, 170, 0);\n"
"font: 16pt \"Eras Bold ITC\";")
        self.viewbtn.setObjectName("viewbtn")
        self.deletebtn = QtWidgets.QPushButton(self.form, clicked=lambda: self.delete())
        self.deletebtn.setGeometry(QtCore.QRect(400, 310, 91, 23))
        self.deletebtn.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"color: rgb(0, 170, 0);\n"
"font: 16pt \"Eras Bold ITC\";")
        self.deletebtn.setObjectName("deletebtn")
        self.clearbtn = QtWidgets.QPushButton(self.form, clicked=lambda: self.clear_items())
        self.clearbtn.setGeometry(QtCore.QRect(510, 310, 81, 23))
        self.clearbtn.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"color: rgb(0, 170, 0);\n"
"font: 16pt \"Eras Bold ITC\";")
        self.clearbtn.setObjectName("clearbtn")
        self.savebtn = QtWidgets.QPushButton(self.form, clicked=lambda: self.add_it())
        self.savebtn.setGeometry(QtCore.QRect(60, 310, 81, 23))
        self.savebtn.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"color: rgb(0, 170, 0);\n"
"font: 16pt \"Eras Bold ITC\";")
        self.savebtn.setObjectName("savebtn")
        self.pattern = QtWidgets.QTextEdit(self.background)
        self.pattern.setGeometry(QtCore.QRect(10, 20, 621, 51))
        self.pattern.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 255);\n"
"font: 75 22pt \"MS Shell Dlg 2\";")
        self.pattern.setObjectName("pattern")
        self.label_7 = QtWidgets.QLabel(self.background)
        self.label_7.setGeometry(QtCore.QRect(30, 30, 151, 31))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("34.png"))
        self.label_7.setObjectName("label_7")
        self.tableWidget = QtWidgets.QTableWidget(self.background)
        self.tableWidget.setGeometry(QtCore.QRect(20, 420, 611, 192))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(16)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        self.label_4 = QtWidgets.QLabel(self.background)
        self.label_4.setGeometry(QtCore.QRect(490, 10, 151, 81))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("medical-ic.png"))
        self.label_4.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.background)
        self.pushButton.setGeometry(QtCore.QRect(230, 632, 161, 41))
        self.pushButton.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        ######################################################################
        self.createTable()
        self.loadData()
        self.tableWidget.itemSelectionChanged.connect(self.selectionChanged)
        # self.pushButton.clicked.connect(self.exportToExcel)
        self.pushButton.clicked.connect(self.oba)

        #####################################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BLESSED ADEOYE OMOBUWA"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">DIAGNOSIS</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">CODE NO</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">FEMALE</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">MALE</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">&lt;  1 YR</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">1 - 14 YRS</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">15 - 44 </span><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">YRS</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">45 - 64 YRS</span></p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">65 YRS &gt;</span></p></body></html>"))
        self.cal_btn.setText(_translate("MainWindow", "CALCULATE"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">TOTAL</span></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">GRAND TOTAL</span></p></body></html>"))
        self.updatebtn.setText(_translate("MainWindow", "UPDATE"))
        self.viewbtn.setText(_translate("MainWindow", "VIEW"))
        self.deletebtn.setText(_translate("MainWindow", "DELETE"))
        self.clearbtn.setText(_translate("MainWindow", "CLEAR"))
        self.savebtn.setText(_translate("MainWindow", "ADD"))
        self.pattern.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:22pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600;\">   DISEASE PATTERN</span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "S/N"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "DIAGNOSIS"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "CODE NO"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "M<1 YR"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "F<1 YR"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "M 1-14 YRS"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "F 1-14 YRS"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "M 15-44 YRS"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "F 15-44 YRS"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "M 45-64 YRS"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "F 45-64 YRS"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "M 65 YRS & ABOVE "))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "F 65 YRS & ABOVE"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "M TOTAL"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "F TOTAL"))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "GRAND"))
        self.pushButton.setText(_translate("MainWindow", "FINISHED"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
