import sys
from PySide2.QtWidgets import QMessageBox, QWidget, QDialog, QApplication
from pymongo import MongoClient

from app.lib.global_var import G
from app.ui import qss
from app.ui.ui_db import Ui_DataBase


class DBWidget(QDialog, Ui_DataBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setStyleSheet(qss)
        self.config_widget = parent
        self.check_res = None
        #
        self.host.textChanged.connect(self.textChanged_slot)
        self.port.textChanged.connect(self.textChanged_slot)
        self.user.textChanged.connect(self.textChanged_slot)
        self.password.textChanged.connect(self.textChanged_slot)
        self.database.textChanged.connect(self.textChanged_slot)
        # btn
        self.test_btn.clicked.connect(self.test_btn_slot)
        self.ok_btn.clicked.connect(self.ok_btn_slot)
        self.close_btn.clicked.connect(self.close)
        self.host.setText('localhost')
        self.port.setText('27017')
        self.url.setPlaceholderText("mongodb://[user:password@]host:port/database")

    def textChanged_slot(self):
        host = self.host.text()
        port = self.port.text()
        user = self.user.text()
        password = self.password.text()
        database = self.database.text()
        userpwd = ''
        if user and password:
            userpwd = f"{user}:{'*' * len(password)}@"
        self.url.setText(f"mongodb://{userpwd}{host}:{port}/{database}")

    def test_btn_slot(self):
        self.test_btn.setText('connecting...')
        QApplication.processEvents()
        password = self.password.text()
        try:
            url = self.url.text().replace("*" * len(password), password)
            client = MongoClient(url, serverSelectionTimeoutMS=3000,
                                 socketTimeoutMS=3000)
            print(client.list_database_names())
            db = client[self.database.text()]
            print(db.list_collection_names())
            self.check_res = True
            QMessageBox.information(self, '提示', 'connect success!', QMessageBox.Ok, QMessageBox.Ok)
        except Exception as e:
            self.check_res = False
            QMessageBox.information(self, '提示', str(e), QMessageBox.Ok, QMessageBox.Ok)
        self.test_btn.setText('Test Connect')

    def ok_btn_slot(self):
        if self.check_res is None:
            self.test_btn_slot()
        elif self.check_res is True:
            G.db = self.db
            G.config.LOCAL_SOURCE = False
            G.config.to_file()
            self.close()

    def closeEvent(self, arg__1):
        self.config_widget.init_data_source()
        arg__1.accept()


if __name__ == '__main__':
    app = QApplication([])
    dd = DBWidget()
    dd.show()
    sys.exit(app.exec_())
