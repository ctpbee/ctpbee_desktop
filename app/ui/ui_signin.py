# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signin.ui',
# licensing of 'signin.ui' applies.
#
# Created: Fri Dec 20 22:21:12 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_SignIn(object):
    def setupUi(self, SignIn):
        SignIn.setObjectName("SignIn")
        SignIn.setEnabled(True)
        SignIn.resize(429, 476)
        SignIn.setMinimumSize(QtCore.QSize(315, 368))
        SignIn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/menu/images/bee_temp_grey.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SignIn.setWindowIcon(icon)
        SignIn.setAutoFillBackground(False)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(SignIn)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.title = QtWidgets.QLabel(SignIn)
        self.title.setObjectName("title")
        self.horizontalLayout_3.addWidget(self.title)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.min_btn = QtWidgets.QToolButton(SignIn)
        self.min_btn.setObjectName("min_btn")
        self.horizontalLayout_3.addWidget(self.min_btn)
        self.close_btn = QtWidgets.QToolButton(SignIn)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout_3.addWidget(self.close_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.login_tab = QtWidgets.QTabWidget(SignIn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.login_tab.sizePolicy().hasHeightForWidth())
        self.login_tab.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.login_tab.setFont(font)
        self.login_tab.setStyleSheet("")
        self.login_tab.setTabPosition(QtWidgets.QTabWidget.North)
        self.login_tab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.login_tab.setObjectName("login_tab")
        self.login1 = QtWidgets.QWidget()
        self.login1.setObjectName("login1")
        self.formLayout = QtWidgets.QFormLayout(self.login1)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.login1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.login1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.login1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.interface_sim = QtWidgets.QComboBox(self.login1)
        self.interface_sim.setMinimumSize(QtCore.QSize(0, 0))
        self.interface_sim.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.interface_sim.setFont(font)
        self.interface_sim.setObjectName("interface_sim")
        self.interface_sim.addItem("")
        self.interface_sim.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.interface_sim)
        self.label_5 = QtWidgets.QLabel(self.login1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.other = QtWidgets.QComboBox(self.login1)
        self.other.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.other.setFont(font)
        self.other.setObjectName("other")
        self.other.addItem("")
        self.other.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.other)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.sign_in_btn_sim = QtWidgets.QPushButton(self.login1)
        self.sign_in_btn_sim.setEnabled(True)
        self.sign_in_btn_sim.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.sign_in_btn_sim.setFont(font)
        self.sign_in_btn_sim.setCheckable(False)
        self.sign_in_btn_sim.setChecked(False)
        self.sign_in_btn_sim.setFlat(False)
        self.sign_in_btn_sim.setObjectName("sign_in_btn_sim")
        self.horizontalLayout_2.addWidget(self.sign_in_btn_sim)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.formLayout.setLayout(7, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.LabelRole, spacerItem3)
        self.userid_sim = QtWidgets.QComboBox(self.login1)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.userid_sim.setFont(font)
        self.userid_sim.setMouseTracking(False)
        self.userid_sim.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.userid_sim.setEditable(True)
        self.userid_sim.setObjectName("userid_sim")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.userid_sim)
        self.password_sim = QtWidgets.QLineEdit(self.login1)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.password_sim.setFont(font)
        self.password_sim.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_sim.setObjectName("password_sim")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.password_sim)
        self.label = QtWidgets.QLabel(self.login1)
        self.label.setMinimumSize(QtCore.QSize(0, 100))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("image: url(:/menu/images/bee_temp_grey.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.remember_me_sim = QtWidgets.QCheckBox(self.login1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.remember_me_sim.setFont(font)
        self.remember_me_sim.setObjectName("remember_me_sim")
        self.horizontalLayout_4.addWidget(self.remember_me_sim)
        self.auto_login_sim = QtWidgets.QCheckBox(self.login1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.auto_login_sim.setFont(font)
        self.auto_login_sim.setObjectName("auto_login_sim")
        self.horizontalLayout_4.addWidget(self.auto_login_sim)
        self.formLayout.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.login_tab.addTab(self.login1, "")
        self.login2 = QtWidgets.QWidget()
        self.login2.setObjectName("login2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.login2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtWidgets.QLabel(self.login2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.login2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.password = QtWidgets.QLineEdit(self.login2)
        self.password.setEnabled(True)
        self.password.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.password.setFont(font)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setPlaceholderText("")
        self.password.setObjectName("password")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password)
        self.label_8 = QtWidgets.QLabel(self.login2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.login2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_10 = QtWidgets.QLabel(self.login2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_11 = QtWidgets.QLabel(self.login2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.label_12 = QtWidgets.QLabel(self.login2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.label_13 = QtWidgets.QLabel(self.login2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.interface_ = QtWidgets.QComboBox(self.login2)
        self.interface_.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.interface_.setFont(font)
        self.interface_.setObjectName("interface_")
        self.interface_.addItem("")
        self.interface_.addItem("")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.interface_)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(8, QtWidgets.QFormLayout.LabelRole, spacerItem4)
        self.remember_me = QtWidgets.QCheckBox(self.login2)
        self.remember_me.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.remember_me.setFont(font)
        self.remember_me.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.remember_me.setChecked(True)
        self.remember_me.setObjectName("remember_me")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.remember_me)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.sign_in_btn = QtWidgets.QPushButton(self.login2)
        self.sign_in_btn.setEnabled(True)
        self.sign_in_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.sign_in_btn.setFont(font)
        self.sign_in_btn.setObjectName("sign_in_btn")
        self.horizontalLayout.addWidget(self.sign_in_btn)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.formLayout_2.setLayout(9, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout)
        self.userid = QtWidgets.QComboBox(self.login2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.userid.setFont(font)
        self.userid.setEditable(True)
        self.userid.setObjectName("userid")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.userid)
        self.brokerid = QtWidgets.QComboBox(self.login2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.brokerid.setFont(font)
        self.brokerid.setEditable(True)
        self.brokerid.setObjectName("brokerid")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.brokerid)
        self.auth_code = QtWidgets.QComboBox(self.login2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.auth_code.setFont(font)
        self.auth_code.setEditable(True)
        self.auth_code.setObjectName("auth_code")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.auth_code)
        self.appid = QtWidgets.QComboBox(self.login2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.appid.setFont(font)
        self.appid.setEditable(True)
        self.appid.setObjectName("appid")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.appid)
        self.td_address = QtWidgets.QComboBox(self.login2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.td_address.setFont(font)
        self.td_address.setEditable(True)
        self.td_address.setObjectName("td_address")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.td_address)
        self.md_address = QtWidgets.QComboBox(self.login2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.md_address.setFont(font)
        self.md_address.setEditable(True)
        self.md_address.setObjectName("md_address")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.md_address)
        self.login_tab.addTab(self.login2, "")
        self.verticalLayout_3.addWidget(self.login_tab)

        self.retranslateUi(SignIn)
        self.login_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SignIn)

    def retranslateUi(self, SignIn):
        SignIn.setWindowTitle(QtWidgets.QApplication.translate("SignIn", "Form", None, -1))
        self.title.setText(QtWidgets.QApplication.translate("SignIn", "🌈ctpbee桌面端", None, -1))
        self.min_btn.setText(QtWidgets.QApplication.translate("SignIn", "—", None, -1))
        self.close_btn.setText(QtWidgets.QApplication.translate("SignIn", "×", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("SignIn", "用户名", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("SignIn", "密  码", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("SignIn", "接  口", None, -1))
        self.interface_sim.setItemText(0, QtWidgets.QApplication.translate("SignIn", "ctp", None, -1))
        self.interface_sim.setItemText(1, QtWidgets.QApplication.translate("SignIn", "ctp_se", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("SignIn", "前  置", None, -1))
        self.other.setItemText(0, QtWidgets.QApplication.translate("SignIn", "simnow24小时", None, -1))
        self.other.setItemText(1, QtWidgets.QApplication.translate("SignIn", "simnow移动", None, -1))
        self.sign_in_btn_sim.setText(QtWidgets.QApplication.translate("SignIn", "登   录", None, -1))
        self.remember_me_sim.setText(QtWidgets.QApplication.translate("SignIn", "记住我", None, -1))
        self.auto_login_sim.setText(QtWidgets.QApplication.translate("SignIn", "自动登录", None, -1))
        self.login_tab.setTabText(self.login_tab.indexOf(self.login1), QtWidgets.QApplication.translate("SignIn", "快速登录", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("SignIn", "用户名", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("SignIn", "密码", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("SignIn", "期货公司编码", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("SignIn", "认证码", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("SignIn", "产品名称", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("SignIn", "交易前置", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("SignIn", "行情前置", None, -1))
        self.label_13.setText(QtWidgets.QApplication.translate("SignIn", "接口", None, -1))
        self.interface_.setItemText(0, QtWidgets.QApplication.translate("SignIn", "ctp", None, -1))
        self.interface_.setItemText(1, QtWidgets.QApplication.translate("SignIn", "ctp_se", None, -1))
        self.remember_me.setText(QtWidgets.QApplication.translate("SignIn", "记住我", None, -1))
        self.sign_in_btn.setText(QtWidgets.QApplication.translate("SignIn", "登    录", None, -1))
        self.login_tab.setTabText(self.login_tab.indexOf(self.login2), QtWidgets.QApplication.translate("SignIn", "详细登录", None, -1))

import app.resource.mainwindow_rc
