import sys
from PySide2.QtWidgets import QMessageBox, QWidget, QDialog, QApplication
from pymongo import MongoClient

from app.ui import qss
from app.ui.ui_db import Ui_Form


class DBWidget(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet(qss)
        #
        self.check_res = None
        #
        self.test_btn.clicked.connect(self.test_btn_slot)
        self.ok_btn.clicked.connect(self.ok_btn_slot)

    def get_uri(self):
        host = self.host.text() or 'localhost'
        port = self.port.text() or '27017'
        user = self.user.text()
        password = self.password.text()
        if user and password:
            return f"mongodb://{user}:{password}@{host}:{port}/"
        else:
            return f"mongodb://{host}:{port}/"

    def test_btn_slot(self):
        self.test_btn.setText('connecting...')
        QApplication.processEvents()
        database = self.database.text()
        try:
            client = MongoClient(self.get_uri(), serverSelectionTimeoutMS=3000, socketTimeoutMS=3000)
            db = client[database]
            db.list_collection_names()
            self.check_res = True
            QMessageBox.information(self, '提示', 'connect success!', QMessageBox.Ok, QMessageBox.Ok)
        except Exception as e:
            self.check_res = False
            QMessageBox.information(self, '提示', str(e), QMessageBox.Ok, QMessageBox.Ok)
        self.test_btn.setText('Test Connect')

    def ok_btn_slot(self):
        if self.check_res is None:
            self.test_btn_slot()
        if self.check_res is True:
            pass


if __name__ == '__main__':
    app = QApplication([])
    dd = DBWidget()
    dd.show()
    sys.exit(app.exec_())
