# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui',
# licensing of 'home.ui' applies.
#
# Created: Tue Nov 12 17:40:50 2019
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
        self.icon_tab = QtWidgets.QWidget()
        self.icon_tab.setGeometry(QtCore.QRect(0, 0, 823, 442))
        self.icon_tab.setObjectName("icon_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.icon_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.icon_tab)
        self.label.setStyleSheet("image: url(:/menu/images/bee_temp_grey.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.toolBox.addItem(self.icon_tab, "")
        self.user_guide_tab = QtWidgets.QWidget()
        self.user_guide_tab.setGeometry(QtCore.QRect(0, 0, 823, 442))
        self.user_guide_tab.setObjectName("user_guide_tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.user_guide_tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.textEdit = QtWidgets.QTextEdit(self.user_guide_tab)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_5.addWidget(self.textEdit)
        self.toolBox.addItem(self.user_guide_tab, "")
        self.issues_tab = QtWidgets.QWidget()
        self.issues_tab.setObjectName("issues_tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.issues_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.desktop_url = QtWidgets.QLineEdit(self.issues_tab)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.desktop_url.setFont(font)
        self.desktop_url.setReadOnly(True)
        self.desktop_url.setObjectName("desktop_url")
        self.horizontalLayout_2.addWidget(self.desktop_url)
        self.issues_btn = QtWidgets.QPushButton(self.issues_tab)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.issues_btn.setFont(font)
        self.issues_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 0);")
        self.issues_btn.setObjectName("issues_btn")
        self.horizontalLayout_2.addWidget(self.issues_btn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 367, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.toolBox.addItem(self.issues_tab, "")
        self.about_us_tab = QtWidgets.QWidget()
        self.about_us_tab.setObjectName("about_us_tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.about_us_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.about_us_tab)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_3.addWidget(self.textEdit_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ctpbeeurl = QtWidgets.QLineEdit(self.about_us_tab)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.ctpbeeurl.setFont(font)
        self.ctpbeeurl.setReadOnly(True)
        self.ctpbeeurl.setObjectName("ctpbeeurl")
        self.horizontalLayout.addWidget(self.ctpbeeurl)
        self.beebtn = QtWidgets.QPushButton(self.about_us_tab)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.beebtn.setFont(font)
        self.beebtn.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.beebtn.setObjectName("beebtn")
        self.horizontalLayout.addWidget(self.beebtn)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.about_us_tab)
        self.line.setMinimumSize(QtCore.QSize(0, 10))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.toolBox.addItem(self.about_us_tab, "")
        self.verticalLayout.addWidget(self.toolBox)

        self.retranslateUi(Home)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        Home.setWindowTitle(QtWidgets.QApplication.translate("Home", "简介", None, -1))
        self.toolBox.setItemText(self.toolBox.indexOf(self.icon_tab), QtWidgets.QApplication.translate("Home", "🍯", None, -1))
        self.textEdit.setHtml(QtWidgets.QApplication.translate("Home", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:600; color:#000000;\">一、账户</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:600;\">    用户的基本账户信息，（动态更新）</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:600;\">二、行情</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:600;\">    可选择订阅各合约的行情推送，（动态更新）</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:600;\">三、下单</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:600;\">    需先订阅一个或多个或选择行情。也可在下单界面重新选择合约品种。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:600;\">四、策略</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:600;\">    可先创建策略模板，（需对ctpbee有一些了解，</span><a href=\"https://docs.ctpbee.com/\"><span style=\" font-family:\'SimSun\'; font-weight:600; text-decoration: underline; color:#0000ff;\">入门文档（</span></a><a href=\"https://docs.ctpbee.com/\"><span style=\" font-family:\'SimSun\'; text-decoration: underline; color:#0000ff;\">https://docs.ctpbee.com/</span></a><a href=\"https://docs.ctpbee.com/\"><span style=\" font-family:\'SimSun\'; font-weight:600; text-decoration: underline; color:#0000ff;\">）</span></a><span style=\" font-family:\'SimSun\'; font-weight:600;\">），导入策略模板：策略文件中必须要含有ext变量，同时实例化策略类时，传入的变量作为策略名称。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:600;\">五、回测</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:600;\">    pass</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:600;\">六、配置</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:600;\">    略</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:600;\">七、日志</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:600;\">    包含下单、策略等的日志</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-weight:600;\"><br /></p></body></html>", None, -1))
        self.toolBox.setItemText(self.toolBox.indexOf(self.user_guide_tab), QtWidgets.QApplication.translate("Home", "💡 用户帮助", None, -1))
        self.desktop_url.setText(QtWidgets.QApplication.translate("Home", "https://github.com/ctpbee/ctpbee_desktop/issues", None, -1))
        self.issues_btn.setText(QtWidgets.QApplication.translate("Home", "去提Issues", None, -1))
        self.toolBox.setItemText(self.toolBox.indexOf(self.issues_tab), QtWidgets.QApplication.translate("Home", "❓ 问题反馈", None, -1))
        self.textEdit_2.setHtml(QtWidgets.QApplication.translate("Home", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:16pt; font-style:italic; text-decoration: underline; color:#ff0000;\">我们是一群热爱祖国,热爱学习的有志青年---</span></p>\n"
"<p dir=\'rtl\' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Helvetica\',\'Arial\',\'sans-serif\',\'Apple Color Emoji\',\'Segoe UI Emoji\'; font-size:16pt; color:#24292e; background-color:#ffffff;\">ctpbee_desktop是基于</span><span style=\" font-family:\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Helvetica\',\'Arial\',\'sans-serif\',\'Apple Color Emoji\',\'Segoe UI Emoji\'; font-size:16pt; font-weight:600; color:#24292e; background-color:#ffffff;\">ctpbee</span><span style=\" font-family:\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Helvetica\',\'Arial\',\'sans-serif\',\'Apple Color Emoji\',\'Segoe UI Emoji\'; font-size:16pt; color:#24292e; background-color:#ffffff;\">开发的桌面客户端。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Helvetica\',\'Arial\',\'sans-serif\',\'Apple Color Emoji\',\'Segoe UI Emoji\'; font-size:16pt; color:#24292e;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Helvetica\',\'Arial\',\'sans-serif\',\'Apple Color Emoji\',\'Segoe UI Emoji\'; font-size:16pt; font-weight:600; color:#24292e; background-color:#ffffff;\">【ctpbee主要面对开发者,ctpbee只提供最小的内核，ctpbee是开源项目.</span><span style=\" font-family:\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Helvetica\',\'Arial\',\'sans-serif\',\'Apple Color Emoji\',\'Segoe UI Emoji\'; font-size:16pt; font-style:italic; color:#24292e; background-color:#ffffff;\">如果你同意使用ctpbee, 那么我们默认你清楚你的每个行为带来的后果, 加以思考并</span><span style=\" font-family:\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Helvetica\',\'Arial\',\'sans-serif\',\'Apple Color Emoji\',\'Segoe UI Emoji\'; font-size:16pt; font-weight:600; font-style:italic; color:#24292e; background-color:#ffffff;\">自行承担后果！】</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:16pt;\"><br /></p></body></html>", None, -1))
        self.ctpbeeurl.setText(QtWidgets.QApplication.translate("Home", "https://github.com/ctpbee", None, -1))
        self.beebtn.setText(QtWidgets.QApplication.translate("Home", "前往", None, -1))
        self.toolBox.setItemText(self.toolBox.indexOf(self.about_us_tab), QtWidgets.QApplication.translate("Home", "🙂 我们是谁", None, -1))

import app.resource.mainwindow_rc
