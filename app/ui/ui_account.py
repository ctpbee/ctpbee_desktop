0
1
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'account.ui',
# licensing of 'account.ui' applies.
#
# Created: Tue Nov 26 17:08:45 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Account(object):
    def setupUi(self, Account):
        Account.setObjectName("Account")
        Account.resize(836, 703)
        Account.setBaseSize(QtCore.QSize(900, 600))
        self.gridLayout = QtWidgets.QGridLayout(Account)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(Account)
        self.tableWidget.setMinimumSize(QtCore.QSize(500, 350))
        self.tableWidget.setBaseSize(QtCore.QSize(300, 200))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.tableWidget, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(Account)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        self.account_layout = QtWidgets.QVBoxLayout()
        self.account_layout.setObjectName("account_layout")
        self.gridLayout.addLayout(self.account_layout, 2, 1, 1, 1)

        self.retranslateUi(Account)
        QtCore.QMetaObject.connectSlotsByName(Account)

    def retranslateUi(self, Account):
        Account.setWindowTitle(QtWidgets.QApplication.translate("Account", "Form", None, -1))
        self.tableWidget.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("Account", "key", None, -1))
        self.tableWidget.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("Account", "value", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Account", "基本账户信息", None, -1))

