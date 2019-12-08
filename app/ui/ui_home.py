0
1
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui',
# licensing of 'home.ui' applies.
#
# Created: Sun Dec  8 21:50:36 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Home(object):
    def setupUi(self, Home):
        Home.setObjectName("Home")
        Home.resize(1098, 705)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/menu/images/bee_temp_grey.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Home.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(Home)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.doc_btn = QtWidgets.QPushButton(Home)
        self.doc_btn.setObjectName("doc_btn")
        self.horizontalLayout.addWidget(self.doc_btn)
        self.community_btn = QtWidgets.QPushButton(Home)
        self.community_btn.setObjectName("community_btn")
        self.horizontalLayout.addWidget(self.community_btn)
        self.beebtn = QtWidgets.QPushButton(Home)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.beebtn.setFont(font)
        self.beebtn.setObjectName("beebtn")
        self.horizontalLayout.addWidget(self.beebtn)
        self.issues_btn = QtWidgets.QPushButton(Home)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.issues_btn.setFont(font)
        self.issues_btn.setObjectName("issues_btn")
        self.horizontalLayout.addWidget(self.issues_btn)
        self.horizontalLayout.setStretch(0, 9)
        self.horizontalLayout.setStretch(4, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 6, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(Home)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 1, 6, 1, 1)
        self.label = QtWidgets.QLabel(Home)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setMargin(0)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 6, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(Home)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setBaseSize(QtCore.QSize(300, 200))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.gridLayout_2.addWidget(self.tableWidget, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Home)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        Home.setWindowTitle(QtWidgets.QApplication.translate("Home", "简介", None, -1))
        self.doc_btn.setText(QtWidgets.QApplication.translate("Home", "📖 文档", None, -1))
        self.community_btn.setText(QtWidgets.QApplication.translate("Home", "👨‍💻 社区", None, -1))
        self.beebtn.setText(QtWidgets.QApplication.translate("Home", "👣 前往组织", None, -1))
        self.issues_btn.setText(QtWidgets.QApplication.translate("Home", "❓ 问题反馈", None, -1))
        self.textEdit.setHtml(QtWidgets.QApplication.translate("Home", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:600;\">.行情</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">双击进入下单界面</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:600;\">.策略</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">参见文档</span><a href=\"https://docs.ctpbee.com/module/strategy\"><span style=\" font-family:\'SimSun\'; text-decoration: underline; color:#0000ff;\">https://docs.ctpbee.com/module/strategy</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\"><br /></span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\"><br /></span></p></body></html>", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Home", "💡 Tip", None, -1))
        self.tableWidget.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("Home", "key", None, -1))
        self.tableWidget.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("Home", "value", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Home", "📜 账户信息", None, -1))

import app.resource.mainwindow_rc
