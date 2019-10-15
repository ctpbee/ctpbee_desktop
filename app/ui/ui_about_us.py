# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_us.ui',
# licensing of 'about_us.ui' applies.
#
# Created: Sun Sep 29 23:45:18 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_AboutUs(object):
    def setupUi(self, AboutUs):
        AboutUs.setObjectName("AboutUs")
        AboutUs.resize(618, 334)
        self.verticalLayoutWidget = QtWidgets.QWidget(AboutUs)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 601, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setStyleSheet("color: rgb(32, 74, 135);")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AboutUs)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), AboutUs.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), AboutUs.reject)
        QtCore.QMetaObject.connectSlotsByName(AboutUs)

    def retranslateUi(self, AboutUs):
        AboutUs.setWindowTitle(QtWidgets.QApplication.translate("AboutUs", "关于我们", None, -1))
        self.textEdit.setHtml(QtWidgets.QApplication.translate("AboutUs", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:16px; color:#24292e; background-color:#ffffff;\">    </span><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:16px; font-weight:600; color:#24292e; background-color:#ffffff;\">ctpbee</span><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:16px; color:#24292e; background-color:#ffffff;\">主要面对开发者, 希望能得到各位大佬的支持.策略以及指标等工具都以c</span><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:16px; font-weight:600; color:#24292e; background-color:#ffffff;\">tpbee_**</span><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:16px; color:#24292e; background-color:#ffffff;\"> 形式发布.</span><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:16px; font-weight:600; color:#24292e; background-color:#ffffff;\">ctpbee</span><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:16px; color:#24292e; background-color:#ffffff;\">只提供最小的内核.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:16px; color:#24292e; background-color:#ffffff;\">     本人崇尚</span><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:16px; text-decoration: underline; color:#24292e; background-color:#ffffff;\">开源</span><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:16px; color:#24292e; background-color:#ffffff;\">, 无论你是交易者还是程序员, 只要你有新的想法以及对开源感兴趣, 欢迎基于</span><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:16px; font-weight:600; color:#24292e; background-color:#ffffff;\">ctpbee</span><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:16px; color:#24292e; background-color:#ffffff;\"> 开发出新的可用工具. 我会维护一个工具列表, 指引用户前往使用.</span></p></body></html>", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("AboutUs", "CtpBee：", None, -1))
        self.lineEdit.setText(QtWidgets.QApplication.translate("AboutUs", "https://github.com/ctpbee", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("AboutUs", "前往", None, -1))

