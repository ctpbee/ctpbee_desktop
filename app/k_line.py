import os
from datetime import datetime, timedelta

from PySide2.QtCore import QUrl, Slot, QDateTime, QDate
from PySide2.QtWebChannel import QWebChannel
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtWidgets import QWidget, QTableWidgetItem, QTableWidget, QMessageBox

from app.lib.global_var import G
from app.ui import qss
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

contract_space = " " * 2


class KlineWidget(QWidget, Ui_Form):
    def __init__(self, mainwindow):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(qss)
        self.mainwindow = mainwindow
        # calendar
        self.start.setCalendarPopup(True)
        self.end.setCalendarPopup(True)
        self.start.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
        self.end.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
        now = datetime.now() - timedelta(days=30)
        self.start.setDate(QDate(now.year, now.month, now.day))
        self.end.setDateTime(QDateTime.currentDateTime())
        #
        for local_symbol in sorted(G.all_contracts):
            self.symbol_list.addItem(local_symbol + contract_space + G.all_contracts[local_symbol])  # 添加下拉框
        self.symbol_list.currentIndexChanged.connect(self.symbol_change_slot)
        self.frq.addItems(['1min', '2min', '5min'])
        # table
        self.tick_table.setRowCount(0)
        self.tick_row = len(G.order_tick_row_map)
        self.tick_table.horizontalHeader().setStretchLastSection(True)  # 最后一列自适应表格宽度
        # self.tick_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自适应表格宽度
        self.tick_table.setEditTriggers(QTableWidget.NoEditTriggers)  # 单元格不可编辑
        self.tick_table.horizontalHeader().setVisible(False)  # 水平表头不可见
        self.tick_table.verticalHeader().setVisible(False)  # 垂直表头不可见
        # btn
        self.hide_btn.clicked.connect(self.hide_btn_slot)
        self.reload_btn.clicked.connect(self.k_line_reload)
        self.hide_btn_slot()  # 默认隐藏
        self.mainwindow.job.kline_tick_signal.connect(self.set_tick_slot)
        self.ready_action()

    def ready_action(self):
        # k-line
        self.symbol_list.setFocus()
        self.k_line_init()
        if not G.config.LOCAL_SOURCE:
            from app.lib.helper import create_db_conn
            info = G.config.DB_INFO.get(G.config.WHICH_DB)
            if info:
                create_db_conn(**info)
            else:
                replay = QMessageBox.information(self, '提示', '你选择了外部数据源但未指定.是否切换本地数据源',
                                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                if replay == QMessageBox.Yes:
                    G.config.LOCAL_SOURCE = True
                    G.config.to_file()
                    self.k_line_reload()

    def k_line_init(self):
        self.browser = QWebEngineView(self)
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

    def k_line_reload(self):
        # self.browser.reload()
        G.choice_local_symbol = self.symbol_list.currentText().split(contract_space)[0]
        G.frq = self.frq.currentText()
        G.start = self.start.text()
        G.end = self.end.text()
        self.mainwindow.kline_job.qt_to_js_reload.emit()

    def symbol_change_slot(self):
        text = self.symbol_list.currentText()
        local_symbol = text.split(contract_space)[0]
        name = text.split(contract_space)[1]
        if local_symbol in G.all_contracts:
            G.choice_local_symbol = local_symbol
            self.k_line_reload()

    def search_path(self, dir):
        p = os.path.split(dir)[0] + G.kline_folder
        self.t -= 1
        if not os.path.exists(p):
            if self.t < 0:  # 防止超过递归深度
                return os.path.split(__file__)[0] + G.kline_folder
            return self.search_path(dir)
        return p

    def hide_btn_slot(self):
        if self.tick_table.isHidden():
            self.tick_table.show()
            self.hide_btn.setText("<<")
        else:
            self.tick_table.hide()
            self.hide_btn.setText(">>")

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
