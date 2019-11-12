# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui',
# licensing of 'home.ui' applies.
#
# Created: Tue Nov 12 16:35:43 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Home(object):
    def setupUi(self, Home):
        Home.setObjectName("Home")
        Home.resize(845, 604)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/menu/images/bee_temp_grey.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Home.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Home)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolBox = QtWidgets.QToolBox(Home)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 823, 457))
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setStyleSheet("image: url(:/menu/images/bee_temp_grey.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 823, 457))
        self.page_2.setObjectName("page_2")
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.toolBox.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.toolBox.addItem(self.page_4, "")
        self.verticalLayout.addWidget(self.toolBox)

        self.retranslateUi(Home)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        Home.setWindowTitle(QtWidgets.QApplication.translate("Home", "简介", None, -1))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QtWidgets.QApplication.translate("Home", "💡", None, -1))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QtWidgets.QApplication.translate("Home", "用户引导", None, -1))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QtWidgets.QApplication.translate("Home", "问题反馈", None, -1))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QtWidgets.QApplication.translate("Home", "我们是谁？", None, -1))

import app.resource.mainwindow_rc
