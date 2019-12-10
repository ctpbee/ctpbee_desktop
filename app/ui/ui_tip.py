# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tip.ui',
# licensing of 'tip.ui' applies.
#
# Created: Tue Dec 10 09:59:16 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Tip(object):
    def setupUi(self, Tip):
        Tip.setObjectName("Tip")
        Tip.resize(255, 122)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Tip)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dd = QtWidgets.QWidget(Tip)
        self.dd.setObjectName("dd")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dd)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.msg = QtWidgets.QLabel(self.dd)
        self.msg.setAlignment(QtCore.Qt.AlignCenter)
        self.msg.setObjectName("msg")
        self.verticalLayout.addWidget(self.msg)
        self.horizontalLayout.addWidget(self.dd)

        self.retranslateUi(Tip)
        QtCore.QMetaObject.connectSlotsByName(Tip)

    def retranslateUi(self, Tip):
        Tip.setWindowTitle(QtWidgets.QApplication.translate("Tip", "Form", None, -1))
        self.msg.setText(QtWidgets.QApplication.translate("Tip", "emmmm", None, -1))

