from PySide2.QtWidgets import QDialog
from app.ui.ui_loading import Ui_Loading


class LoadingDialog(QDialog, Ui_Loading):
    def __init__(self):
        super(LoadingDialog, self).__init__()
        self.setupUi(self)
