import json
import os
import operator
from time import sleep
from PySide2.QtCore import Slot, QUrl
from PySide2.QtGui import QColor
from PySide2.QtWebChannel import QWebChannel
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtWidgets import QWidget, QTableWidgetItem, QPushButton, QMessageBox, QTableWidget, QHeaderView
from ctpbee import helper
from ctpbee.constant import Exchange, TickData
from ctpbee import current_app as bee_current_app

from app.lib.global_var import G
from app.ui.ui_order import Ui_Order

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
exchange_map = {
    "SHFE": Exchange.SHFE,
    "INE": Exchange.INE,
    "CZCE": Exchange.CZCE,
    "CFFEX": Exchange.CFFEX,
    "DCE": Exchange.DCE,
    "SSE": Exchange.SSE,
    "SZSE": Exchange.SZSE,
    "SGE": Exchange.SGE
}

########
#  make sure the same with UI tablewidget columns
position_table_column = (
    'symbol', 'direction', 'exchange', 'volume', 'position_profit', 'price', 'yd_volume', 'operator')
activate_order_table_column = (
    'order_id', 'symbol', 'direction', 'exchange', 'volume', 'price', 'status', 'time', 'type', 'operator')
order_table_column = ('symbol', 'direction', 'exchange', 'volume', 'price', 'status', 'time', 'type')
trade_table_column = ('symbol', 'direction', 'exchange', 'volume', 'price', 'offset', 'time')


