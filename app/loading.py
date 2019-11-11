from PySide2.QtCore import Qt
from PySide2.QtWidgets import QDialog
from app.ui.ui_loading import Ui_Loading


class LoadingDialog(QDialog, Ui_Loading):
    def __init__(self):
        super(LoadingDialog, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏整个头部
