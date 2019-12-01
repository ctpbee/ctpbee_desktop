from PySide2.QtCore import Qt, QTimer, Slot
from PySide2.QtGui import QCloseEvent
from PySide2.QtWidgets import QDialog

from app.lib.global_var import G
from app.ui.ui_log import Ui_Log

qss = """
QWidget{
background:#ffffff;
color:#000000;
margin:0px;
}

QListWidget::item{
margin:10px
}"""


class LogDialog(QDialog, Ui_Log):
    def __init__(self, mainwindow):
        super(LogDialog, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(qss)

        # self.setWindowFlags(Qt.WindowStaysOnTopHint)#窗口置顶
        self.mainwindow = mainwindow
        self.mainwindow.job.order_log_signal.connect(self.set_log_slot)
        self.fill_log()

    def fill_log(self):
        for record in G.log_history:
            self.log_list.insertItem(0, record)

    @Slot(str)
    def set_log_slot(self, record: str):
        self.log_list.insertItem(0, record)
        # if self.log_list.count() > 500:
        #     self.log_list.clear()

    def closeEvent(self, arg__1: QCloseEvent):
        self.mainwindow.log_dialog = None
        arg__1.accept()
