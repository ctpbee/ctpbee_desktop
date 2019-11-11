0
1
2
3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'strategy.ui',
# licensing of 'strategy.ui' applies.
#
# Created: Sun Sep 29 23:07:53 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Strategy(object):
    def setupUi(self, Strategy):
        Strategy.setObjectName("Strategy")
        Strategy.resize(874, 623)
        self.formLayout = QtWidgets.QFormLayout(Strategy)
        self.formLayout.setObjectName("formLayout")
        self.strategy_table = QtWidgets.QTableWidget(Strategy)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.strategy_table.sizePolicy().hasHeightForWidth())
        self.strategy_table.setSizePolicy(sizePolicy)
        self.strategy_table.setObjectName("strategy_table")
        self.strategy_table.setColumnCount(4)
        self.strategy_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.strategy_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.strategy_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.strategy_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.strategy_table.setHorizontalHeaderItem(3, item)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.strategy_table)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_strategy_btn = QtWidgets.QPushButton(Strategy)
        self.add_strategy_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/menu/icon/添加.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_strategy_btn.setIcon(icon)
        self.add_strategy_btn.setObjectName("add_strategy_btn")
        self.horizontalLayout.addWidget(self.add_strategy_btn)
        self.gen_strategy = QtWidgets.QPushButton(Strategy)
        self.gen_strategy.setMaximumSize(QtCore.QSize(200, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/menu/icon/生成支付单.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gen_strategy.setIcon(icon1)
        self.gen_strategy.setObjectName("gen_strategy")
        self.horizontalLayout.addWidget(self.gen_strategy)
        self.horizontalLayout.setStretch(1, 2)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)

        self.retranslateUi(Strategy)
        QtCore.QMetaObject.connectSlotsByName(Strategy)

    def retranslateUi(self, Strategy):
        Strategy.setWindowTitle(QtWidgets.QApplication.translate("Strategy", "Form", None, -1))
        self.strategy_table.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("Strategy", "名称", None, -1))
        self.strategy_table.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("Strategy", "状态", None, -1))
        self.strategy_table.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("Strategy", "操作", None, -1))
        self.strategy_table.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("Strategy", "操作", None, -1))
        self.add_strategy_btn.setText(QtWidgets.QApplication.translate("Strategy", "添加策略", None, -1))
        self.gen_strategy.setText(QtWidgets.QApplication.translate("Strategy", "生成策略模板", None, -1))

import app.resource.mainwindow_rc
