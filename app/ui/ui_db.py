# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'db.ui',
# licensing of 'db.ui' applies.
#
# Created: Wed Dec 18 20:55:15 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(467, 430)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.database = QtWidgets.QLineEdit(Form)
        self.database.setObjectName("database")
        self.gridLayout.addWidget(self.database, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.host = QtWidgets.QLineEdit(Form)
        self.host.setObjectName("host")
        self.gridLayout.addWidget(self.host, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.test_btn = QtWidgets.QPushButton(Form)
        self.test_btn.setObjectName("test_btn")
        self.gridLayout.addWidget(self.test_btn, 5, 1, 1, 1)
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setClearButtonEnabled(False)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 3, 1, 1, 1)
        self.user = QtWidgets.QLineEdit(Form)
        self.user.setObjectName("user")
        self.gridLayout.addWidget(self.user, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.port = QtWidgets.QLineEdit(Form)
        self.port.setObjectName("port")
        self.gridLayout.addWidget(self.port, 0, 3, 1, 1)
        self.ok_btn = QtWidgets.QPushButton(Form)
        self.ok_btn.setObjectName("ok_btn")
        self.gridLayout.addWidget(self.ok_btn, 6, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Form", "Database:", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Host:", None, -1))
        self.host.setText(QtWidgets.QApplication.translate("Form", "localhost", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "User:", None, -1))
        self.test_btn.setText(QtWidgets.QApplication.translate("Form", "Test Connect", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "Password:", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Form", "Port", None, -1))
        self.port.setText(QtWidgets.QApplication.translate("Form", "27017", None, -1))
        self.ok_btn.setText(QtWidgets.QApplication.translate("Form", "OK", None, -1))

