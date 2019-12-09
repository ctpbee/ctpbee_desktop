# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'backtrack.ui',
# licensing of 'backtrack.ui' applies.
#
# Created: Mon Dec  9 23:02:42 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(844, 529)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.local_symbol_box = QtWidgets.QComboBox(Form)
        self.local_symbol_box.setEditable(True)
        self.local_symbol_box.setObjectName("local_symbol_box")
        self.verticalLayout_3.addWidget(self.local_symbol_box)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.add_backtrack_btn = QtWidgets.QPushButton(Form)
        self.add_backtrack_btn.setObjectName("add_backtrack_btn")
        self.verticalLayout_2.addWidget(self.add_backtrack_btn)
        self.backtrack_label = QtWidgets.QLabel(Form)
        self.backtrack_label.setAlignment(QtCore.Qt.AlignCenter)
        self.backtrack_label.setObjectName("backtrack_label")
        self.verticalLayout_2.addWidget(self.backtrack_label)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_data_btn = QtWidgets.QPushButton(Form)
        self.add_data_btn.setObjectName("add_data_btn")
        self.verticalLayout.addWidget(self.add_data_btn)
        self.data_label = QtWidgets.QLabel(Form)
        self.data_label.setAlignment(QtCore.Qt.AlignCenter)
        self.data_label.setObjectName("data_label")
        self.verticalLayout.addWidget(self.data_label)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.run_btn = QtWidgets.QPushButton(Form)
        self.run_btn.setObjectName("run_btn")
        self.verticalLayout_3.addWidget(self.run_btn)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.res_layout = QtWidgets.QVBoxLayout()
        self.res_layout.setObjectName("res_layout")
        self.horizontalLayout.addLayout(self.res_layout)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(2, 9)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.add_backtrack_btn.setText(QtWidgets.QApplication.translate("Form", "回测API", None, -1))
        self.backtrack_label.setText(QtWidgets.QApplication.translate("Form", "空", None, -1))
        self.add_data_btn.setText(QtWidgets.QApplication.translate("Form", "添加数据", None, -1))
        self.data_label.setText(QtWidgets.QApplication.translate("Form", "空", None, -1))
        self.run_btn.setText(QtWidgets.QApplication.translate("Form", "Run", None, -1))

