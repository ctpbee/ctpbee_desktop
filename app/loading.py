from PySide2.QtCore import Qt, QTimer, QSize
from PySide2.QtGui import QCloseEvent, QBitmap, QPainter
from PySide2.QtWidgets import QDialog, QDesktopWidget
from app.ui.ui_loading import Ui_Loading

qss = """
#bb {
    background: #002025;
    border-radius: 10px;
    opacity: 50;
    border: 1px solid #ff2025;                   
}
"""


class LoadingDialog(QDialog, Ui_Loading):
    def __init__(self):
        super(LoadingDialog, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(qss)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏整个头部
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.do)
        self.timer.start(500)

    def do(self):
        if self.radioButton1.isChecked():
            self.radioButton1.setChecked(False)
            self.radioButton2.setChecked(True)
        else:
            self.radioButton1.setChecked(True)
            self.radioButton2.setChecked(False)

    def closeEvent(self, arg__1: QCloseEvent):
        self.timer.stop()
        arg__1.accept()
