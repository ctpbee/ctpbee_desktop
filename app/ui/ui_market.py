0
1
2
3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'market.ui',
# licensing of 'market.ui' applies.
#
# Created: Mon Sep 30 14:00:05 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Market(object):
    def setupUi(self, Market):
        Market.setObjectName("Market")
        Market.resize(1071, 816)
        Market.setMinimumSize(QtCore.QSize(0, 0))
        self.formLayout = QtWidgets.QFormLayout(Market)
        self.formLayout.setObjectName("formLayout")
        self.tableWidget = QtWidgets.QTableWidget(Market)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.symbol_list = QtWidgets.QComboBox(Market)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.symbol_list.sizePolicy().hasHeightForWidth())
        self.symbol_list.setSizePolicy(sizePolicy)
        self.symbol_list.setMaximumSize(QtCore.QSize(300, 300))
        self.symbol_list.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.symbol_list.setEditable(True)
        self.symbol_list.setObjectName("symbol_list")
        self.horizontalLayout.addWidget(self.symbol_list)
        self.subscribe_singel = QtWidgets.QPushButton(Market)
        self.subscribe_singel.setMaximumSize(QtCore.QSize(100, 200))
        self.subscribe_singel.setObjectName("subscribe_singel")
        self.horizontalLayout.addWidget(self.subscribe_singel)
        self.pushButton_test = QtWidgets.QPushButton(Market)
        self.pushButton_test.setObjectName("pushButton_test")
        self.horizontalLayout.addWidget(self.pushButton_test)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(3, 4)
        self.formLayout.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label = QtWidgets.QLabel(Market)
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.label)

        self.retranslateUi(Market)
        QtCore.QMetaObject.connectSlotsByName(Market)

    def retranslateUi(self, Market):
        Market.setWindowTitle(QtWidgets.QApplication.translate("Market", "Form", None, -1))
        self.tableWidget.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("Market", "中文名", None, -1))
        self.tableWidget.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("Market", "品种", None, -1))
        self.tableWidget.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("Market", "行情", None, -1))
        self.tableWidget.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("Market", "操作", None, -1))
        self.subscribe_singel.setText(QtWidgets.QApplication.translate("Market", "订阅单个", None, -1))
        self.pushButton_test.setText(QtWidgets.QApplication.translate("Market", "订阅所有【测试】", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Market", "订阅列表", None, -1))

