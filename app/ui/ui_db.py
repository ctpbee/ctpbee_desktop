# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'db.ui',
# licensing of 'db.ui' applies.
#
# Created: Thu Dec 26 16:38:33 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_DataBase(object):
    def setupUi(self, DataBase):
        DataBase.setObjectName("DataBase")
        DataBase.resize(428, 370)
        self.gridLayout = QtWidgets.QGridLayout(DataBase)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(DataBase)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 6, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(self.tab_2)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.gridLayout_2.addWidget(self.password, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        self.user = QtWidgets.QLineEdit(self.tab_2)
        self.user.setObjectName("user")
        self.gridLayout_2.addWidget(self.user, 3, 1, 1, 1)
        self.database = QtWidgets.QLineEdit(self.tab_2)
        self.database.setObjectName("database")
        self.gridLayout_2.addWidget(self.database, 5, 1, 1, 1)
        self.host = QtWidgets.QLineEdit(self.tab_2)
        self.host.setObjectName("host")
        self.gridLayout_2.addWidget(self.host, 2, 1, 1, 1)
        self.close_btn = QtWidgets.QPushButton(self.tab_2)
        self.close_btn.setObjectName("close_btn")
        self.gridLayout_2.addWidget(self.close_btn, 8, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)
        self.ok_btn = QtWidgets.QPushButton(self.tab_2)
        self.ok_btn.setObjectName("ok_btn")
        self.gridLayout_2.addWidget(self.ok_btn, 8, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 2, 1, 1)
        self.port = QtWidgets.QLineEdit(self.tab_2)
        self.port.setObjectName("port")
        self.gridLayout_2.addWidget(self.port, 2, 3, 1, 1)
        self.url = QtWidgets.QLineEdit(self.tab_2)
        self.url.setObjectName("url")
        self.gridLayout_2.addWidget(self.url, 6, 1, 1, 1)
        self.test_btn = QtWidgets.QPushButton(self.tab_2)
        self.test_btn.setObjectName("test_btn")
        self.gridLayout_2.addWidget(self.test_btn, 7, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 2, 1, 1)
        self.name = QtWidgets.QLineEdit(self.tab_2)
        self.name.setObjectName("name")
        self.gridLayout_2.addWidget(self.name, 0, 1, 1, 2)
        self.savebox = QtWidgets.QComboBox(self.tab_2)
        self.savebox.setObjectName("savebox")
        self.savebox.addItem("")
        self.savebox.addItem("")
        self.gridLayout_2.addWidget(self.savebox, 4, 3, 1, 1)
        self.res = QtWidgets.QLabel(self.tab_2)
        self.res.setText("")
        self.res.setObjectName("res")
        self.gridLayout_2.addWidget(self.res, 7, 2, 1, 2)
        self.line = QtWidgets.QFrame(self.tab_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 4)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 1, 1, 1)

        self.retranslateUi(DataBase)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DataBase)

    def retranslateUi(self, DataBase):
        DataBase.setWindowTitle(QtWidgets.QApplication.translate("DataBase", "DataBase", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtWidgets.QApplication.translate("DataBase", "可用", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("DataBase", "URL\n"
"Mongo", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("DataBase", "密码\n"
"Password", None, -1))
        self.close_btn.setText(QtWidgets.QApplication.translate("DataBase", "关闭", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("DataBase", "名称\n"
"name", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("DataBase", "主机\n"
"Host", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("DataBase", "数据库\n"
"Database", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("DataBase", "用户名\n"
"User", None, -1))
        self.ok_btn.setText(QtWidgets.QApplication.translate("DataBase", "新增", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("DataBase", "端口\n"
"Port", None, -1))
        self.test_btn.setText(QtWidgets.QApplication.translate("DataBase", "测试连接", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("DataBase", "保存密码\n"
"save", None, -1))
        self.savebox.setItemText(0, QtWidgets.QApplication.translate("DataBase", "总是", None, -1))
        self.savebox.setItemText(1, QtWidgets.QApplication.translate("DataBase", "从不", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtWidgets.QApplication.translate("DataBase", "数据库配置", None, -1))

