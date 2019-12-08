# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log.ui',
# licensing of 'log.ui' applies.
#
# Created: Sun Dec  8 17:11:23 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Log(object):
    def setupUi(self, Log):
        Log.setObjectName("Log")
        Log.resize(749, 400)
        Log.setMinimumSize(QtCore.QSize(675, 212))
        Log.setMaximumSize(QtCore.QSize(9999999, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/menu/images/bee_temp_grey.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Log.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Log)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.kw = QtWidgets.QLineEdit(Log)
        self.kw.setObjectName("kw")
        self.horizontalLayout.addWidget(self.kw)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Log)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.search_list = QtWidgets.QListWidget(Log)
        self.search_list.setObjectName("search_list")
        self.verticalLayout.addWidget(self.search_list)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.log_list = QtWidgets.QListWidget(Log)
        self.log_list.setObjectName("log_list")
        self.horizontalLayout_2.addWidget(self.log_list)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Log)
        QtCore.QMetaObject.connectSlotsByName(Log)

    def retranslateUi(self, Log):
        Log.setWindowTitle(QtWidgets.QApplication.translate("Log", "日志信息", None, -1))
        self.kw.setPlaceholderText(QtWidgets.QApplication.translate("Log", "Search...", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Log", "搜索结果", None, -1))

import app.resource.mainwindow_rc
