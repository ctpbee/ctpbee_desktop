# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log.ui',
# licensing of 'log.ui' applies.
#
# Created: Wed Nov 13 17:55:03 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Log(object):
    def setupUi(self, Log):
        Log.setObjectName("Log")
        Log.resize(675, 212)
        Log.setMinimumSize(QtCore.QSize(675, 212))
        Log.setMaximumSize(QtCore.QSize(9999999, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/menu/images/bee_temp_grey.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Log.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Log)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.log_list = QtWidgets.QListWidget(Log)
        self.log_list.setObjectName("log_list")
        self.verticalLayout.addWidget(self.log_list)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Log)
        QtCore.QMetaObject.connectSlotsByName(Log)

    def retranslateUi(self, Log):
        Log.setWindowTitle(QtWidgets.QApplication.translate("Log", "日志信息", None, -1))

import app.resource.mainwindow_rc
