import json
import os
from time import sleep
from PySide2.QtCore import Slot, QUrl
from PySide2.QtWebChannel import QWebChannel
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtWidgets import QWidget, QTableWidgetItem, QPushButton, QMessageBox, QTableWidget, QHeaderView
from ctpbee import helper
from ctpbee.constant import Exchange, TickData
from ctpbee import current_app as bee_current_app
from app.lib.global_var import G
from app.ui.ui_order import Ui_Order

tick_zn = {
    "ask_price_1": '买一价',
    "ask_volume_1": '买一量',
    "bid_price_1": '卖一价',
    "bid_volume_1": '卖一量',
    "last_price": '最新价格',
    "local_symbol": '本地id',
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
        self.tick_row = len(G.order_tick_row_map)
        self.position_row = len(G.order_position_row_map)
        self.activate_row = len(G.order_activate_row_map)
        self.order_row = len(G.order_order_row_map)
        self.trade_row = len(G.order_trade_row_map)
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
        # self.fill_tick_table()
        # self.fill_position_table()
        # self.fill_trade_table()
        # self.fill_order_table()
        # self.fill_activate_table()

        self.tick_table.setRowCount(self.tick_row)
        self.position_table.setRowCount(self.position_row)
        self.activate_order_table.setRowCount(self.activate_row)
        self.order_table.setRowCount(self.order_row)
        self.trade_table.setRowCount(self.trade_row)
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
        # 信号控制
        self.symbol_name_list.currentIndexChanged.connect(self.symbol_change_slot)  # 监听合约列表

    def search_path(self, dir):
        p = os.path.split(dir)[0] + '/static/kline.html'
        # print(p)
        self.t -= 1
        if not os.path.exists(p):
            if self.t < 0:  # 防止超过递归深度
                return os.path.split(__file__)[0] + '/static/kline.html'
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
        for index, k in enumerate(d):
            row = index
            self.tick_table.insertRow(row)
            self.tick_table.setItem(row, 0, QTableWidgetItem(str(tick_zn[k])))
            self.tick_table.setItem(row, 1, QTableWidgetItem(str(tick[k])))

    def fill_position_table(self):
        d = G.order_position_row_map
        for index, k in enumerate(d):
            row = index
            try:
                p = G.order_position[k]
            except KeyError:  # 说明此订单已平
                d.remove(k)  # 删除表row映射
                continue
            self.position_table.insertRow(row)
            for i, col in enumerate(position_table_column):
                if col != 'operator':
                    self.position_table.setItem(row, i, QTableWidgetItem(str(p[col])))
                else:
                    btn = QPushButton('平仓')
                    self.position_table.setCellWidget(row, i, btn)

    def fill_order_table(self):
        d = G.order_order_row_map
        for index, k in enumerate(d):
            row = index
            try:
                p = G.order_order[k]
            except KeyError:
                d.remove(k)
                continue
            self.order_table.insertRow(row)
            for i, col in enumerate(order_table_column):
                self.order_table.setItem(row, i, QTableWidgetItem(str(p[col])))

    def fill_activate_table(self):
        d = G.order_activate_row_map
        for index, k in enumerate(d):
            row = index
            try:
                p = G.order_activate[k]
            except KeyError:
                d.remove(k)
                continue
            self.activate_order_table.insertRow(row)
            for i, col in enumerate(activate_order_table_column):
                if col != 'operator':
                    self.activate_order_table.setItem(row, i, QTableWidgetItem(str(p[col])))
                else:
                    btn = QPushButton('撤单')
                    self.activate_order_table.setCellWidget(row, i, btn)

    def fill_trade_table(self):
        d = G.order_trade_row_map
        for index, k in enumerate(d):
            row = index
            try:
                p = G.order_trade[k]
            except KeyError:
                d.remove(k)
                continue
            self.trade_table.insertRow(row)
            for i, col in enumerate(trade_table_column):
                self.trade_table.setItem(row, i, QTableWidgetItem(str(p[col])))

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
    def set_tick_slot(self, tick: dict):
        local_symbol = tick['local_symbol']
        if local_symbol != G.choice_local_symbol:
            return
        for k, v in tick_zn.items():
            if k not in G.order_tick_row_map:
                row = self.tick_row
                G.order_tick_row_map.append(k)
                self.tick_table.insertRow(row)
                self.tick_row += 1
            else:
                row = G.order_tick_row_map.index(k)
            self.tick_table.setItem(row, 0, QTableWidgetItem(v))
            self.tick_table.setItem(row, 1, QTableWidgetItem(str(tick[k])))
        # print("tick", tick)

    @Slot(list)
    def set_position_slot(self, positions: list):
        self.position_table.clearContents()
        # print("positions", positions)
        for p in positions:
            local_position_id = p["local_symbol"] + p["direction"]
            if local_position_id not in G.order_position_row_map:
                row = self.position_row
                G.order_position_row_map.append(local_position_id)
                self.position_table.insertRow(row)
                self.position_row += 1
            else:
                row = G.order_position_row_map.index(local_position_id)
            for i, col in enumerate(position_table_column):
                if col != 'operator':
                    self.position_table.setItem(row, i, QTableWidgetItem(str(p[col])))
                else:
                    btn = QPushButton('平仓')
                    btn.clicked.connect(self.close_position)
                    self.position_table.setCellWidget(row, i, btn)

    @Slot(list)
    def set_activate_slot(self, active_orders: list):
        self.activate_order_table.clearContents()
        print("active_orders", active_orders)
        for o in active_orders:
            local_order_id = o['local_order_id']
            if local_order_id not in G.order_activate_row_map:  # 不在table
                row = self.activate_row
                G.order_activate_row_map.append(local_order_id)
                self.activate_order_table.insertRow(row)
                self.activate_row += 1
            else:  # in table
                row = G.order_activate_row_map.index(local_order_id)
            for i, col in enumerate(activate_order_table_column):  # 渲染
                if col != 'operator':
                    self.activate_order_table.setItem(row, i, QTableWidgetItem(str(o[col])))
                else:
                    btn = QPushButton('撤单')
                    btn.clicked.connect(self.cancel_order)
                    self.activate_order_table.setCellWidget(row, i, btn)

    @Slot(list)
    def set_order_slot(self, orders: list):
        self.order_table.clearContents()
        print("orders", orders)
        for o in orders:
            local_order_id = o['local_order_id']
            if local_order_id not in G.order_order_row_map:
                row = self.order_row
                G.order_order_row_map.append(local_order_id)
                self.order_table.insertRow(row)
                self.order_row += 1
            else:
                row = G.order_order_row_map.index(local_order_id)
            for i, col in enumerate(order_table_column):
                self.order_table.setItem(row, i, QTableWidgetItem(str(o[col])))

    @Slot(list)
    def set_trade_slot(self, trades: list):
        self.trade_table.clearContents()
        print("trades", trades)
        for t in trades:
            local_trade_id = t['local_trade_id']
            if local_trade_id not in G.order_trade_row_map:
                row = self.trade_row
                G.order_trade_row_map.append(local_trade_id)
                self.trade_table.insertRow(row)
                self.trade_row += 1
            else:
                row = G.order_trade_row_map.index(local_trade_id)
            for i, col in enumerate(trade_table_column):
                self.trade_table.setItem(row, i, QTableWidgetItem(str(t[col])))
