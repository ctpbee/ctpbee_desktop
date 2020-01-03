import sys

from PySide2.QtCore import Qt, QThreadPool, QObject, Signal, Slot
from PySide2.QtWidgets import QMessageBox, QWidget, QDialog, QApplication, QRadioButton, QButtonGroup, QMenu, \
    QTableWidgetItem
from app.lib.helper import create_db_conn, db_connect
from app.lib.global_var import G
from app.lib.worker import Worker
from app.tip import TipDialog
from app.ui import qss
from app.ui.ui_db import Ui_DataBase


class DBObject(QObject):
    dbsig = Signal(str)

    def __init__(self):
        super(self.__class__, self).__init__()


class DBWidget(QDialog, Ui_DataBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setStyleSheet(qss)
        self.config_widget = parent
        self.check_res = None
        self.btn_group = QButtonGroup(self)
        #
        self.res.setWordWrap(True)
        self.user.setFocus()
        self.host.textChanged.connect(self.host_slot)
        self.port.textChanged.connect(self.textChanged_slot)
        self.user.textChanged.connect(self.textChanged_slot)
        self.password.textChanged.connect(self.textChanged_slot)
        self.database.textChanged.connect(self.textChanged_slot)
        # 右键菜单
        self.ava_table.horizontalHeader().setVisible(False)
        self.ava_table.setContextMenuPolicy(Qt.CustomContextMenu)  ######允许右键产生子菜单
        self.ava_table.customContextMenuRequested.connect(self.generate_menu)  ####右键菜单
        # btn
        self.test_btn.clicked.connect(self.test_btn_slot)
        self.ok_btn.clicked.connect(self.ok_btn_slot)
        self.host.setText('localhost')
        self.port.setText('27017')
        self.url.setPlaceholderText("mongodb://[user:password@]host:port/database")
        #
        self.thread_pool = QThreadPool()
        self.sig = DBObject()
        self.sig.dbsig.connect(self.db_connect_result)

    def load_available(self):
        self.ava_table.setRowCount(0)
        self.ava_table.clearContents()
        for name, info in G.config.DB_INFO.items():
            self.ava_table.insertRow(0)
            self.ava_table.setItem(0, 0, QTableWidgetItem(name))
            radio = QRadioButton(self)
            self.btn_group.addButton(radio)
            radio.clicked.connect(self.radio_slot)
            if name == G.config.WHICH_DB:
                radio.setChecked(True)
            self.ava_table.setCellWidget(0, 1, radio)

    def radio_slot(self):
        row = self.ava_table.currentRow()
        name = self.ava_table.item(row, 0).text()
        info = G.config.DB_INFO[name]
        self.thread_pool.start(Worker(db_connect, **info, callback=self.radio_slot_callback))
        G.temp_var = dict(WHICH_DB=name, info=info)

    def radio_slot_callback(self, res):
        if not res:
            G.config.update(G.temp_var)
            create_db_conn(**G.temp_var['info'])  # 创建数据库连接
            G.config.to_file()
            TipDialog("修改成功")
        else:
            TipDialog(f"修改失败{res}")

    def generate_menu(self, pos):
        row_num = -1
        for i in self.ava_table.selectionModel().selection().indexes():
            row_num = i.row()
        if row_num < 0:
            return
        menu = QMenu()
        modify_item = menu.addAction('修改')
        del_item = menu.addAction('删除')
        action = menu.exec_(self.ava_table.mapToGlobal(pos))
        name = self.ava_table.item(row_num, 0).text()
        if action == del_item:
            if G.config.WHICH_DB == name:
                G.config.WHICH_DB = ""
            G.config.DB_INFO.pop(name, None)
            self.ava_table.removeRow(row_num)
        elif action == modify_item:
            self.load_info(G.config.DB_INFO.get(name, {}))
            self.tabWidget.setCurrentIndex(1)

    def load_info(self, info: dict):
        for k, v in info.items():
            w = getattr(self, k)
            if k == 'password':
                w.setText(len(v) * "*")
            else:
                w.setText(v)

    def host_slot(self):
        self.name.setText(self.host.text())
        self.textChanged_slot()

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
        url = self.url.text().replace("*" * len(password), password)
        database = self.database.text()
        self.thread_pool.start(
            Worker(db_connect, url=url, database=database, callback=self.db_connect_callback))

    def db_connect_callback(self, res):
        res = res if res else ""
        self.sig.dbsig.emit(res)

    @Slot(str)
    def db_connect_result(self, res):
        if res:
            self.check_res = False
            self.res.setText(res)
            self.res.setStyleSheet("""color:yellow""")
        else:
            self.check_res = True
            self.res.setText('connect success！')
            self.res.setStyleSheet("""color:green""")
        self.test_btn.setText('Test Connect')

    def ok_btn_slot(self):
        if self.check_res is None:
            self.test_btn_slot()
        if self.check_res is True:
            G.config.DB_INFO[self.name.text()] = dict(host=self.host.text(), user=self.user.text(),
                                                      password=self.password.text() if self.savebox.currentText() == '总是' else "",
                                                      database=self.database.text(), port=self.port.text(),
                                                      url=self.url.text())
            G.config.to_file()
            TipDialog("成功")
            self.tabWidget.setCurrentIndex(0)

    def closeEvent(self, arg__1):
        self.config_widget.init_data_source()
        arg__1.accept()


if __name__ == '__main__':
    app = QApplication([])
    dd = DBWidget()
    dd.show()
    sys.exit(app.exec_())
