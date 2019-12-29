# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'k_line.ui',
# licensing of 'k_line.ui' applies.
#
# Created: Sun Dec 29 15:43:58 2019
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
        self.gridLayout.addLayout(self.kline_layout, 2, 0, 3, 12)
        self.tick_table = QtWidgets.QTableWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(255)
        sizePolicy.setHeightForWidth(self.tick_table.sizePolicy().hasHeightForWidth())
        self.tick_table.setSizePolicy(sizePolicy)
        self.tick_table.setMinimumSize(QtCore.QSize(0, 300))
        self.tick_table.setMaximumSize(QtCore.QSize(400, 16777215))
        self.tick_table.setObjectName("tick_table")
        self.tick_table.setColumnCount(2)
        self.tick_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tick_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tick_table.setHorizontalHeaderItem(1, item)
        self.tick_table.verticalHeader().setSortIndicatorShown(True)
        self.gridLayout.addWidget(self.tick_table, 1, 12, 4, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 6, 1, 1)
        self.end = QtWidgets.QDateTimeEdit(Form)
        self.end.setObjectName("end")
        self.gridLayout.addWidget(self.end, 1, 7, 1, 1)
        self.start = QtWidgets.QDateTimeEdit(Form)
        self.start.setObjectName("start")
        self.gridLayout.addWidget(self.start, 1, 5, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 4, 1, 1)
        self.frq = QtWidgets.QComboBox(Form)
        self.frq.setObjectName("frq")
        self.gridLayout.addWidget(self.frq, 1, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 9, 1, 1)
        self.symbol_list = QtWidgets.QComboBox(Form)
        self.symbol_list.setEditable(True)
        self.symbol_list.setObjectName("symbol_list")
        self.gridLayout.addWidget(self.symbol_list, 1, 2, 1, 1)
        self.source_btn = QtWidgets.QToolButton(Form)
        self.source_btn.setObjectName("source_btn")
        self.gridLayout.addWidget(self.source_btn, 1, 1, 1, 1)
        self.reload_btn = QtWidgets.QToolButton(Form)
        self.reload_btn.setObjectName("reload_btn")
        self.gridLayout.addWidget(self.reload_btn, 1, 8, 1, 1)
        self.hide_btn = QtWidgets.QToolButton(Form)
        self.hide_btn.setObjectName("hide_btn")
        self.gridLayout.addWidget(self.hide_btn, 1, 10, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.tick_table.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("Form", "key", None, -1))
        self.tick_table.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("Form", "value", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "至", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "起始", None, -1))
        self.source_btn.setText(QtWidgets.QApplication.translate("Form", "数据源", None, -1))
        self.reload_btn.setText(QtWidgets.QApplication.translate("Form", "reload", None, -1))
        self.hide_btn.setText(QtWidgets.QApplication.translate("Form", "隐藏", None, -1))

