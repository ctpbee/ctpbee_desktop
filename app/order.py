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
from app.tip import TipDialog
from app.ui import qss
from app.ui.ui_order import Ui_Order

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
        self.setStyleSheet(qss)
        self.setWindowTitle("下单")
        #
        self.position_table.setEditTriggers(QTableWidget.NoEditTriggers)  # 单元格不可编辑
        self.activate_order_table.setEditTriggers(QTableWidget.NoEditTriggers)  # 单元格不可编辑
        self.order_table.setEditTriggers(QTableWidget.NoEditTriggers)  # 单元格不可编辑
        self.trade_table.setEditTriggers(QTableWidget.NoEditTriggers)  # 单元格不可编辑
        self.position_table.verticalHeader().setVisible(False)  # 垂直表头不可见
        self.activate_order_table.verticalHeader().setVisible(False)  # 垂直表头不可见
        self.order_table.verticalHeader().setVisible(False)  # 垂直表头不可见
        self.trade_table.verticalHeader().setVisible(False)  # 垂直表头不可见
        #
        self.mainwindow = mainwindow
        self.bee_ext = mainwindow.bee_ext
        # 合约列表
        self.local_symbol_zn.setText(G.subscribes.get(G.choice_local_symbol) or "未选择")
        for local_symbol in sorted(G.subscribes):
            self.symbol_name_list.addItem(local_symbol)
        self.symbol_name_list.setCurrentText(G.choice_local_symbol or "未选择")
        if G.choice_local_symbol is None:
            self.buy_btn.setDisabled(True)
            self.short_btn.setDisabled(True)
        else:
            if G.ticks.get(G.choice_local_symbol):
                self.price.setValue(G.ticks[G.choice_local_symbol].get('last_price', 0))
        # 买多/卖空
        self.buy_btn.clicked.connect(self.buy_slot)
        self.short_btn.clicked.connect(self.short_slot)
        # 初始化table

        self.position_table.setRowCount(0)
        self.activate_order_table.setRowCount(0)
        self.order_table.setRowCount(0)
        self.trade_table.setRowCount(0)
        #
        self.order_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自适应表格宽度
        self.position_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自适应表格宽度
        self.activate_order_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自适应表格宽度
        self.trade_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自适应表格宽度

        self.activate_order_table.setColumnHidden(0, True)  # 设置order_id隐藏
        # 信号插槽
        self.mainwindow.job.order_position_signal.connect(self.set_position_slot)
        self.mainwindow.job.order_activate_signal.connect(self.set_activate_slot)
        self.mainwindow.job.order_order_signal.connect(self.set_order_slot)
        self.mainwindow.job.order_trade_signal.connect(self.set_trade_slot)
        self.mainwindow.job.account_signal.connect(self.set_account_slot)
        # 信号控制
        self.symbol_name_list.currentIndexChanged.connect(self.symbol_change_slot)  # 监听合约列表
        # 初始化
        self.fill_other()

    def symbol_change_slot(self):
        self.short_btn.setEnabled(True)
        self.buy_btn.setEnabled(True)
        symbol = self.symbol_name_list.currentText()
        if G.choice_local_symbol != symbol:
            G.choice_local_symbol = symbol
            self.local_symbol_zn.setText(G.subscribes.get(G.choice_local_symbol))
        if G.ticks.get(symbol):
            self.price.setValue(G.ticks[symbol].get('last_price', 0))

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
        """平仓"""
        row = self.position_table.currentRow()
        symbol = self.position_table.item(row, position_table_column.index('symbol')).text()
        direction = self.position_table.item(row, position_table_column.index('direction')).text()
        exchange = self.position_table.item(row, position_table_column.index('exchange')).text()
        volume = self.position_table.item(row, position_table_column.index('volume')).text()
        local_symbol = symbol + '.' + exchange
        tick = TickData(symbol=symbol, exchange=exchange_map[exchange])
        try:
            price = self.bee_ext.app.recorder.get_tick(local_symbol).last_price
        except AttributeError:
            TipDialog("未订阅此合约行情")
        else:
            try:
                if direction == "long":
                    self.bee_ext.app.action.cover(price=float(price), volume=float(volume), origin=tick)
                if direction == "short":
                    self.bee_ext.app.action.sell(price=float(price), volume=float(volume), origin=tick)
                TipDialog("平仓请求发送成功")
            except Exception as e:
                print(e)
                QMessageBox().warning(self, "提示", "平仓请求发送失败" + str(e), QMessageBox.Ok, QMessageBox.Ok)

    @Slot()
    def cancel_order(self):
        """撤单"""
        row = self.activate_order_table.currentRow()
        symbol = self.activate_order_table.item(row, activate_order_table_column.index('symbol')).text()
        exchange = self.activate_order_table.item(row, activate_order_table_column.index('exchange')).text()
        local_symbol = symbol + '.' + exchange
        order_id = self.activate_order_table.item(row, activate_order_table_column.index('order_id')).text()
        req = helper.generate_cancel_req_by_str(symbol=local_symbol, exchange=exchange, order_id=order_id)
        try:
            bee_current_app.cancel_order(req)
            TipDialog("撤单请求发送成功")
        except Exception as e:
            QMessageBox().warning(self, "提示", "撤单请求发送失败" + str(e), QMessageBox.Ok, QMessageBox.Ok)

    @Slot()
    def open_order(self, direction):
        """下单"""
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
                TipDialog("下单请求发送成功")
        except Exception as e:
            QMessageBox().warning(self, "提示", "下单请求发送失败" + str(e), QMessageBox.Ok, QMessageBox.Ok)

    @Slot()
    def buy_slot(self):
        """买多"""
        self.open_order('long')

    @Slot()
    def short_slot(self):
        """卖空"""
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

    @Slot(list)
    def set_position_slot(self, positions: list):
        self.position_table.setRowCount(0)
        barpos = self.position_table.verticalScrollBar().value()
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
        self.position_table.verticalScrollBar().setValue(barpos)

    @Slot(list)
    def set_activate_slot(self, active_orders: list):
        self.activate_order_table.setRowCount(0)
        row = 0
        barpos = self.activate_order_table.verticalScrollBar().value()
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
        self.activate_order_table.verticalScrollBar().setValue(barpos)

    @Slot(list)
    def set_order_slot(self, orders: list):
        self.order_table.setRowCount(0)
        barpos = self.order_table.verticalScrollBar().value()
        row = 0
        x = sorted(orders, key=operator.itemgetter('local_symbol'))
        for o in x:
            self.order_table.insertRow(row)
            # 渲染
            for i, col in enumerate(order_table_column):
                self.order_table.setItem(row, i, QTableWidgetItem(str(o[col])))
        self.order_table.verticalScrollBar().setValue(barpos)

    @Slot(list)
    def set_trade_slot(self, trades: list):
        self.trade_table.setRowCount(0)
        barpos = self.trade_table.verticalScrollBar().value()
        row = 0
        x = sorted(trades, key=operator.itemgetter('local_symbol'))
        for t in x:
            self.trade_table.insertRow(row)

            for i, col in enumerate(trade_table_column):
                self.trade_table.setItem(row, i, QTableWidgetItem(str(t[col])))
        self.trade_table.verticalScrollBar().setValue(barpos)

    def closeEvent(self, arg__1):
        self.mainwindow.order_widget = None
        arg__1.accept()
