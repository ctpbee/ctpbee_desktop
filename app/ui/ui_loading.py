# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loading.ui',
# licensing of 'loading.ui' applies.
#
# Created: Fri Nov 29 13:26:29 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Loading(object):
    def setupUi(self, Loading):
        Loading.setObjectName("Loading")
        Loading.resize(329, 102)
        Loading.setMinimumSize(QtCore.QSize(0, 0))
        Loading.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.verticalLayout = QtWidgets.QVBoxLayout(Loading)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bb = QtWidgets.QWidget(Loading)
        self.bb.setObjectName("bb")
        self.formLayout = QtWidgets.QFormLayout(self.bb)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.msg = QtWidgets.QLabel(self.bb)
        self.msg.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.msg.setStyleSheet("font: 75 16pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.msg.setAlignment(QtCore.Qt.AlignCenter)
        self.msg.setObjectName("msg")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.msg)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton1 = QtWidgets.QRadioButton(self.bb)
        self.radioButton1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton1.setText("")
        self.radioButton1.setObjectName("radioButton1")
        self.horizontalLayout_3.addWidget(self.radioButton1)
        self.radioButton2 = QtWidgets.QRadioButton(self.bb)
        self.radioButton2.setAutoFillBackground(False)
        self.radioButton2.setText("")
        self.radioButton2.setChecked(True)
        self.radioButton2.setObjectName("radioButton2")
        self.horizontalLayout_3.addWidget(self.radioButton2)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.bb)

        self.retranslateUi(Loading)
        QtCore.QMetaObject.connectSlotsByName(Loading)

    def retranslateUi(self, Loading):
        Loading.setWindowTitle(QtWidgets.QApplication.translate("Loading", "提示", None, -1))
        self.msg.setText(QtWidgets.QApplication.translate("Loading", "emmmmmmm", None, -1))

