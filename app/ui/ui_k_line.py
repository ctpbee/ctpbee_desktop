
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'k_line.ui',
# licensing of 'k_line.ui' applies.
#
# Created: Sun Dec  8 22:57:08 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1091, 602)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.kline_layout = QtWidgets.QVBoxLayout()
        self.kline_layout.setObjectName("kline_layout")
        self.gridLayout.addLayout(self.kline_layout, 1, 0, 1, 1)
        self.tick_table = QtWidgets.QTableWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(255)
        sizePolicy.setHeightForWidth(self.tick_table.sizePolicy().hasHeightForWidth())
        self.tick_table.setSizePolicy(sizePolicy)
        self.tick_table.setMinimumSize(QtCore.QSize(0, 400))
        self.tick_table.setMaximumSize(QtCore.QSize(400, 16777215))
        self.tick_table.setObjectName("tick_table")
        self.tick_table.setColumnCount(2)
        self.tick_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tick_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tick_table.setHorizontalHeaderItem(1, item)
        self.tick_table.verticalHeader().setSortIndicatorShown(True)
        self.gridLayout.addWidget(self.tick_table, 1, 1, 1, 1)
        self.symbol = QtWidgets.QLabel(Form)
        self.symbol.setObjectName("symbol")
        self.gridLayout.addWidget(self.symbol, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.tick_table.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("Form", "key", None, -1))
        self.tick_table.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("Form", "value", None, -1))
        self.symbol.setText(QtWidgets.QApplication.translate("Form", "symbol", None, -1))

