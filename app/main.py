import json
import os
import sys

from PySide2.QtCore import Signal, QObject, Slot
from PySide2.QtGui import QCloseEvent, QIcon, QPixmap
from PySide2.QtWidgets import QMainWindow, QAction, QApplication, QProgressBar, QMessageBox, QLabel, QMenu

from app.lib.global_var import G
from app.ui.ui_mainwindow import Ui_MainWindow
from ctpbee import CtpbeeApi
from app.account import AccountWidget
from app.market import MarketWidget
from app.order import OrderWidget
from app.strategy import StrategyWidget
from app.config import ConfigDialog
from app.about_us import AboutUsDialog
from ctpbee.constant import *
from ctpbee.event_engine.engine import EVENT_TIMER
from ctpbee import current_app
from app.lib.get_path import path


class Job(QObject):
    account_signal = Signal(dict)
    market_signal = Signal(dict)
    order_tick_signal = Signal(dict)
    order_position_signal = Signal(list)
    order_activate_signal = Signal(list)
    order_order_signal = Signal(list)
    order_trade_signal = Signal(list)
    order_log_signal = Signal(str)

    def __init__(self):
        super(self.__class__, self).__init__()


class KInterfaceObject(QObject):
    qt_to_js = Signal(str)  # channel only str
    js_to_qt = Signal(str)
    transfer_signal = Signal(dict)

    def __init__(self):
        super(self.__class__, self).__init__()

    @Slot(result=str)
    def get_history_data(self):
        """js传数据通过调用此函数"""
        try:
            file_path = path + f"/{str(G.choice_local_symbol)}.json"
            with open(file_path, 'r') as f:
                data = f.read()
        except:
            data = json.dumps({G.choice_local_symbol: []})
        return data


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("ctpbee桌面端")
        G.mainwindow = self
        self.job = Job()
        self.kline_job = KInterfaceObject()
        self.bee_ext = None

        # designer 不支持将action加入菜单栏 只能手撸
        for a in ["账户", "行情", "下单", "策略", "回测", "配置"]:
            self.account_action = QAction(self)
            self.account_action.setText(a)
            self.menubar.addAction(self.account_action)
        self.menubar.triggered[QAction].connect(self.menu_triggered)
        #
        self.status_msg = QLabel("实时信息")
        self.market_msg = QLabel("最新行情")
        self.progressbar = QProgressBar()
        self.progressbar.setFixedHeight(10)
        self.progressbar.setRange(0, 0)
        self.progressbar.setTextVisible(False)
        self.statusbar.addPermanentWidget(self.progressbar, stretch=1)
        self.statusbar.addPermanentWidget(self.status_msg, stretch=5)
        self.statusbar.addPermanentWidget(self.market_msg, stretch=5)

    def sign_in_success(self, bee_app):
        self.bee_ext = CtpbeeApi('default_setting', bee_app)
        self.bee_ext.map[EVENT_ACCOUNT] = self.on_account
        self.bee_ext.map[EVENT_CONTRACT] = self.on_contract
        self.bee_ext.map[EVENT_BAR] = self.on_bar
        self.bee_ext.map[EVENT_ORDER] = self.on_order
        self.bee_ext.map[EVENT_POSITION] = self.on_position
        self.bee_ext.map[EVENT_TICK] = self.on_tick
        self.bee_ext.map[EVENT_SHARED] = self.on_shared
        self.bee_ext.map[EVENT_TRADE] = self.on_trade
        self.bee_ext.map[EVENT_TIMER] = self.on_realtime
        #
        contracts = {contract.local_symbol: contract.name for contract in
                     self.bee_ext.app.recorder.get_all_contracts()}
        G.all_contracts = contracts
        # 默认打开account
        self.widget = AccountWidget(self)
        self.setCentralWidget(self.widget)

    def menu_triggered(self, q):
        action = q.text()
        if action == "账户":
            self.account_handle()
        if action == "回测":
            QMessageBox.information(self, "提示", "正在加班赶...", QMessageBox.Ok, QMessageBox.Ok)
        if action == "行情":
            self.market_handle()
        if action == "策略":
            self.strategy_handle()
        if action == "配置":
            self.config_handle()
        if action == "下单":
            self.order_handle()
        if action == "注销":
            self.logout_handle()
        if action == '关于':
            self.about_us_handle()

    def strategy_handle(self):
        self.widget = StrategyWidget(self)
        self.setCentralWidget(self.widget)

    def account_handle(self):
        self.widget = AccountWidget(self)
        self.setCentralWidget(self.widget)

    def market_handle(self):
        self.widget = MarketWidget(self)
        self.setCentralWidget(self.widget)

    def config_handle(self):
        self.cfg_dialog = ConfigDialog(self)
        self.cfg_dialog.show()

    def order_handle(self):
        if not G.choice_local_symbol:
            QMessageBox.information(self, "提示", "请在[行情]先订阅或选择一个合约", QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.widget = OrderWidget(self)
            self.setCentralWidget(self.widget)

    def about_us_handle(self):
        about = AboutUsDialog()
        about.exec_()

    def on_account(self, ext, account: AccountData) -> None:
        account = account._to_dict()
        G.account = account
        self.job.account_signal.emit(account)

    def on_contract(self, ext, contract: ContractData):
        pass

    def on_bar(self, ext, bar: BarData) -> None:
        timestamp = round(bar.datetime.timestamp() * 1000)
        info = [timestamp, bar.open_price, bar.high_price, bar.low_price,
                bar.close_price, bar.volume]
        if bar.local_symbol == G.choice_local_symbol:
            self.kline_job.transfer_signal.emit({bar.local_symbol: info})
        # 存入文件
        file_path = path + f"/{str(bar.local_symbol)}.json"
        old = {}
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                data = f.read()
                if data:
                    old = json.loads(data)
        with open(file_path, 'w') as f:
            if not old.get(bar.local_symbol):
                old.setdefault(bar.local_symbol, []).append(info)
            else:
                old[bar.local_symbol].append(info)
            json.dump(old, f)

    def on_order(self, ext, order: OrderData) -> None:
        active_orders = []
        for order1 in self.bee_ext.app.recorder.get_all_active_orders():
            o1 = order1._to_dict()
            active_orders.append(o1)
            G.order_activate[o1['local_order_id']] = o1
        self.job.order_activate_signal.emit(active_orders)

        orders = []
        for order2 in self.bee_ext.app.recorder.get_all_orders():
            o2 = order2._to_dict()
            orders.append(o2)
            G.order_order[o2['local_order_id']] = o2
        self.job.order_order_signal.emit(orders)

    def on_realtime(*args):

        self = args[0]
        all_positions = self.bee_ext.app.recorder.get_all_positions()
        for p in all_positions:
            mark = p["local_symbol"] + p["direction"]
            G.order_position[mark] = p
        self.job.order_position_signal.emit(all_positions)

    def on_position(self, ext, position: PositionData) -> None:
        pass

    def on_tick(self, ext, tick: TickData) -> None:
        self.market_msg.setText(f"最新行情：{tick.name}   {tick.last_price}")
        tick = tick._to_dict()
        local_symbol = tick['local_symbol']
        G.market_tick[local_symbol] = tick

        self.job.market_signal.emit(tick)
        self.job.order_tick_signal.emit(tick)

    def on_shared(self, ext, shared: SharedData) -> None:
        pass

    def on_trade(self, ext, trade: TradeData) -> None:
        trades = []
        for trade in self.bee_ext.app.recorder.get_all_trades():
            t = trade._to_dict()
            trades.append(t)
            G.order_trade[t['local_trade_id']] = t
        self.job.order_trade_signal.emit(trades)

    def on_init(self, ext, init):
        pass

    def closeEvent(self, event: QCloseEvent):

        msg = QMessageBox(QMessageBox.Question, "提示", "是否要退出程序？",
                          QMessageBox.NoButton,
                          self)
        yr_btn = msg.addButton(self.tr("确定"), QMessageBox.YesRole)
        msg.addButton(self.tr("取消"), QMessageBox.NoRole)
        msg.exec_()
        if msg.clickedButton() == yr_btn:
            try:
                current_app.release()
            except:
                pass
            event.accept()
        else:
            event.ignore()