class OrderWidget(QWidget, Ui_Order):
    def __init__(self, mainwindow):
        super(OrderWidget, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("下单")
        #
        self.position_table.setEditTriggers(QTableWidget.NoEditTriggers)  # 单元格不可编辑
        self.activate_order_table.setEditTriggers(QTableWidget.NoEditTriggers)  # 单元格不可编辑
        self.order_table.setEditTriggers(QTableWidget.NoEditTriggers)  # 单元格不可编辑
        self.trade_table.setEditTriggers(QTableWidget.NoEditTriggers)  # 单元格不可编辑
        self.tick_table.setEditTriggers(QTableWidget.NoEditTriggers)  # 单元格不可编辑
        #
        self.mainwindow = mainwindow
        self.bee_ext = mainwindow.bee_ext
        # 合约列表
        self.local_symbol_zn.setText(G.subscribes[G.choice_local_symbol] or "未选择")
        for local_symbol in sorted(G.subscribes):
            self.symbol_name_list.addItem(local_symbol)
        self.symbol_name_list.setCurrentText(G.choice_local_symbol or "未选择")
        # k-line
        self.browser = QWebEngineView(self)
        self.channel = QWebChannel()  # 增加一个通信中需要用到的频道
        self.kline_job = mainwindow.kline_job
        self.channel.registerObject("bee_signal", self.kline_job)
        self.browser.page().setWebChannel(self.channel)  # 在浏览器中设置该频道
        self.t = 5  # 递归深度
        self.url = self.search_path(dir=os.path.split(__file__)[0])

        self.browser.page().load(QUrl.fromLocalFile(self.url))
        self.browser.show()
        self.kline_layout.addWidget(self.browser)
        # kline 信号
        self.kline_job.transfer_signal.connect(self.to_js_slot)

        # 买多/卖空
        self.buy_btn.clicked.connect(self.buy_slot)
        self.short_btn.clicked.connect(self.short_slot)
        # 初始化table
        self.tick_row = len(G.order_tick_row_map)

        self.tick_table.setRowCount(0)
        self.position_table.setRowCount(0)
        self.activate_order_table.setRowCount(0)
        self.order_table.setRowCount(0)
        self.trade_table.setRowCount(0)
        #
        self.tick_table.horizontalHeader().setStretchLastSection(True)  # 最后一列自适应表格宽度
        # self.tick_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自适应表格宽度
        self.order_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自适应表格宽度
        self.position_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自适应表格宽度
        self.activate_order_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自适应表格宽度
        self.trade_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自适应表格宽度

        self.activate_order_table.setColumnHidden(0, True)  # 设置order_id隐藏
        # 信号插槽
        self.mainwindow.job.order_tick_signal.connect(self.set_tick_slot)
        self.mainwindow.job.order_position_signal.connect(self.set_position_slot)
        self.mainwindow.job.order_activate_signal.connect(self.set_activate_slot)
        self.mainwindow.job.order_order_signal.connect(self.set_order_slot)
        self.mainwindow.job.order_trade_signal.connect(self.set_trade_slot)
        self.mainwindow.job.account_signal.connect(self.set_account_slot)
        # 信号控制
        self.symbol_name_list.currentIndexChanged.connect(self.symbol_change_slot)  # 监听合约列表
        # 初始化
        self.fill_tick_table()
        self.fill_other()

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
    def to_js_slot(self, data: dict):
        """发送单条bar到js: 只能str """
        self.kline_job.qt_to_js.emit(json.dumps(data))

    def symbol_change_slot(self):
        if G.choice_local_symbol != self.symbol_name_list.currentText():
            G.choice_local_symbol = self.symbol_name_list.currentText()
            self.mainwindow.order_handle()

    def fill_tick_table(self):
        d = G.order_tick_row_map
        tick = G.market_tick[G.choice_local_symbol]
        for row, k in enumerate(d):
            self.tick_table.insertRow(row)
            self.tick_table.setItem(row, 0, QTableWidgetItem(str(tick_zn[k])))
            self.tick_table.setItem(row, 1, QTableWidgetItem(str(tick[k])))

    def fill_other(self):
        ##acount
        bee_current_app.trader.query_account()
        ##position
        all_positions = bee_current_app.recorder.get_all_positions()
        self.set_position_slot(all_positions)
        ## active
        active_orders = []
        for order1 in bee_current_app.recorder.get_all_active_orders():
            o1 = order1._to_dict()
            active_orders.append(o1)
        self.set_activate_slot(active_orders)
        ## order
        orders = []
        for order2 in bee_current_app.recorder.get_all_orders():
            o2 = order2._to_dict()
            orders.append(o2)
        self.set_order_slot(orders)
        ## trade
        trades = []
        for trade in bee_current_app.recorder.get_all_trades():
            t = trade._to_dict()
            trades.append(t)
        self.set_trade_slot(trades)

    @Slot()
    def close_position(self):
        row = self.position_table.currentRow()
        symbol = self.position_table.item(row, position_table_column.index('symbol')).text()
        direction = self.position_table.item(row, position_table_column.index('direction')).text()
        exchange = self.position_table.item(row, position_table_column.index('exchange')).text()
        volume = self.position_table.item(row, position_table_column.index('volume')).text()
        local_symbol = symbol + '.' + exchange
        print(local_symbol)
        tick = TickData(symbol=symbol, exchange=exchange_map[exchange])
        try:
            price = self.bee_ext.app.recorder.get_tick(local_symbol).last_price
        except AttributeError:
            QMessageBox().warning(self, "提示", "未订阅此合约行情", QMessageBox.Ok, QMessageBox.Ok)
        else:
            try:
                if direction == "long":
                    self.bee_ext.app.action.cover(price=float(price), volume=float(volume), origin=tick)
                if direction == "short":
                    self.bee_ext.app.action.sell(price=float(price), volume=float(volume), origin=tick)
                QMessageBox().information(self, "提示", "平仓请求发送成功", QMessageBox.Ok, QMessageBox.Ok)
            except Exception as e:
                print(e)
                QMessageBox().warning(self, "提示", "平仓请求发送失败", QMessageBox.Ok, QMessageBox.Ok)

    @Slot()
    def open_order(self, direction):
        local_symbol = G.choice_local_symbol
        exchange = local_symbol.split(".")[1]
        type = "LIMIT" if self.price_type.currentText() == "限价" else "MARKET"
        price = self.price.text()
        volume = self.volume.text()
        offset = "open"
        req = helper.generate_order_req_by_str(symbol=local_symbol,
                                               exchange=exchange,
                                               direction=direction, offset=offset, volume=int(volume),
                                               price=float(price),
                                               type=type)
        try:
            req_id = self.bee_ext.app.send_order(req)
            sleep(0.2)
            order = self.bee_ext.app.recorder.get_order(req_id)
            if order.status.value == "拒单":
                msg = self.bee_ext.app.recorder.get_new_error()['data']['ErrorMsg']
                QMessageBox().warning(self, "提示", str(msg), QMessageBox.Ok, QMessageBox.Ok)
            else:
                msg = "下单请求发送成功"
                QMessageBox().information(self, "提示", str(msg), QMessageBox.Ok, QMessageBox.Ok)
        except Exception as e:
            msg = "下单请求发送失败"
            QMessageBox().warning(self, "提示", str(msg), QMessageBox.Ok, QMessageBox.Ok)

    @Slot()
    def cancel_order(self):
        row = self.activate_order_table.currentRow()
        symbol = self.activate_order_table.item(row, activate_order_table_column.index('symbol')).text()
        exchange = self.activate_order_table.item(row, activate_order_table_column.index('exchange')).text()
        local_symbol = symbol + '.' + exchange
        order_id = self.activate_order_table.item(row, activate_order_table_column.index('order_id')).text()
        req = helper.generate_cancel_req_by_str(symbol=local_symbol, exchange=exchange, order_id=order_id)
        try:
            bee_current_app.cancel_order(req)
            QMessageBox().information(self, "提示", "撤单请求发送成功", QMessageBox.Ok, QMessageBox.Ok)
        except Exception:
            QMessageBox().warning(self, "提示", "撤单请求发送失败", QMessageBox.Ok, QMessageBox.Ok)

    @Slot()
    def buy_slot(self):
        self.open_order('long')

    @Slot()
    def short_slot(self):
        self.open_order('short')

    @Slot(dict)
    def set_account_slot(self, account):
        map = {
            "accountid": "账户名",
            "available": "账户可用",
            "balance": "余额",
            "frozen": "冻结",
            "gateway_name": "接口",
            "local_account_id": "本地账户名",
        }
        info = []
        for k, v in map.items():
            info.append(str(v) + " : " + str(account.get(k, "")))
        self.account_label.setText("    ".join(info))

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
            self.tick_table.setItem(row, 0, QTableWidgetItem(v))
            self.tick_table.setItem(row, 1, QTableWidgetItem(str(tick[k])))

    @Slot(list)
    def set_position_slot(self, positions: list):
        self.position_table.setRowCount(0)
        row = 0
        x = sorted(positions, key=operator.itemgetter('local_symbol'))
        for p in x:
            self.position_table.insertRow(row)
            for i, col in enumerate(position_table_column):
                if col != 'operator':
                    if col == 'position_profit':
                        new = float(p[col])
                        it = QTableWidgetItem(str(new))
                        if new > 0:
                            it.setTextColor(QColor('red'))
                        elif new < 0:
                            it.setTextColor(QColor('green'))
                        self.position_table.setItem(row, i, it)
                    else:
                        self.position_table.setItem(row, i, QTableWidgetItem(str(p[col])))
                else:
                    btn = QPushButton('平仓')
                    btn.clicked.connect(self.close_position)
                    self.position_table.setCellWidget(row, i, btn)
            row += 1

    @Slot(list)
    def set_activate_slot(self, active_orders: list):
        self.activate_order_table.setRowCount(0)
        row = 0
        x = sorted(active_orders, key=operator.itemgetter('local_symbol'))
        for o in x:
            self.activate_order_table.insertRow(row)
            for i, col in enumerate(activate_order_table_column):  # 渲染
                if col != 'operator':
                    self.activate_order_table.setItem(row, i, QTableWidgetItem(str(o[col])))
                else:
                    btn = QPushButton('撤单')
                    btn.clicked.connect(self.cancel_order)
                    self.activate_order_table.setCellWidget(row, i, btn)
            row += 1

    @Slot(list)
    def set_order_slot(self, orders: list):
        self.order_table.setRowCount(0)
        row = 0
        x = sorted(orders, key=operator.itemgetter('local_symbol'))
        for o in x:
            self.order_table.insertRow(row)
            # 渲染
            for i, col in enumerate(order_table_column):
                self.order_table.setItem(row, i, QTableWidgetItem(str(o[col])))
            row += 1

    @Slot(list)
    def set_trade_slot(self, trades: list):
        self.trade_table.setRowCount(0)
        row = 0
        x = sorted(trades, key=operator.itemgetter('local_symbol'))
        for t in x:
            self.trade_table.insertRow(row)

            for i, col in enumerate(trade_table_column):
                self.trade_table.setItem(row, i, QTableWidgetItem(str(t[col])))
            row += 1
