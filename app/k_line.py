import json
import os

from PySide2.QtCore import QUrl, Slot
from PySide2.QtWebChannel import QWebChannel
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtWidgets import QWidget, QTableWidgetItem, QTableWidget

from app.lib.global_var import G
from app.ui import kline_qss
from app.ui.ui_k_line import Ui_Form

tick_zn = {
    "local_symbol": '本地id',
    "last_price": '最新价格',
    "ask_price_1": '买一价',
    "ask_volume_1": '买一量',
    "bid_price_1": '卖一价',
    "bid_volume_1": '卖一量',
    "exchange": '交易所',
    "open_interest": '持仓量',
    "pre_close": '昨日收盘价',
    "volume": '成交量',
    "datetime": '时间'
}


class KlineWidget(QWidget, Ui_Form):
    def __init__(self, mainwindow):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(kline_qss)
        self.mainwindow = mainwindow
        # k-line
        self.browser = None
        self.k_line_init()
        # table
        self.tick_table.setRowCount(0)
        self.tick_row = len(G.order_tick_row_map)
        self.tick_table.horizontalHeader().setStretchLastSection(True)  # 最后一列自适应表格宽度
        # self.tick_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自适应表格宽度
        self.tick_table.setEditTriggers(QTableWidget.NoEditTriggers)  # 单元格不可编辑
        self.tick_table.horizontalHeader().setVisible(False)  # 水平表头不可见
        self.tick_table.verticalHeader().setVisible(False)  # 垂直表头不可见
        #
        self.mainwindow.job.order_tick_signal.connect(self.set_tick_slot)

    def k_line_init(self):
        self.symbol.setText(f"{G.choice_local_symbol}")
        if self.browser is None:
            self.browser = QWebEngineView(self)
        else:
            self.kline_layout.removeWidget(self.browser)
        # kline 信号
        self.kline_job = self.mainwindow.kline_job
        # 增加一个通信中需要用到的频道
        self.channel = QWebChannel()
        self.channel.registerObject("bee_signal", self.kline_job)
        # 在浏览器中设置该频道
        self.browser.page().setWebChannel(self.channel)
        self.t = 5  # 递归深度
        self.url = self.search_path(dir=os.path.split(__file__)[0])
        self.browser.page().load(QUrl.fromLocalFile(self.url))
        self.browser.show()
        self.kline_layout.addWidget(self.browser)

    def search_path(self, dir):
        p = os.path.split(dir)[0] + G.kline_folder
        # print(p)
        self.t -= 1
        if not os.path.exists(p):
            if self.t < 0:  # 防止超过递归深度
                return os.path.split(__file__)[0] + G.kline_folder
            return self.search_path(dir)
        return p


    @Slot(dict)
    def set_tick_slot(self, tick: dict):
        local_symbol = tick['local_symbol']
        if local_symbol != G.choice_local_symbol:
            return
        for k, v in tick_zn.items():
            if k not in G.order_tick_row_map:  # 不在表中
                row = self.tick_row
                G.order_tick_row_map.append(k)
                self.tick_table.insertRow(row)
                self.tick_row += 1
            else:
                row = G.order_tick_row_map.index(k)
                if k not in ["local_symbol", "exchange", "datetime"]:
                    space_ = " " * 2
                    old = self.tick_table.item(row, 1).text()
                    different = float(tick[k]) - float(old)
                    if different > 0:  # 增
                        v = f"{v}{space_}↑≈{'%0.2f' % abs(different)}"
                    elif different < 0:  # 减
                        v = f"{v}{space_}↓≈{'%0.2f' % abs(different)}"
                    else:
                        continue
            self.tick_table.setItem(row, 0, QTableWidgetItem(v))
            self.tick_table.setItem(row, 1, QTableWidgetItem(str(tick[k])))

    def fill_tick_table(self):
        d = G.order_tick_row_map
        tick = G.market_tick[G.choice_local_symbol]
        for row, k in enumerate(d):
            self.tick_table.insertRow(row)
            self.tick_table.setItem(row, 0, QTableWidgetItem(str(tick_zn[k])))
            self.tick_table.setItem(row, 1, QTableWidgetItem(str(tick[k])))
