from PySide2.QtCore import Slot
from PySide2.QtWidgets import QWidget
from app.ui.ui_home import Ui_Home
from app.lib.global_var import G
import webbrowser

qss = """
        QWidget{
background:#ffffff;
    color: #000000;

}
QToolBox::tab{
margin:0px;
border-radius: 5px;
color: #1b89ca;

}

QToolBox::tab:selected {
    color: white;
    background:#1b89ca;
}"""


class HomeWidget(QWidget, Ui_Home):
    def __init__(self, mainwindow):
        super(HomeWidget, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(qss)
        self.beebtn.clicked.connect(self.open_url)
        self.issues_btn.clicked.connect(self.open_url2)

    def open_url(self):
        url = self.ctpbeeurl.text()
        try:
            webbrowser.get('chrome').open_new_tab(url)
        except Exception as e:
            webbrowser.open_new_tab(url)

    def open_url2(self):
        url = self.desktop_url.text()
        try:
            webbrowser.get('chrome').open_new_tab(url)
        except Exception as e:
            webbrowser.open_new_tab(url)
