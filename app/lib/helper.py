from datetime import datetime, timedelta
import json
import os
from PySide2.QtCore import QObject, Signal, Slot
from pymongo import MongoClient

from app.lib.get_path import tick_path, join_path
from app.lib.global_var import G

import csv
import pandas as pd


class Job(QObject):
    account_signal = Signal(dict)
    market_signal = Signal(dict)
    kline_tick_signal = Signal(dict)
    order_position_signal = Signal(list)
    order_activate_signal = Signal(list)
    order_order_signal = Signal(list)
    order_trade_signal = Signal(list)
    log_signal = Signal(str)
    #
    sig_bar_record = Signal(str, list)

    def __init__(self):
        super(self.__class__, self).__init__()


def get_history_tick():
    if G.config.LOCAL_SOURCE:
        return get_local()
    else:
        return get_external()


headers = ['timestamp', 'open_price', 'close_price', 'low_price',
           'high_price', 'volume']


def get_local():
    try:
        file_path = join_path(tick_path, f"{str(G.choice_local_symbol)}.csv")
        f_csv = pd.read_csv(file_path)
        info = map(lambda x: [x[i] for i in headers], f_csv.to_dict(orient='index').values())
        data = json.dumps({G.choice_local_symbol: list(info)})
    except Exception as e:
        print("get_local", e)
        data = json.dumps({G.choice_local_symbol: list()})
    return data


def db_connect(**kwargs):
    """
    连接成功返回为空，失败返回错误
    :param kwargs:
    :return: if true return None else return error message
    """
    try:
        client = MongoClient(kwargs['url'], serverSelectionTimeoutMS=3000,
                             socketTimeoutMS=3000)
        print(client.list_database_names())
        db = client[kwargs['database']]
        print(db.list_collection_names())
    except Exception as e:
        return str(e)


def create_db_conn(**kwargs):
    from ctpbee import QADataSupport
    G.db = QADataSupport(host=kwargs['host'])


def get_external():
    try:
        info = []
        data = G.db.get_future_min(G.choice_local_symbol, frq=G.frq, start=G.start, end=G.end)
        if data:
            for item in data:
                timestamp = item['datetime']
                info.append([timestamp, item['open_price'], item['high_price'], item['low_price'],
                             item['close_price'], item['volume']])
    except Exception as e:
        print(e)
        info = []
    return json.dumps({G.choice_local_symbol: info})


class KInterfaceObject(QObject):
    qt_to_js = Signal(str)  # channel only str  在js中connect
    qt_to_js_reload = Signal()  # channel only str  在js中connect
    js_to_qt = Signal(str)

    def __init__(self):
        super(self.__class__, self).__init__()

    @Slot(result=str)
    def get_history_data(self):
        """js通过调用此函数获取数据"""
        return get_history_tick()


class RecordWorker(QObject):
    record_sig = Signal(str, list)

    def __init__(self):
        super(self.__class__, self).__init__()
        self.record_sig.connect(self.record)

    def record(self, local_symbol, info):
        file_path = join_path(tick_path, f"{str(local_symbol)}.csv")
        isexists = os.path.exists(file_path)
        with open(file_path, 'a+', newline='') as f:
            f_csv = csv.writer(f)
            if not isexists:
                f_csv.writerow(headers)
            f_csv.writerow(info)
