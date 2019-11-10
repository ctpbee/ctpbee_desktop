# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loading.ui',
# licensing of 'loading.ui' applies.
#
# Created: Sun Nov 10 13:47:57 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Loading(object):
    def setupUi(self, Loading):
        Loading.setObjectName("Loading")
        Loading.resize(426, 155)
        Loading.setMinimumSize(QtCore.QSize(426, 155))
        Loading.setMaximumSize(QtCore.QSize(426, 155))
        Loading.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Loading)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.msg = QtWidgets.QLabel(Loading)
        self.msg.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.msg.setStyleSheet("font: 75 14pt \"Arial\";\n"
"color: rgb(0, 170, 0);")
        self.msg.setAlignment(QtCore.Qt.AlignCenter)
        self.msg.setObjectName("msg")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.msg)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(Loading)
        QtCore.QMetaObject.connectSlotsByName(Loading)

    def retranslateUi(self, Loading):
        Loading.setWindowTitle(QtWidgets.QApplication.translate("Loading", "提示", None, -1))
        self.msg.setText(QtWidgets.QApplication.translate("Loading", "emmmmmmm", None, -1))

