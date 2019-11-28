import json
import os

from PySide2.QtCore import Slot
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QWidget, QTableWidgetItem, QTableWidget, QHeaderView
from ctpbee import current_app

from app.lib.get_path import desktop_path
from app.lib.helper import QssHelper
from app.ui.ui_account import Ui_Account
from app.lib.global_var import G


# import pyqtgraph as pg


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


class AccountWidget(QWidget, Ui_Account):
    def __init__(self, mainwindow):
        super(AccountWidget, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("账户")
        self.setStyleSheet(QssHelper.read_account())
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
        # self.mainwindow.job.account_signal.connect(self.set_pg)
        ##
        # self.plot = pg.PlotWidget(background=QColor('white'))
        # self.x_axis = self.plot.getAxis('bottom')
        # self.account_layout.addWidget(self.plot)
        # self.fill_pg()

    def fill_pg(self):
        file_path = os.path.join(desktop_path, f"{G.current_account}_diary.json")
        if os.path.exists(file_path):
            with open(file_path, 'r')as f:
                d = f.read()
                if d:
                    data = json.loads(d)
                    x = dict(enumerate(data.keys()))
                    y_available = [i['available'] for i in data.values()]
                    # y_balance = [i['balance'] for i in data.values()]
                    # self.x_axis.setTicks([x.items()])
                    self.plot.plot(y_available, symbol='o')
                    # self.plot.plot(list(x.keys()), y_balance, symbol='t')

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

    # @Slot(dict)
    # def set_pg(self, account):
    #     pass
    # self.plot.setData()
