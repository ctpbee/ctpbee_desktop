import json
import os
import webbrowser
from datetime import datetime

import pandas
from PySide2.QtCore import QThreadPool, QRunnable, QObject, Signal, Slot, QRegExp, Qt
from PySide2.QtGui import QRegExpValidator
from PySide2.QtWidgets import QWidget, QFileDialog, QMessageBox, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, \
    QHeaderView, QTableWidgetItem, QMenu

from app.tip import TipDialog
from app.ui import qss
from app.ui.ui_backtrack import Ui_Form
from app.lib.global_var import G
from ctpbee import Vessel, LooperApi
from ctpbee import dynamic_loading_api


class BacktrackrWorker(QRunnable):
    def __init__(self, name, sig, data, strategy, params):
        super(self.__class__, self).__init__()
        self.name = name
        self.sig = sig
        self.data = data
        self.strategy = strategy
        self.params = params

    def run(self):
        # try:
        vessel = Vessel()
        for i in self.data:
            vessel.add_data(i)
        for i in self.strategy:
            vessel.add_strategy(i)
        vessel.set_params({"looper": self.params,
                           "strategy": {}
                           })
        vessel.run()
        result = vessel.get_result(report=True)
        error = ""
        # except Exception as e:
        #     result = ""
        #     error = str(e)
        self.sig.emit({"name": self.name,
                       "url": result,
                       "error": error,
                       })


class BacktrackSig(QObject):
    report_sig = Signal(dict)

    def __init__(self):
        super(self.__class__, self).__init__()


