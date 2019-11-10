# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loading.ui',
# licensing of 'loading.ui' applies.
#
# Created: Sun Nov 10 12:54:22 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Loading(object):
    def setupUi(self, Loading):
        Loading.setObjectName("Loading")
        Loading.resize(441, 301)
        self.msg = QtWidgets.QLabel(Loading)
        self.msg.setGeometry(QtCore.QRect(120, 80, 181, 81))
        self.msg.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.msg.setStyleSheet("font: 75 14pt \"Arial\";")
        self.msg.setAlignment(QtCore.Qt.AlignCenter)
        self.msg.setObjectName("msg")
        self.progressBar = QtWidgets.QProgressBar(Loading)
        self.progressBar.setGeometry(QtCore.QRect(120, 190, 221, 21))
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 20)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Loading)
        QtCore.QMetaObject.connectSlotsByName(Loading)

    def retranslateUi(self, Loading):
        Loading.setWindowTitle(QtWidgets.QApplication.translate("Loading", "提示", None, -1))
        self.msg.setText(QtWidgets.QApplication.translate("Loading", "emmmmmmm", None, -1))

