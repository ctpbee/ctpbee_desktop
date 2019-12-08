import json
import os
import sys
from PySide2.QtCore import Signal, QObject, Slot, Qt, QSize, QThread
from PySide2.QtGui import QCloseEvent, QIcon, QPixmap, QBitmap, QPainter
from PySide2.QtWidgets import QMainWindow, QAction, QApplication, QProgressBar, QMessageBox, QLabel, QMenu, \
    QSystemTrayIcon

from app.lib.global_var import G
from app.lib.helper import Job, KInterfaceObject, RecordObject
from app.ui.ui_mainwindow import Ui_MainWindow
from ctpbee import CtpbeeApi
from app.account import AccountWidget
from app.market import MarketWidget
from app.order import OrderWidget
from app.strategy import StrategyWidget
from app.config import ConfigDialog
from ctpbee.constant import *
from ctpbee.event_engine.engine import EVENT_TIMER
from ctpbee import current_app
from app.log import LogDialog
from app.home import HomeWidget

qss = """
QMainWindow{
background:#ffffff;
color:#000000;
margin:0px;
}


QMenuBar,QStatusBar{
background:#1b89ca;
color:#000000;
}

QProgressBar {
    border-radius: 5px;
    text-align: center;
}

QProgressBar::chunk {
    width: 2px;
    margin: 0.5px;
    background-color: #1B89CA;
}

QMenuBar::item:selected {
    color: #1b89ca;
    background: #ffffff
}

QPushButton{
    padding:10px;
    background: #ffffff

}

QPushButton:hover{
    background:#1b89ca;
}"""


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("ctpbee桌面端")
        # self.setWindowFlag(Qt.FramelessWindowHint)  # 去边框 可能会导致闪屏异常
        self.setStyleSheet(qss)
        #
        G.mainwindow = self
        self.exit_ = False
        self.job = Job()
        self.kline_job = KInterfaceObject()
        self.record_job = RecordObject()
        self.bee_ext = None
        self.log_dialog = None
        self.cfg_dialog = None
        self.tray_init()
        # designer 不支持将action加入菜单栏 只能手撸
        for a in ["首页", "账户", "行情", "下单", "策略", "回测", "配置", "日志"]:
            self.account_action = QAction(self)
            self.account_action.setText(a)
            self.menubar.addAction(self.account_action)
        self.menubar.triggered[QAction].connect(self.menu_triggered)
        ##
        self.status_msg = QLabel("实时信息")
        self.market_msg = QLabel("最新行情")
        self.progressbar = QProgressBar()
        self.progressbar.setFixedHeight(10)
        self.progressbar.setRange(0, 0)
        self.progressbar.setTextVisible(False)
        self.statusbar.addPermanentWidget(self.progressbar, stretch=1)
        self.statusbar.addPermanentWidget(self.status_msg, stretch=5)
        self.statusbar.addPermanentWidget(self.market_msg, stretch=5)

    def sign_in_success(self):
        self.bee_ext = CtpbeeApi('default_setting', current_app)
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
        # 默认打开
        self.widget = HomeWidget(self)
        self.setCentralWidget(self.widget)

    def submask(self):
        self.bmp = QBitmap(self.size())
        self.bmp.fill()
        self.p = QPainter(self.bmp)
        self.p.setPen(Qt.black)
        self.p.setBrush(Qt.black)
        self.p.drawRoundedRect(self.bmp.rect(), 10, 10)
        self.setMask(self.bmp)

    def menu_triggered(self, q):
        action = q.text()
        if action == "首页":
            self.home_handle()
        elif action == "账户":
            self.account_handle()
        elif action == "回测":
            return
        elif action == "行情":
            self.market_handle()
        elif action == "策略":
            self.strategy_handle()
        elif action == "配置":
            self.config_handle()
        elif action == "下单":
            self.order_handle()
        elif action == "注销":
            self.logout_handle()
        elif action == '日志':
            self.log_handle()

    def home_handle(self):
        self.widget = HomeWidget(self)
        self.setCentralWidget(self.widget)

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
        if self.cfg_dialog is None:
            self.cfg_dialog = ConfigDialog(self)
            self.cfg_dialog.show()
        else:
            self.cfg_dialog.raise_()

    def order_handle(self):
        if not G.choice_local_symbol:
            replay = QMessageBox.information(self, "提示", "请在[行情]先订阅或选择一个合约", QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.widget = OrderWidget(self)
            self.setCentralWidget(self.widget)

    def log_handle(self):
        if self.log_dialog is None:
            self.log_dialog = LogDialog(self)
            self.log_dialog.show()
        else:
            self.log_dialog.raise_()

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
        self.record_job.sig_bar_record.emit(bar.local_symbol, info)

    def on_order(self, ext, order: OrderData) -> None:
        active_orders = []
        for order1 in self.bee_ext.app.recorder.get_all_active_orders():
            o1 = order1._to_dict()
            active_orders.append(o1)
        self.job.order_activate_signal.emit(active_orders)

        orders = []
        for order2 in self.bee_ext.app.recorder.get_all_orders():
            o2 = order2._to_dict()
            orders.append(o2)
        self.job.order_order_signal.emit(orders)

    def on_realtime(*args):
        self = args[0]
        all_positions = self.bee_ext.app.recorder.get_all_positions()
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
        self.job.order_trade_signal.emit(trades)

    def on_init(self, ext, init):
        pass

    def tray_init(self):
        icon = QIcon(":menu/images/bee_temp_grey.png")
        menu = QMenu()
        openAction = menu.addAction("🍯 界面")
        exitAction = menu.addAction("❎ 退出")
        openAction.triggered.connect(self.show)
        exitAction.triggered.connect(self.quit)
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(icon)
        self.tray.setContextMenu(menu)
        self.tray.activated.connect(self.iconActivated)
        self.tray.show()
        self.tray.setToolTip("ctpbee桌面端")

    def quit(self):
        self.exit_ = True
        self.close()

    def iconActivated(self, reason):
        if reason in (QSystemTrayIcon.Trigger, QSystemTrayIcon.DoubleClick):
            if self.isHidden():
                self.show()
            else:
                self.hide()

    def closeEvent(self, event: QCloseEvent):
        if self.exit_:
            event.accept()
            self.tray.hide()
            try:
                current_app.release()
            except:
                pass
            if self.cfg_dialog:
                self.cfg_dialog.close()
            if self.log_dialog:
                self.log_dialog.close()
        else:
            self.tray.showMessage("ctpbee", "以最小化隐藏在托盘", msecs=2)
            self.hide()
            event.ignore()

    # def mousePressEvent(self, event):
    #     if event.button() == Qt.LeftButton:
    #         self.m_flag = True
    #         self.r_flag = False
    #         self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
    #         event.accept()
    #
    # def mouseReleaseEvent(self, event):
    #     self.r_flag = True
    #     event.accept()
    #
    # def mouseMoveEvent(self, QMouseEvent):
    #     try:
    #         if Qt.LeftButton and self.m_flag and not self.r_flag:
    #             self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
    #             QMouseEvent.accept()
    #     except:
    #         pass
    #
    # def mouseDoubleClickEvent(self, event):
    #     if self.isFullScreen():
    #         self.showNormal()
    #     else:
    #         self.showFullScreen()
    #     event.accept()
