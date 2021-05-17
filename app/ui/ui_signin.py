# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signin.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SignIn(object):
    def setupUi(self, SignIn):
        if not SignIn.objectName():
            SignIn.setObjectName(u"SignIn")
        SignIn.setEnabled(True)
        SignIn.resize(428, 544)
        SignIn.setMinimumSize(QSize(315, 368))
        SignIn.setMaximumSize(QSize(16777215, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/menu/images/bee_temp_grey.png", QSize(), QIcon.Normal, QIcon.Off)
        SignIn.setWindowIcon(icon1)
        SignIn.setAutoFillBackground(False)
        self.verticalLayout_3 = QVBoxLayout(SignIn)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.icon = QLabel(SignIn)
        self.icon.setObjectName(u"icon")
        self.icon.setMinimumSize(QSize(0, 100))
        self.icon.setLayoutDirection(Qt.LeftToRight)
        self.icon.setStyleSheet(u"image: url(:/menu/images/bee_temp_grey.png);\n"
"")

        self.verticalLayout_3.addWidget(self.icon)

        self.login_tab = QStackedWidget(SignIn)
        self.login_tab.setObjectName(u"login_tab")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.login_tab.sizePolicy().hasHeightForWidth())
        self.login_tab.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(8)
        self.login_tab.setFont(font)
        self.login_tab.setStyleSheet(u"")
        self.login_tabPage1 = QWidget()
        self.login_tabPage1.setObjectName(u"login_tabPage1")
        self.gridLayout = QGridLayout(self.login_tabPage1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.gridLayout.addLayout(self.horizontalLayout_4, 5, 1, 1, 1)

        self.scrollArea_2 = QScrollArea(self.login_tabPage1)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 384, 362))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.password_sim = QLineEdit(self.scrollAreaWidgetContents_2)
        self.password_sim.setObjectName(u"password_sim")
        self.password_sim.setMinimumSize(QSize(0, 24))
        self.password_sim.setFont(font)
        self.password_sim.setEchoMode(QLineEdit.Password)

        self.gridLayout_4.addWidget(self.password_sim, 1, 1, 1, 1)

        self.interface_sim = QComboBox(self.scrollAreaWidgetContents_2)
        self.interface_sim.addItem("")
        self.interface_sim.addItem("")
        self.interface_sim.addItem("")
        self.interface_sim.setObjectName(u"interface_sim")
        self.interface_sim.setMinimumSize(QSize(0, 24))
        self.interface_sim.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setWeight(50)
        self.interface_sim.setFont(font1)

        self.gridLayout_4.addWidget(self.interface_sim, 2, 1, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(False)
        font2.setWeight(50)
        self.label_4.setFont(font2)

        self.gridLayout_4.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)

        self.other = QComboBox(self.scrollAreaWidgetContents_2)
        self.other.addItem("")
        self.other.addItem("")
        self.other.setObjectName(u"other")
        self.other.setMinimumSize(QSize(0, 24))
        self.other.setMaximumSize(QSize(16777215, 16777215))
        self.other.setFont(font1)

        self.gridLayout_4.addWidget(self.other, 3, 1, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.gridLayout_4.addWidget(self.label_5, 3, 0, 1, 1)

        self.userid_sim = QComboBox(self.scrollAreaWidgetContents_2)
        self.userid_sim.setObjectName(u"userid_sim")
        self.userid_sim.setMinimumSize(QSize(0, 24))
        self.userid_sim.setFont(font)
        self.userid_sim.setMouseTracking(False)
        self.userid_sim.setFocusPolicy(Qt.WheelFocus)
        self.userid_sim.setEditable(True)

        self.gridLayout_4.addWidget(self.userid_sim, 0, 1, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)

        self.remember_me_sim = QCheckBox(self.scrollAreaWidgetContents_2)
        self.remember_me_sim.setObjectName(u"remember_me_sim")
        font3 = QFont()
        font3.setPointSize(9)
        self.remember_me_sim.setFont(font3)
        self.remember_me_sim.setChecked(True)

        self.gridLayout_4.addWidget(self.remember_me_sim, 4, 1, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.login_tab.addWidget(self.login_tabPage1)
        self.scrollArea_2.raise_()
        self.login_tabPage2 = QWidget()
        self.login_tabPage2.setObjectName(u"login_tabPage2")
        self.gridLayout_2 = QGridLayout(self.login_tabPage2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea = QScrollArea(self.login_tabPage2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 392, 370))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.password = QLineEdit(self.scrollAreaWidgetContents)
        self.password.setObjectName(u"password")
        self.password.setEnabled(True)
        self.password.setMinimumSize(QSize(0, 24))
        self.password.setMaximumSize(QSize(16777215, 16777215))
        self.password.setFont(font1)
        self.password.setEchoMode(QLineEdit.Password)

        self.gridLayout_3.addWidget(self.password, 1, 1, 1, 1)

        self.td_address = QComboBox(self.scrollAreaWidgetContents)
        self.td_address.setObjectName(u"td_address")
        self.td_address.setMinimumSize(QSize(0, 24))
        self.td_address.setFont(font)
        self.td_address.setEditable(True)

        self.gridLayout_3.addWidget(self.td_address, 5, 1, 1, 1)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.gridLayout_3.addWidget(self.label_10, 4, 0, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.gridLayout_3.addWidget(self.label_9, 3, 0, 1, 1)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)

        self.gridLayout_3.addWidget(self.label_13, 7, 0, 1, 1)

        self.userid = QComboBox(self.scrollAreaWidgetContents)
        self.userid.setObjectName(u"userid")
        self.userid.setMinimumSize(QSize(0, 24))
        self.userid.setFont(font)
        self.userid.setEditable(True)

        self.gridLayout_3.addWidget(self.userid, 0, 1, 1, 1)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)

        self.gridLayout_3.addWidget(self.label_12, 6, 0, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)

        self.appid = QComboBox(self.scrollAreaWidgetContents)
        self.appid.setObjectName(u"appid")
        self.appid.setMinimumSize(QSize(0, 24))
        self.appid.setFont(font)
        self.appid.setEditable(True)

        self.gridLayout_3.addWidget(self.appid, 4, 1, 1, 1)

        self.md_address = QComboBox(self.scrollAreaWidgetContents)
        self.md_address.setObjectName(u"md_address")
        self.md_address.setMinimumSize(QSize(0, 24))
        self.md_address.setFont(font)
        self.md_address.setEditable(True)

        self.gridLayout_3.addWidget(self.md_address, 6, 1, 1, 1)

        self.interface_ = QComboBox(self.scrollAreaWidgetContents)
        self.interface_.addItem("")
        self.interface_.addItem("")
        self.interface_.addItem("")
        self.interface_.setObjectName(u"interface_")
        self.interface_.setMinimumSize(QSize(0, 24))
        self.interface_.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setWeight(50)
        self.interface_.setFont(font4)

        self.gridLayout_3.addWidget(self.interface_, 7, 1, 1, 1)

        self.auth_code = QComboBox(self.scrollAreaWidgetContents)
        self.auth_code.setObjectName(u"auth_code")
        self.auth_code.setMinimumSize(QSize(0, 24))
        self.auth_code.setFont(font)
        self.auth_code.setEditable(True)

        self.gridLayout_3.addWidget(self.auth_code, 3, 1, 1, 1)

        self.brokerid = QComboBox(self.scrollAreaWidgetContents)
        self.brokerid.setObjectName(u"brokerid")
        self.brokerid.setMinimumSize(QSize(0, 24))
        self.brokerid.setFont(font)
        self.brokerid.setEditable(True)

        self.gridLayout_3.addWidget(self.brokerid, 2, 1, 1, 1)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.gridLayout_3.addWidget(self.label_11, 5, 0, 1, 1)

        self.remember_me = QCheckBox(self.scrollAreaWidgetContents)
        self.remember_me.setObjectName(u"remember_me")
        self.remember_me.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setPointSize(9)
        font5.setBold(False)
        font5.setWeight(50)
        self.remember_me.setFont(font5)
        self.remember_me.setLayoutDirection(Qt.LeftToRight)
        self.remember_me.setChecked(True)

        self.gridLayout_3.addWidget(self.remember_me, 8, 1, 1, 1)

        self.gridLayout_3.setColumnStretch(1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.login_tab.addWidget(self.login_tabPage2)

        self.verticalLayout_3.addWidget(self.login_tab)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.sign_in_btn = QPushButton(SignIn)
        self.sign_in_btn.setObjectName(u"sign_in_btn")
        self.sign_in_btn.setEnabled(True)
        self.sign_in_btn.setMaximumSize(QSize(16777215, 16777215))
        self.sign_in_btn.setFont(font4)

        self.horizontalLayout.addWidget(self.sign_in_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.retranslateUi(SignIn)

        self.login_tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SignIn)
    # setupUi

    def retranslateUi(self, SignIn):
        SignIn.setWindowTitle(QCoreApplication.translate("SignIn", u"Form", None))
        self.icon.setText("")
        self.interface_sim.setItemText(0, QCoreApplication.translate("SignIn", u"ctp", None))
        self.interface_sim.setItemText(1, QCoreApplication.translate("SignIn", u"ctp_mini", None))
        self.interface_sim.setItemText(2, QCoreApplication.translate("SignIn", u"ctp_se", None))

        self.label_4.setText(QCoreApplication.translate("SignIn", u"\u63a5  \u53e3", None))
        self.label_2.setText(QCoreApplication.translate("SignIn", u"\u7528\u6237\u540d", None))
        self.other.setItemText(0, QCoreApplication.translate("SignIn", u"simnow24\u5c0f\u65f6", None))
        self.other.setItemText(1, QCoreApplication.translate("SignIn", u"simnow\u79fb\u52a8", None))

        self.label_5.setText(QCoreApplication.translate("SignIn", u"\u524d  \u7f6e", None))
        self.label_3.setText(QCoreApplication.translate("SignIn", u"\u5bc6  \u7801", None))
        self.remember_me_sim.setText(QCoreApplication.translate("SignIn", u"\u8bb0\u4f4f\u6211", None))
        self.password.setPlaceholderText("")
        self.label_10.setText(QCoreApplication.translate("SignIn", u"\u4ea7\u54c1\u540d\u79f0", None))
        self.label_6.setText(QCoreApplication.translate("SignIn", u"\u7528\u6237\u540d", None))
        self.label_9.setText(QCoreApplication.translate("SignIn", u"\u8ba4\u8bc1\u7801", None))
        self.label_13.setText(QCoreApplication.translate("SignIn", u"\u63a5\u53e3", None))
        self.label_8.setText(QCoreApplication.translate("SignIn", u"\u671f\u8d27\u516c\u53f8\n"
"\u7f16\u7801", None))
        self.label_12.setText(QCoreApplication.translate("SignIn", u"\u884c\u60c5\u524d\u7f6e", None))
        self.label_7.setText(QCoreApplication.translate("SignIn", u"\u5bc6\u7801", None))
        self.interface_.setItemText(0, QCoreApplication.translate("SignIn", u"ctp", None))
        self.interface_.setItemText(1, QCoreApplication.translate("SignIn", u"ctp_se", None))
        self.interface_.setItemText(2, QCoreApplication.translate("SignIn", u"ctp_mini", None))

        self.label_11.setText(QCoreApplication.translate("SignIn", u"\u4ea4\u6613\u524d\u7f6e", None))
        self.remember_me.setText(QCoreApplication.translate("SignIn", u"\u8bb0\u4f4f\u6211", None))
        self.sign_in_btn.setText(QCoreApplication.translate("SignIn", u"\u767b    \u5f55", None))
    # retranslateUi
