# -*- coding: utf-8 -*-
import sqlite3
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import os

class number:
    def __init__(self,number,firstname='Отсутствует',
                 lastname='Отсутствует',adres='Отсутствует'):
        if firstname=='':
            firstname='None'
        if lastname=='':
            lastname='None'
        if adres=='':
            adres='None'
        self.data_number=(str.capitalize(firstname),str.capitalize(lastname),
                          str.capitalize(number),str.capitalize(adres))

class Ui_TelephoneBook(object):
    current_file_path = os.path.abspath(__file__)
    current_directory = os.path.dirname(current_file_path)
    database_path = os.path.join(current_directory, 'database.db')
    def setupUi(self, TelephoneBook):
        TelephoneBook.setObjectName("TelephoneBook")
        TelephoneBook.setMinimumSize(QtCore.QSize(896, 500))
        self.centralwidget = QtWidgets.QWidget(TelephoneBook)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 180, 141, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(190, 370, 641, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 3, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 0, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 1, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 2)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(160, 10, 731, 351))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 40, 141, 101))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_2.addWidget(self.lineEdit_5)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        TelephoneBook.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TelephoneBook)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 896, 21))
        self.menubar.setObjectName("menubar")
        TelephoneBook.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TelephoneBook)
        self.statusbar.setObjectName("statusbar")
        TelephoneBook.setStatusBar(self.statusbar)
        self.actionEnglish = QtWidgets.QAction(TelephoneBook)
        self.actionEnglish.setObjectName("actionEnglish")
        self.action_5 = QtWidgets.QAction(TelephoneBook)
        self.action_5.setObjectName("action_5")

        self.retranslateUi(TelephoneBook)
        QtCore.QMetaObject.connectSlotsByName(TelephoneBook)


        self.connection=sqlite3.connect(Ui_TelephoneBook.database_path)
        self.pushButton.clicked.connect(self.delete_contact)
        self.pushButton_4.clicked.connect(self.submit_contact)
        self.pushButton_3.clicked.connect(self.find_contact)
        self.pushButton_2.clicked.connect(self.change_contact)
        self.refresh()

    def retranslateUi(self, TelephoneBook):
        _translate = QtCore.QCoreApplication.translate
        TelephoneBook.setWindowTitle(_translate("TelephoneBook", "MainWindow"))
        self.pushButton.setText(_translate("TelephoneBook", "Удалить контакт"))
        self.label_3.setText(_translate("TelephoneBook", "Введите номер контакта"))
        self.label_4.setText(_translate("TelephoneBook", "Введите адрес контакта"))
        self.label.setText(_translate("TelephoneBook", "Введите имя контакта"))
        self.label_2.setText(_translate("TelephoneBook", "Введите фамилию контакта"))
        self.pushButton_4.setText(_translate("TelephoneBook", "Добавить запись в справочник"))
        self.pushButton_2.setText(_translate("TelephoneBook", "Изменить контакт"))
        self.pushButton_3.setText(_translate("TelephoneBook", "Найти контакт"))
        self.actionEnglish.setText(_translate("TelephoneBook", "English"))
        self.action_5.setText(_translate("TelephoneBook", "Русский"))
        
    def refresh(self):
        query="""SELECT * FROM expenses ORDER BY lastname"""
        res=self.connection.cursor().execute(query).fetchall()
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['Имя','Фамилия','Номер','Адрес'])
        self.tableWidget.horizontalHeader().setDefaultSectionSize(172)
        self.tableWidget.setRowCount(len(res))
        for i,row in enumerate(res):
            for j,elem in enumerate(row):
                self.tableWidget.setItem(i,j,QTableWidgetItem(str(elem)))
                
    def submit_contact(self):
        self.ind=False
        self.data=number(self.lineEdit_3.text(),self.lineEdit.text(),
                    self.lineEdit_2.text(),self.lineEdit_4.text())
        with sqlite3.connect(Ui_TelephoneBook.database_path) as db:
            cursor=db.cursor()
            query="""INSERT INTO expenses(firstname,lastname,number,adres) VALUES(?,?,?,?)"""
            cursor.execute(query,self.data.data_number)
            self.ind=True
            db.commit()
        if self.ind==True:
            self.refresh()
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()

            
    def find_contact(self):
        self.data=self.lineEdit_5.text()
        if self.data!='':
            self.tableWidget.clear()
            query="""SELECT * FROM expenses WHERE lastname LIKE '{}%'""".format(str.capitalize(self.data))
            res=self.connection.cursor().execute(query).fetchall()
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderLabels(['Имя','Фамилия','Номер','Адрес'])
            self.tableWidget.horizontalHeader().setDefaultSectionSize(175)
            self.tableWidget.setRowCount(len(res))
            for i,row in enumerate(res):
                for j,elem in enumerate(row):
                    self.tableWidget.setItem(i,j,QTableWidgetItem(str(elem)))  
            self.lineEdit_5.clear()
        else:
            self.refresh()
            
    def delete_contact(self):
        roww = self.tableWidget.currentItem().row()
        self.data=self.tableWidget.item(roww, 2).text()
        with sqlite3.connect(Ui_TelephoneBook.database_path) as db:
            cursor=db.cursor()
            query="""DELETE FROM expenses WHERE number ='{}'""".format(self.data)
            cursor.execute(query)
            db.commit()
        self.refresh()
        
    def change_contact(self):
        if self.lineEdit.text()=='':
            roww = self.tableWidget.currentItem().row()
            self.data=[]
            for i in range(4):
                self.data.append(self.tableWidget.item(roww, i).text()) 
            self.lineEdit.setText(self.data[0])
            self.lineEdit_2.setText(self.data[1])
            self.lineEdit_3.setText(self.data[2])
            self.lineEdit_4.setText(self.data[3])
        else:
            self.ind=False
            with sqlite3.connect(Ui_TelephoneBook.database_path) as db:
                cursor=db.cursor()
                query="""UPDATE expenses SET firstname='{1}',lastname='{2}',number='{3}',adres='{4}' WHERE number ='{0}'""".format(self.data[2],
                                                                                                              self.lineEdit.text(),self.lineEdit_2.text(),
                                                                                                              self.lineEdit_3.text(),self.lineEdit_4.text())
                cursor.execute(query)
                self.ind=True
                db.commit()
            if self.ind==True:
                self.refresh()
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.lineEdit_3.clear()
                self.lineEdit_4.clear()
        
    def closeEvent(self,event):
        self.connection.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelephoneBook = QtWidgets.QMainWindow()
    ui = Ui_TelephoneBook()
    ui.setupUi(TelephoneBook)
    TelephoneBook.show()
    sys.exit(app.exec_())