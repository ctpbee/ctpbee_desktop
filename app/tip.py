from PySide2.QtCore import QTimer
from PySide2.QtGui import Qt, QCloseEvent
from PySide2.QtWidgets import QDialog

from app.ui.ui_tip import Ui_Tip

qss = """
#dd {
    background: #000000;
    border-radius: 10px;
}

#msg{
    color:#ffffff;
    font: 16pt;
}
"""


class TipDialog(QDialog, Ui_Tip):
    def __init__(self, msg):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏整个头部
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setStyleSheet(qss)
        self.msg.setText(msg)
        self.l = [i / 10 for i in range(11)]
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.do)
        self.timer.start(50)
        self.exec_()

    def do(self):
        try:
            i = self.l.pop()
            self.setWindowOpacity(i)
        except IndexError:
            self.close()

    def closeEvent(self, arg__1: QCloseEvent):
        self.timer.stop()
        arg__1.accept()
