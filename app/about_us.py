import webbrowser

from PySide2.QtWidgets import QDialog
from app.ui.ui_about_us import Ui_AboutUs


class AboutUsDialog(QDialog, Ui_AboutUs):
    def __init__(self):
        super(AboutUsDialog, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_url)

    def open_url(self):
        url = self.lineEdit.text()
        try:
            webbrowser.get('chrome').open_new_tab(url)
        except Exception as e:
            webbrowser.open_new_tab(url)
