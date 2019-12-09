# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'backtrack.ui',
# licensing of 'backtrack.ui' applies.
#
# Created: Mon Dec  9 21:44:51 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(844, 529)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.add_backtrack_btn = QtWidgets.QPushButton(Form)
        self.add_backtrack_btn.setObjectName("add_backtrack_btn")
        self.gridLayout.addWidget(self.add_backtrack_btn, 0, 2, 1, 1)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 4)
        self.add_data_btn = QtWidgets.QPushButton(Form)
        self.add_data_btn.setObjectName("add_data_btn")
        self.gridLayout.addWidget(self.add_data_btn, 0, 1, 1, 1)
        self.local_symbol_box = QtWidgets.QComboBox(Form)
        self.local_symbol_box.setEditable(True)
        self.local_symbol_box.setObjectName("local_symbol_box")
        self.gridLayout.addWidget(self.local_symbol_box, 0, 0, 1, 1)
        self.run_btn = QtWidgets.QPushButton(Form)
        self.run_btn.setObjectName("run_btn")
        self.gridLayout.addWidget(self.run_btn, 0, 3, 1, 1)
        self.res_layout = QtWidgets.QVBoxLayout()
        self.res_layout.setObjectName("res_layout")
        self.gridLayout.addLayout(self.res_layout, 2, 0, 1, 4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.add_backtrack_btn.setText(QtWidgets.QApplication.translate("Form", "回测API", None, -1))
        self.add_data_btn.setText(QtWidgets.QApplication.translate("Form", "添加数据", None, -1))
        self.run_btn.setText(QtWidgets.QApplication.translate("Form", "Run", None, -1))

