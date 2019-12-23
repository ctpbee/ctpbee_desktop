from datetime import time, datetime, timedelta

from PySide2.QtCore import Slot, QTimer
from PySide2.QtWidgets import QWidget, QTableWidget, QTableWidgetItem
from ctpbee import current_app

from app.ui import qss
from app.ui.ui_home import Ui_Home
from app.lib.global_var import G
import webbrowser


def key_zn(key):
    map = {
        "accountid": "账户名",
        "available": "账户可用",
        "balance": "余额",
        "frozen": "冻结",
        "gateway_name": "接口",
        "local_account_id": "本地账户名",
    }
    return map[key]


class HomeWidget(QWidget, Ui_Home):
    def __init__(self, mainwindow):
        super(HomeWidget, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(qss)
        # btn
        self.beebtn.clicked.connect(self.bee_slot)
        self.issues_btn.clicked.connect(self.issues_slot)
        self.doc_btn.clicked.connect(self.doc_slot)
        self.community_btn.clicked.connect(self.community_slot)
        self.quit_btn.clicked.connect(mainwindow.quit)
        # account
        self.row = 0
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)  # 单元格不可编辑
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自适应表格宽度        #
        self.tableWidget.horizontalHeader().setStretchLastSection(True)  # 最后一列自适应表格宽度
        self.fill_table()
        #
        self.mainwindow = mainwindow
        self.mainwindow.job.account_signal.connect(self.set_item)

    def fill_table(self):
        """
        必须按序填充
        :return:
        """
        current_app.trader.query_account()
        d = G.account_row_map
        for index, k in enumerate(d):  # 必须按顺序插入row ,否则渲染失败
            row = index
            self.tableWidget.insertRow(row)
            key = key_zn(k)
            value = G.account[k]  # 获取值
            self.tableWidget.setItem(row, 0, QTableWidgetItem(key))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(value)))

    @Slot(dict)
    def set_item(self, account: dict):
        for k, v in account.items():
            if k not in G.account_row_map:
                row = self.row
                G.account_row_map.append(k)
                self.tableWidget.insertRow(row)
                self.row += 1
            else:
                row = G.account_row_map.index(k)
            key = key_zn(k)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(key))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(v)))

    def bee_slot(self):
        url = "https://github.com/ctpbee"
        self.open_url(url)

    def doc_slot(self):
        url = "https://docs.ctpbee.com/"
        self.open_url(url)

    def community_slot(self):
        url = "http://community.ctpbee.com"
        self.open_url(url)

    def issues_slot(self):
        url = "https://github.com/ctpbee/ctpbee_desktop/issues"
        self.open_url(url)

    def open_url(self, url):
        try:
            webbrowser.get('chrome').open_new_tab(url)
        except Exception as e:
            webbrowser.open_new_tab(url)
