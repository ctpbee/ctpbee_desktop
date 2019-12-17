import json
import os
import time
from queue import Queue

from PySide2.QtCore import QObject, Signal, Slot

from app.lib.get_path import tick_path
from app.lib.global_var import G


class Job(QObject):
    account_signal = Signal(dict)
    market_signal = Signal(dict)
    order_tick_signal = Signal(dict)
    order_position_signal = Signal(list)
    order_activate_signal = Signal(list)
    order_order_signal = Signal(list)
    order_trade_signal = Signal(list)
    log_signal = Signal(str)
    #
    sig_bar_record = Signal(str, list)

    def __init__(self):
        super(self.__class__, self).__init__()


class KInterfaceObject(QObject):
    qt_to_js = Signal(str)  # channel only str  在js中connect
    js_to_qt = Signal(str)

    def __init__(self):
        super(self.__class__, self).__init__()

    @Slot(result=str)
    def get_history_data(self):
        """js通过调用此函数获取数据"""
        try:
            file_path = tick_path + f"/{str(G.choice_local_symbol)}.json"
            with open(file_path, 'r') as f:
                data = f.read()
        except:
            data = json.dumps({G.choice_local_symbol: []})
        return data


class RecordWorker(QObject):
    record_sig = Signal(str, list)

    def __init__(self):
        super(self.__class__, self).__init__()
        self.record_sig.connect(self.record)

    def record(self, local_symbol, info):
        file_path = os.path.join(tick_path, f"{str(local_symbol)}.json")
        old = {}
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                data = f.read()
                if data:
                    old = json.loads(data)
        with open(file_path, 'w') as f:
            if not old.get(local_symbol):
                old.setdefault(local_symbol, []).append(info)
            else:
                old[local_symbol].append(info)
            json.dump(old, f)
