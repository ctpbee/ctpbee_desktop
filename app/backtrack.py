import json
import webbrowser
from datetime import datetime

import pandas
from PySide2.QtCore import QThreadPool, QRunnable, QObject, Signal, Slot, QRegExp
from PySide2.QtGui import QRegExpValidator
from PySide2.QtWidgets import QWidget, QFileDialog, QMessageBox, QVBoxLayout, QHBoxLayout, QLabel, QPushButton

from app.tip import TipDialog
from app.ui import backtrack_qss
from app.ui.ui_backtrack import Ui_Form
from app.lib.global_var import G
from ctpbee import Vessel, LooperApi


class BacktrackrWorker(QRunnable):
    def __init__(self, name, sig, data, strategy, params):
        super(self.__class__, self).__init__()
        self.name = name
        self.sig = sig
        self.data = data
        self.strategy = strategy
        self.params = params

    def run(self):
        try:
            vessel = Vessel()
            vessel.add_data(self.data)
            vessel.add_strategy(self.strategy)
            vessel.set_params({"looper": self.params,
                               "strategy": {}
                               })
            vessel.run()
            result = vessel.get_result(report=True)
            error = ""
        except Exception as e:
            result = ""
            error = str(e)
        self.sig.emit({"name": self.name, "url": result, "error": error})


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
        # validate
        rx = QRegExp(r"[0-9]{1,7}\.[0-9]{1,6}")
        self.commission.setValidator(QRegExpValidator(rx, self))
        self.close_commission.setValidator(QRegExpValidator(rx, self))
        self.yesterday_commission.setValidator(QRegExpValidator(rx, self))
        self.today_commission.setValidator(QRegExpValidator(rx, self))

        # btn
        self.add_data_btn.clicked.connect(self.add_data_slot)
        self.add_backtrack_btn.clicked.connect(self.add_backtrack_slot)
        self.run_btn.clicked.connect(self.run_slot)
        # var
        self.counter = 1
        self.name = None
        self.ext = None
        self.data = None
        #

    def init_ui(self):
        for local_symbol, _ in G.all_contracts.items():
            self.local_symbol_box.addItem(local_symbol)

    def add_data_slot(self):
        filetypes = ["Text files(*.json)", "Text files(*.csv)"]
        filename, ft = QFileDialog.getOpenFileName(self, '选择数据文件', '', ";;".join(filetypes))
        if not filename:
            return
        self.data_label.setText(filename)
        i = filetypes.index(ft)

        def resolve_json(data):
            data['datetime'] = datetime.strptime(data['datetime'], "%Y-%m-%d %H:%M:%S.%f")
            return data

        if i == 0:  # json
            try:
                with open(filename, 'r') as fp:
                    data = json.load(fp)
                    self.data = list(map(resolve_json, data['data']))
            except Exception as e:
                QMessageBox.information(self, '提示', str(e))
                return
        elif i == 1:  # csv
            try:
                with open(filename, 'r') as fp:
                    data = pandas.read_csv(fp)
                    self.data = data.to_dict("index")
            except Exception as e:
                QMessageBox.information(self, '提示', str(e))
                return
        TipDialog("传入数据成功")

    def add_backtrack_slot(self):
        filename, _ = QFileDialog.getOpenFileName(self, '选择回测API', '', 'Python files(*.py)')
        if not filename:
            return
        self.backtrack_label.setText(filename)
        from ctpbee import dynamic_loading_api
        try:
            with open(filename, 'r') as fp:
                self.ext = dynamic_loading_api(fp)
                if not isinstance(self.ext, LooperApi):
                    raise Exception(f"你的回测API类型出错,期望LooperApi,你的{type(self.ext)}")
        except Exception as e:
            QMessageBox.information(self, '提示', str(e))
            return
        TipDialog("传入回测API成功")

    def get_params(self):
        par = {"initial_capital": float(self.initial_capital.text()),
               "size_map": {self.local_symbol_box.currentText(): int(self.size_map.text())},
               "deal_pattern": self.deal_pattern.currentText(),
               "close_pattern": self.close_pattern.currentText(),
               "commission": float(self.commission.text()),
               "today_commission": float(self.today_commission.text()),
               "yesterday_commission": float(self.yesterday_commission.text()),
               "close_commission": float(self.close_commission.text()),
               "slippage_sell": float(self.slippage_sell.text()),
               "slippage_cover": float(self.slippage_cover.text()),
               "slippage_buy": float(self.slippage_buy.text()),
               "slippage_short": float(self.slippage_short.text()),
               }
        return par

    def run_slot(self):
        if not self.data:
            TipDialog("还未传入数据")
            return
        if not self.ext:
            TipDialog("还未传入回测API")
            return
        symbol = self.local_symbol_box.currentText()
        self.name = f"回测{self.counter}_{symbol}"
        self.thread_pool.start(
            BacktrackrWorker(name=self.name, sig=self.sig.report_sig, data=self.data, strategy=self.ext,
                             params=self.get_params()))
        self.counter += 1

    @Slot(dict)
    def report_slot(self, res: dict):
        if res['error']:
            QMessageBox.information(self, '错误', res['error'])
        else:
            h_layout = QHBoxLayout(self)
            open_btn = QsPushButton(self, res['url'])
            open_btn.setText(res['name'])
            h_layout.addWidget(open_btn)
            self.res_layout.insertLayout(self.counter-1, h_layout)


class QsPushButton(QPushButton):
    def __init__(self, parent, url):
        super(self.__class__, self).__init__(parent)
        self.url = url
        self.clicked.connect(self.open_url)

    def open_url(self):
        try:
            webbrowser.get('chrome').open_new_tab(self.url)
        except Exception as e:
            webbrowser.open_new_tab(self.url)
