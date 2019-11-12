from PySide2.QtCore import Slot
from PySide2.QtWidgets import QWidget
from app.ui.ui_home import Ui_Home
from app.lib.global_var import G


class HomeWidget(QWidget, Ui_Home):
    def __init__(self, mainwindow):
        super(HomeWidget, self).__init__()
        self.setupUi(self)
