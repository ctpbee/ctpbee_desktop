import webbrowser

from PySide2.QtCore import QThreadPool, QRunnable, QObject, Signal, Slot
from PySide2.QtWidgets import QWidget, QFileDialog, QMessageBox, QVBoxLayout, QHBoxLayout, QLabel, QPushButton

from app.ui import backtrack_qss
from app.ui.ui_backtrack import Ui_Form
from app.lib.global_var import G
from ctpbee import Vessel, LooperApi


class BacktrackrWorker(QRunnable):
    def __init__(self, name, sig, data, strategy):
        super(self.__class__, self).__init__()
        self.name = name
        self.sig = sig
        self.data = data
        self.strategy = strategy

    def run(self):
        vessel = Vessel()
        vessel.add_data(self.data)
        vessel.add_strategy(self.strategy)
        vessel.set_params({"looper":
                               {"initial_capital": 100000,
                                "commission": 0.005,
                                "deal_pattern": "price",
                                "size_map": {"ag1912.SHFE": 15},
                                "today_commission": 0.005,
                                "yesterday_commission": 0.02,
                                "close_commission": 0.005,
                                "slippage_sell": 0,
                                "slippage_cover": 0,
                                "slippage_buy": 0,
                                "slippage_short": 0,
                                "close_pattern": "yesterday",
                                },
                           "strategy": {}
                           })
        vessel.run()
        result = vessel.get_result(report=True)

        self.sig.emit({"name": self.name, "url": result})


class BacktrackSig(QObject):
    report_sig = Signal(dict)

    def __init__(self):
        super(self.__class__, self).__init__()


class BacktrackWidget(QWidget, Ui_Form):
    def __init__(self, mainwindow):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(backtrack_qss)
        self.thread_pool = QThreadPool()
        self.init_ui()
        self.sig = BacktrackSig()
        self.sig.report_sig.connect(self.report_slot)
        # btn
        self.add_data_btn.clicked.connect(self.add_data_slot)
        self.add_backtrack_btn.clicked.connect(self.add_backtrack_slot)
        self.run_btn.clicked.connect(self.run_slot)
        # var
        self.counter = 1
        self.name = None
        self.ext = None
        self.data = None

    def init_ui(self):
        for local_symbol, _ in G.all_contracts.items():
            self.local_symbol_box.addItem(local_symbol)

    def add_data_slot(self):
        filename, _ = QFileDialog.getOpenFileName(self, '选择数据文件', '', 'Text files(*.json);;Text files(*.csv)')

    def add_backtrack_slot(self):
        filename, _ = QFileDialog.getOpenFileName(self, '选择回测API', '', 'Python files(*.py)')
        from ctpbee import dynamic_loading_api
        try:
            with open(filename, 'r') as fp:
                self.ext = dynamic_loading_api(fp)
        except Exception as e:
            QMessageBox.information(self, '提示', str(e))

    def run_slot(self):
        symbol = self.local_symbol_box.currentText()
        self.name = f"回测{self.counter}_{symbol}"
        self.thread_pool.start(BacktrackrWorker(sig=self.sig, data=self.data, strategy=self.ext))
        self.counter += 1

    @Slot(dict)
    def report_slot(self, res: dict):
        h_layout = QHBoxLayout(self)
        label = QLabel(self)
        label.setText(res['name'])
        open_btn = QsPushButton(self, res['url'])
        h_layout.addWidget(label)
        h_layout.addWidget(open_btn)
        self.res_layout.addLayout(h_layout)


class QsPushButton(QPushButton):
    def __init__(self, url):
        super(self.__class__, self).__init__()
        self.url = url

    def open_url(self):
        try:
            webbrowser.get('chrome').open_new_tab(self.url)
        except Exception as e:
            webbrowser.open_new_tab(self.url)
