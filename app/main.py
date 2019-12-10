import json
from PySide2 import QtGui
from PySide2.QtCore import QThread, Qt, QPropertyAnimation
from PySide2.QtGui import QCloseEvent, QIcon, QKeySequence
from PySide2.QtWidgets import QMainWindow, QProgressBar, QMessageBox, QLabel, QMenu, \
    QSystemTrayIcon, QShortcut

from app.backtrack import BacktrackWidget
from app.lib.global_var import G
from app.lib.helper import Job, KInterfaceObject, RecordWorker
from app.tip import TipDialog
from app.ui import main_qss
from app.ui.ui_mainwindow import Ui_MainWindow
from ctpbee import CtpbeeApi
from app.market import MarketWidget
from app.order import OrderWidget
from app.strategy import StrategyWidget
from app.config import ConfigDialog
from ctpbee.constant import *
from ctpbee.event_engine.engine import EVENT_TIMER
from ctpbee import current_app
from app.log import LogDialog
from app.home import HomeWidget
from app.k_line import KlineWidget


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("ctpbee桌面端")
        # self.setWindowFlag(Qt.FramelessWindowHint)  # 去边框 可能会导致闪屏异常
        self.setStyleSheet(main_qss)
        self.animation = QPropertyAnimation(self, b'windowOpacity')
        self.animation.stop()
        self.animation.setDuration(500)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()
        #
        G.mainwindow = self
        self.exit_ = False
        self._page_history = []
        self._page_maxsize = 10
        self.job = Job()
        self.kline_job = KInterfaceObject()
        self.record_work = RecordWorker()
        self.r_thread = QThread()
        self.record_work.moveToThread(self.r_thread)
        self.r_thread.started.connect(self.record_work.record)
        self.r_thread.start()
        self.bee_ext = None
        self.tray_init()
        self.shortcut_init()
        ##
        self.status_msg = QLabel("实时信息")
        self.market_msg = QLabel("最新行情")
        self.statusbar.addPermanentWidget(self.status_msg, stretch=5)
        self.statusbar.addPermanentWidget(self.market_msg, stretch=5)
        # btn
        self.pre_page_btn.clicked.connect(self.pre_page_slot)
        self.home_btn.clicked.connect(self.home_handle)
        self.market_btn.clicked.connect(self.market_handle)
        self.order_btn.clicked.connect(self.order_handle)
        self.strategy_btn.clicked.connect(self.strategy_handle)
        self.setting_btn.clicked.connect(self.config_handle)
        self.log_btn.clicked.connect(self.log_handle)
        self.order_btn.clicked.connect(self.order_handle)
        self.backtrack_btn.clicked.connect(self.backtrack_handle)
        self.kline_btn.clicked.connect(self.kline_handle)
        #
        self.menuBar.triggered.connect(self.menu_triggered)
        # widgets
        self.map_ = []
        self.home_widget = None
        self.strategy_widget = None
        self.account_widget = None
        self.market_widget = None
        self.order_widget = None
        self.kline_widget = None
        self.log_dialog = None
        self.cfg_dialog = None
        self.backtrack_widget = None

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
        self.home_handle()

    def menu_triggered(self, q):
        q = q.text()
        if q == "退出应用":
            self.quit()

    @property
    def page_history(self):
        return self._page_history

    @page_history.setter
    def page_history(self, val):
        if len(self._page_history) == self._page_maxsize:  # 达到最大容量
            self._page_history.pop(0)  # 弹出第一项
        self._page_history.append(val)

    def pre_page_slot(self):
        try:
            i = self.page_history.pop()
            while i == self.stackedWidget.currentIndex():
                i = self.page_history.pop()
            self.stackedWidget.setCurrentIndex(i)
        except IndexError:
            TipDialog("到底啦~")

    def shortcut_init(self):
        sc = G.config.shortcut
        for name, sho in sc.items():
            if sho == '--':
                continue
            temp = QShortcut(QKeySequence(self.tr(sho)), self)
            temp.activated.connect(getattr(self, f"{name}_handle"))
            setattr(self, f"{name}_sc", temp)

    def update_shortcut(self):
        sc = G.config.shortcut
        for name, sho in sc.items():
            getattr(self, f"{name}_sc").setKey(QKeySequence(self.tr(sho)))

    def page_map(self, w):
        name = w.__class__.__name__
        if name not in self.map_:
            self.map_.append(name)
        i = self.map_.index(name)
        self.page_history = i
        return i

    def home_handle(self):
        if self.home_widget is None:
            self.home_widget = HomeWidget(self)
            self.stackedWidget.addWidget(self.home_widget)
        self.stackedWidget.setCurrentIndex(self.page_map(self.home_widget))

    def strategy_handle(self):
        if self.strategy_widget is None:
            self.strategy_widget = StrategyWidget(self)
            self.stackedWidget.addWidget(self.strategy_widget)
        self.stackedWidget.setCurrentIndex(self.page_map(self.strategy_widget))

    def backtrack_handle(self):
        if self.backtrack_widget is None:
            self.backtrack_widget = BacktrackWidget(self)
            self.stackedWidget.addWidget(self.backtrack_widget)
        self.stackedWidget.setCurrentIndex(self.page_map(self.backtrack_widget))

    def market_handle(self):
        if self.market_widget is None:
            self.market_widget = MarketWidget(self)
            self.stackedWidget.addWidget(self.market_widget)
        self.stackedWidget.setCurrentIndex(self.page_map(self.market_widget))
        G.current_page = "market"

    def kline_handle(self):
        if self.kline_widget is None:
            self.kline_widget = KlineWidget(self)
            self.stackedWidget.addWidget(self.kline_widget)
        self.stackedWidget.setCurrentIndex(self.page_map(self.kline_widget))
        self.kline_widget.k_line_reload()

    def order_handle(self):
        if self.order_widget is None:
            self.order_widget = OrderWidget(self)
        self.order_widget.show()
        self.order_widget.raise_()

    def config_handle(self):
        if self.cfg_dialog is None:
            self.cfg_dialog = ConfigDialog(self)
        self.cfg_dialog.show()
        self.cfg_dialog.raise_()

    def log_handle(self):
        if self.log_dialog is None:
            self.log_dialog = LogDialog(self)
        self.log_dialog.show()
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
            data = {bar.local_symbol: info}
            self.kline_job.qt_to_js.emit(json.dumps(data))
        # 存入文件
        G.tick_queue.put([bar.local_symbol, info])

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
        if G.current_page == "market":
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

    def closeEvent(self, event: QCloseEvent):
        if self.exit_:
            G.pool_done = True
            self.tray.deleteLater()
            try:
                for k, v in current_app.extensions.items():
                    current_app.suspend_extension(k)
                current_app.release()
            except:
                pass
            if self.cfg_dialog:
                self.cfg_dialog.close()
            if self.log_dialog:
                self.log_dialog.close()
            if self.order_widget:
                self.order_widget.close()
            event.accept()
        else:
            self.tray.showMessage("ctpbee", "以最小化隐藏在托盘", msecs=1)
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
