# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'db.ui',
# licensing of 'db.ui' applies.
#
# Created: Fri Dec 20 21:33:48 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_DataBase(object):
    def setupUi(self, DataBase):
        DataBase.setObjectName("DataBase")
        DataBase.resize(467, 430)
        self.gridLayout = QtWidgets.QGridLayout(DataBase)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(DataBase)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.close_btn = QtWidgets.QPushButton(DataBase)
        self.close_btn.setObjectName("close_btn")
        self.gridLayout.addWidget(self.close_btn, 7, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(DataBase)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(DataBase)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.test_btn = QtWidgets.QPushButton(DataBase)
        self.test_btn.setObjectName("test_btn")
        self.gridLayout.addWidget(self.test_btn, 6, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(DataBase)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 2, 1, 1)
        self.ok_btn = QtWidgets.QPushButton(DataBase)
        self.ok_btn.setObjectName("ok_btn")
        self.gridLayout.addWidget(self.ok_btn, 7, 1, 1, 1)
        self.savebox = QtWidgets.QComboBox(DataBase)
        self.savebox.setObjectName("savebox")
        self.savebox.addItem("")
        self.savebox.addItem("")
        self.gridLayout.addWidget(self.savebox, 3, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(DataBase)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(DataBase)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(DataBase)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.host = QtWidgets.QLineEdit(DataBase)
        self.host.setObjectName("host")
        self.gridLayout.addWidget(self.host, 0, 1, 1, 1)
        self.port = QtWidgets.QLineEdit(DataBase)
        self.port.setObjectName("port")
        self.gridLayout.addWidget(self.port, 0, 3, 1, 1)
        self.user = QtWidgets.QLineEdit(DataBase)
        self.user.setObjectName("user")
        self.gridLayout.addWidget(self.user, 1, 1, 1, 1)
        self.password = QtWidgets.QLineEdit(DataBase)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 3, 1, 1, 1)
        self.database = QtWidgets.QLineEdit(DataBase)
        self.database.setObjectName("database")
        self.gridLayout.addWidget(self.database, 4, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(DataBase)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 5, 1, 1, 3)

        self.retranslateUi(DataBase)
        QtCore.QMetaObject.connectSlotsByName(DataBase)

    def retranslateUi(self, DataBase):
        DataBase.setWindowTitle(QtWidgets.QApplication.translate("DataBase", "DataBase", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("DataBase", "主机\n"
"Host", None, -1))
        self.close_btn.setText(QtWidgets.QApplication.translate("DataBase", "关闭", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("DataBase", "密码\n"
"Password", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("DataBase", "用户名\n"
"User", None, -1))
        self.test_btn.setText(QtWidgets.QApplication.translate("DataBase", "测试连接", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("DataBase", "保存密码\n"
"save", None, -1))
        self.ok_btn.setText(QtWidgets.QApplication.translate("DataBase", "应用", None, -1))
        self.savebox.setItemText(0, QtWidgets.QApplication.translate("DataBase", "总是", None, -1))
        self.savebox.setItemText(1, QtWidgets.QApplication.translate("DataBase", "从不", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("DataBase", "数据库\n"
"Database", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("DataBase", "端口\n"
"Port", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("DataBase", "URL\n"
"Mongo", None, -1))
        self.lineEdit.setPlaceholderText(QtWidgets.QApplication.translate("DataBase", "mongodb://user:password@host:port/", None, -1))

