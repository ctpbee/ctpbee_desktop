from PySide2.QtCore import Qt, QTimer, Slot
from PySide2.QtGui import QCloseEvent
from PySide2.QtWidgets import QDialog, QAbstractItemView

from app.lib.global_var import G
from app.ui import log_qss
from app.ui.ui_log import Ui_Log


class LogDialog(QDialog, Ui_Log):
    def __init__(self, mainwindow):
        super(LogDialog, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(log_qss)

        # self.setWindowFlags(Qt.WindowStaysOnTopHint)#窗口置顶
        self.mainwindow = mainwindow
        self.mainwindow.job.order_log_signal.connect(self.set_log_slot)
        self.search_list.hide()
        self.label.hide()
        self.fill_log()
        self.kw.textChanged.connect(self.search_slot)

    def fill_log(self):
        for record in G.log_history:
            self.log_list.insertItem(0, record)

    def search_slot(self, kw):
        res = self.log_list.findItems(kw, Qt.MatchContains)
        if len(res) <= 0 or kw.replace(" ", '') is "":
            self.search_list.hide()
            self.label.hide()
        else:
            self.search_list.show()
            self.label.show()
            self.search_list.clear()
            for item in res:
                self.search_list.insertItem(0, item.text())

    @Slot(str)
    def set_log_slot(self, record: str):
        self.log_list.insertItem(0, record)

    def closeEvent(self, arg__1: QCloseEvent):
        self.mainwindow.log_dialog = None
        arg__1.accept()