class BacktrackWidget(QWidget, Ui_Form):
    def __init__(self, mainwindow):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(qss)
        self.thread_pool = QThreadPool()
        self.init_ui()
        self.sig = BacktrackSig()
        self.sig.report_sig.connect(self.report_slot)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setVisible(False)  # 垂直表头不可见
        self.size_map_table.verticalHeader().setVisible(False)  # 垂直表头不可见
        self.tableWidget.hide()
        # validate
        rx = QRegExp(r"[0-9]{1,7}\.[0-9]{1,6}")
        self.initial_capital.setValidator(QRegExpValidator(rx, self))
        self.commission.setValidator(QRegExpValidator(rx, self))
        self.close_commission.setValidator(QRegExpValidator(rx, self))
        self.yesterday_commission.setValidator(QRegExpValidator(rx, self))
        self.today_commission.setValidator(QRegExpValidator(rx, self))
        self.slippage_sell.setValidator(QRegExpValidator(rx, self))
        self.slippage_buy.setValidator(QRegExpValidator(rx, self))
        self.slippage_cover.setValidator(QRegExpValidator(rx, self))
        self.slippage_short.setValidator(QRegExpValidator(rx, self))
        # btn
        self.add_sm_btn.clicked.connect(self.add_sm_slot)
        self.add_data_btn.clicked.connect(self.add_data_slot)
        self.add_backtrack_btn.clicked.connect(self.add_backtrack_slot)
        self.run_btn.clicked.connect(self.run_slot)
        # 右键菜单
        self.size_map_table.setContextMenuPolicy(Qt.CustomContextMenu)  ######允许右键产生子菜单
        self.size_map_table.customContextMenuRequested.connect(self.sm_generate_menu)  ####右键菜单
        self.data_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.data_list.customContextMenuRequested.connect(self.data_generate_menu)
        self.backtrack_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.backtrack_list.customContextMenuRequested.connect(self.bt_generate_menu)
        # var
        self.counter = 1
        self.table_index = 0
        self.name = None
        self.sm_pool = dict()
        #

    def init_ui(self):
        self.params_zn()
        for local_symbol in sorted(G.all_contracts):
            self.local_symbol_box.addItem(local_symbol)  # 添加下拉框

    def add_data_slot(self):
        filetypes = ["Text files(*.json)", "Text files(*.csv)"]
        filename, ft = QFileDialog.getOpenFileName(self, '选择数据文件', '', ";;".join(filetypes))
        if not filename:
            return
        self.data_list.addItem(filename)

    def add_backtrack_slot(self):
        filename, _ = QFileDialog.getOpenFileName(self, '选择回测API', '', 'Python files(*.py)')
        if not filename:
            return
        self.backtrack_list.addItem(filename)

    def add_sm_slot(self):
        local_symbol = self.local_symbol_box.currentText()
        sm = self.size_map.text()
        lst = self.sm_pool.setdefault(local_symbol, [])
        if sm in lst:
            return
        lst.append(sm)
        self.size_map_table.insertRow(0)
        self.size_map_table.setItem(0, 0, QTableWidgetItem(local_symbol))
        self.size_map_table.setItem(0, 1, QTableWidgetItem(sm))

    def get_params(self):
        s_m = {self.size_map_table.item(i, 0).text(): int(self.size_map_table.item(i, 1).text()) for i in
               range(self.size_map_table.rowCount())}
        par = {"initial_capital": float(self.initial_capital.text()),
               "size_map": s_m,
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

    def get_data(self):
        data = []
        for row in range(self.data_list.count()):
            path = self.data_list.item(row).text()
            suffix = os.path.splitext(path)[-1]
            if suffix == '.json':  # json
                with open(path, 'r') as fp:
                    data.append(json.load(fp)['data'])
            elif suffix == '.csv':  # csv
                with open(path, 'r') as fp:
                    data.append(pandas.read_csv(fp))
            else:
                raise Exception(f"未知文件类型\n{path}")
        return data

    def get_ext(self):
        ext = []
        for row in range(self.backtrack_list.count()):
            path = self.backtrack_list.item(row).text()
            with open(path, 'r') as fp:
                ext_ = dynamic_loading_api(fp)
                if not isinstance(ext_, LooperApi):
                    raise TypeError(f"你的回测API类型出错,期望LooperApi,你的{type(ext_)}\n{path}")
                ext.append(ext_)
        return ext

    def params_zn(self):
        zn_map = {"initial_capital": "初始资金",
                  # "size_map": "合约数量乘数",
                  "deal_pattern": "成交模式",
                  "close_pattern": "优先平仓模式",
                  "commission": "手续费",
                  "today_commission": "平今手续费",
                  "yesterday_commission": "平昨手续费",
                  "close_commission": "平仓手续费",
                  "slippage_sell": "平空头滑点",
                  "slippage_cover": "平多头滑点",
                  "slippage_buy": "买多滑点",
                  "slippage_short": "卖空滑点",
                  }
        for en, zn in zn_map.items():
            getattr(self, f"{en}_label").setText(f"{zn}\n{en}")

    def run_slot(self):
        if self.data_list.count() <= 0:
            TipDialog("还未传入数据")
            return
        if self.backtrack_list.count() <= 0:
            TipDialog("还未传入回测API")
            return
        if self.size_map_table.rowCount() <= 0:
            TipDialog("还未选择size_map")
            return
        self.name = f"回测{self.counter} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        try:
            worker = BacktrackrWorker(name=self.name, sig=self.sig.report_sig, data=self.get_data(),
                                      strategy=self.get_ext(),
                                      params=self.get_params())
        except Exception as e:
            QMessageBox.information(self, '提示', str(e))
            return
        self.thread_pool.start(worker)
        self.counter += 1

    @Slot(dict)
    def report_slot(self, res: dict):
        if res['error']:
            QMessageBox.information(self, '错误', res['error'])
        else:
            if self.tableWidget.isHidden():
                self.tableWidget.show()
            open_btn = QsPushButton(self, res['url'])
            open_btn.setText(res['name'])
            self.tableWidget.insertRow(self.table_index)
            self.tableWidget.setCellWidget(self.table_index, 0, open_btn)
            self.table_index += 1

    def sm_generate_menu(self, pos):
        row_num = -1
        for i in self.size_map_table.selectionModel().selection().indexes():
            row_num = i.row()
        if row_num < 0:
            return
        menu = QMenu()
        del_item = menu.addAction("移除")
        delall_item = menu.addAction("❌移除所有")
        action = menu.exec_(self.size_map_table.mapToGlobal(pos))
        if action == del_item:
            local_symbol = self.size_map_table.item(row_num, 0).text()
            sm = self.size_map_table.item(row_num, 1).text()
            self.sm_pool[local_symbol].remove(sm)
            self.size_map_table.removeRow(row_num)
        elif action == delall_item:
            self.size_map_table.setRowCount(0)

    def data_generate_menu(self, pos):
        row_num = -1
        for i in self.data_list.selectionModel().selection().indexes():
            row_num = i.row()
        if row_num < 0:
            return
        menu = QMenu()
        del_item = menu.addAction("移除")
        delall_item = menu.addAction("❌移除所有")
        action = menu.exec_(self.data_list.mapToGlobal(pos))
        if action == del_item:
            self.data_list.takeItem(row_num)
        elif action == delall_item:
            self.data_list.clear()

    def bt_generate_menu(self, pos):
        row_num = -1
        for i in self.backtrack_list.selectionModel().selection().indexes():
            row_num = i.row()
        if row_num < 0:
            return
        menu = QMenu()
        del_item = menu.addAction("移除")
        delall_item = menu.addAction("❌移除所有")
        action = menu.exec_(self.backtrack_list.mapToGlobal(pos))
        if action == del_item:
            self.backtrack_list.takeItem(row_num)
        elif action == delall_item:
            self.backtrack_list.clear()


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
