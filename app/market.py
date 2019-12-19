import time

from PySide2.QtCore import Slot, QTimer, Qt
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QWidget, QTableWidgetItem, QPushButton, QMessageBox, QListWidgetItem, QTableWidget, \
    QHeaderView, QAbstractItemView, QMenu
from ctpbee import current_app

from app.tip import TipDialog
from app.ui.ui_market import Ui_Market
from app.lib.global_var import G
from app.ui import qss

contract_space = " " * 2
market_table_column = ['name',  # 中文名
                       'local_symbol',  # 品种
                       'last_price',  # 最新
                       'ask_price_1',  # 买价
                       'bid_price_1',  # 卖价
                       'ask_volume_1',  # 买量
                       'bid_volume_1',  # 卖量
                       'volume',  # 成交量
                       'limit',  # 涨跌  ====
                       'limit1',  # 涨幅  =====
                       'open_interest',  # 持仓量
                       'inc_day_interest',  # 日增仓 open_interest-pre_open_interest
                       'open_price',  # 开盘
                       'high_price',  # 最高
                       'inc_now_interest',  # 现增仓 =====
                       'pre_close'  # 昨收
                       ]

yellow = ['local_symbol', 'ask_volume_1', 'bid_volume_1', 'volume', 'open_interest']


class MarketWidget(QWidget, Ui_Market):
    def __init__(self, mainwindow):
        super(MarketWidget, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(qss)
        self.setWindowTitle("行情")
        self.item_row = len(G.market_tick_row_map)
        self.mainwindow = mainwindow
        self.load_status = self.mainwindow.status_msg
        # ctpbee
        for local_symbol in sorted(G.all_contracts):
            self.symbol_list.addItem(local_symbol + contract_space + G.all_contracts[local_symbol])  # 添加下拉框
        #
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)  # 单元格不可编辑
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自适应表格宽度
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.cellDoubleClicked.connect(self.cellDoubleClicked_slot)
        # 渲染table
        self.obj = self.mainwindow.job
        self.obj.market_signal.connect(self.set_item_slot)
        # 订阅
        self.subscribe_singel.clicked.connect(self.subscribe_slot)
        self.subscribe_type.clicked.connect(self.subscribe_type_slot)
        self.subscribe_all.clicked.connect(self.subscribe_all_slot)
        self.unsubscribe.clicked.connect(self.unsubscribe_all_slot)
        # 右键菜单
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)  ######允许右键产生子菜单
        self.tableWidget.customContextMenuRequested.connect(self.generate_menu)  ####右键菜单

        # timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timer_slot)

    def generate_menu(self, pos):
        row_num = -1
        for i in self.tableWidget.selectionModel().selection().indexes():
            row_num = i.row()
        if row_num < 0:
            return
        menu = QMenu()
        item1 = menu.addAction("取消订阅")
        action = menu.exec_(self.tableWidget.mapToGlobal(pos))
        row_data = self.tableWidget.item(row_num, market_table_column.index('local_symbol'))
        if action == item1 and row_data:
            local_symbol = row_data.text()
            # 取消订阅
            res = current_app.market.unsubscribe(local_symbol.split('.')[0])
            # 事后处理
            if res == 0:
                G.market_tick_row_map.remove(local_symbol)
                G.subscribes.pop(local_symbol, None)
                self.tableWidget.removeRow(row_num)
                self.item_row -= 1

    @Slot()
    def cellDoubleClicked_slot(self, row, col):
        name = self.tableWidget.item(row, 0).text()
        local_symbol = self.tableWidget.item(row, 1).text()
        G.choice_local_symbol = local_symbol
        self.mainwindow.kline_handle()

    @Slot()
    def timer_slot(self):
        self.load_status.setText("正在加载...")
        if time.time() - self.load_time > 0.5:
            self.load_status.setText("订阅合约列表加载完成")
            self.timer.stop()
            self.tableWidget.setEnabled(True)

    def fresh_(self):
        self.item_row = 0
        self.tableWidget.setRowCount(0)
        G.subscribes.clear()
        G.market_tick_row_map.clear()

    @Slot()
    def unsubscribe_all_slot(self):
        for i in G.subscribes:
            res = current_app.market.unsubscribe(i.split('.')[0])
        self.fresh_()

    @Slot()
    def subscribe_slot(self):
        text = self.symbol_list.currentText()
        local_symbol = text.split(contract_space)[0]
        name = text.split(contract_space)[1]
        if local_symbol not in G.all_contracts:
            TipDialog("未知合约")
            return
        if local_symbol:
            res = current_app.subscribe(local_symbol)
            if res == 0:
                G.subscribes.update({local_symbol: name})
                TipDialog("订阅成功")
            else:
                TipDialog("订阅失败")

    @Slot()
    def subscribe_type_slot(self):
        text = self.symbol_list.currentText()
        local_symbol_ = text.split(contract_space)[0]
        symbol = ''.join([x for x in local_symbol_.split('.')[0] if x.isalpha()])  # AP
        if local_symbol_ not in G.all_contracts:
            TipDialog("未知合约")
            return
        for local_symbol in G.all_contracts:
            if local_symbol.startswith(symbol):
                res = current_app.subscribe(local_symbol)
                if res == 0:
                    G.subscribes.update({local_symbol: G.all_contracts[local_symbol]})

    @Slot()
    def subscribe_all_slot(self):
        self.load_time = time.time()
        self.timer.start(300)
        self.tableWidget.setDisabled(True)
        for local_symbol in sorted(G.all_contracts):
            res = current_app.subscribe(local_symbol)  # 订阅
            if res == 0:
                G.subscribes.update({local_symbol: G.all_contracts[local_symbol]})  # 更新订阅列表

    def insert_(self, row, tick):
        for i, col in enumerate(market_table_column):
            item = QTableWidgetItem(str(tick.get(col, "---")))
            if col in yellow:
                item.setTextColor(QColor(199, 199, 9))
            self.tableWidget.setItem(row, i, item)

    @Slot()
    def set_item_slot(self, tick: dict):
        local_symbol = tick['local_symbol']
        if local_symbol not in G.market_tick_row_map:  # 不在table ,插入row
            G.market_tick_row_map.append(local_symbol)
            row = self.item_row
            self.tableWidget.insertRow(row)
            self.item_row += 1
            # 渲染
            self.load_time = time.time()  # 刷新渲染动画计时
            self.insert_(row, tick)
        else:  # 已在table中 ,更新对应row
            row = G.market_tick_row_map.index(local_symbol)
            for i, col in enumerate(market_table_column):
                if col == "last_price":  # 对最新价动态颜色表示涨跌
                    old = self.tableWidget.item(row, i)
                    if old:  # 非空
                        old = float(old.text())
                        new = float(tick[col])
                        difference = new - old
                        item = QTableWidgetItem(str(new))
                        if difference > 0:  # 涨
                            item.setTextColor(QColor('red'))
                        elif difference < 0:  # 跌
                            item.setTextColor(QColor('green'))
                        else:
                            continue
                    else:  # None
                        item = QTableWidgetItem(str(tick[col]))
                elif col == "inc_day_interest":
                    data = tick['open_interest'] - tick['pre_open_interest']
                    item = QTableWidgetItem(str(data))
                    # item.setTextColor()
                # elif col == "inc_now_interest":
                #     item = ''
                # elif col == "limit":
                #     item = ''
                # elif col == "limit1":
                #     item = ''
                else:
                    item = QTableWidgetItem(str(tick.get(col, "---")))
                if item.text().isdigit():
                    item.setText("%0.2f" % float(item.text()))
                if col in yellow:
                    item.setTextColor(QColor(199, 199, 9))
                self.tableWidget.setItem(row, i, item)
