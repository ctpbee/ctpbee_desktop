0
1
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'account.ui',
# licensing of 'account.ui' applies.
#
# Created: Sun Sep 29 21:49:13 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Account(object):
    def setupUi(self, Account):
        Account.setObjectName("Account")
        Account.resize(836, 703)
        Account.setBaseSize(QtCore.QSize(900, 600))
        self.formLayout = QtWidgets.QFormLayout(Account)
        self.formLayout.setObjectName("formLayout")
        self.tableWidget = QtWidgets.QTableWidget(Account)
        self.tableWidget.setMinimumSize(QtCore.QSize(500, 500))
        self.tableWidget.setBaseSize(QtCore.QSize(300, 200))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.tableWidget)
        self.label = QtWidgets.QLabel(Account)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label)

        self.retranslateUi(Account)
        QtCore.QMetaObject.connectSlotsByName(Account)

    def retranslateUi(self, Account):
        Account.setWindowTitle(QtWidgets.QApplication.translate("Account", "Form", None, -1))
        self.tableWidget.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("Account", "key", None, -1))
        self.tableWidget.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("Account", "value", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Account", "基本账户信息", None, -1))

