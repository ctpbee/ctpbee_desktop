import json
import os
from queue import Queue
from app.lib.get_path import config_path
from copy import deepcopy

default_shortcut = {
    "home": "Ctrl+H",
    "market": "Ctrl+Q",
    "order": "Ctrl+X",
    "strategy": "Ctrl+S",
    "backtrack": "Ctrl+B",
    "log": "Ctrl+L",
    "config": "Ctrl+C",
}


class Config:
    REFRESH_INTERVAL = None
    INSTRUMENT_INDEPEND = None
    SLIPPAGE_SHORT = None
    SLIPPAGE_BUY = None
    SLIPPAGE_COVER = None
    SLIPPAGE_SELL = None
    CLOSE_PATTERN = None
    SHARED_FUNC = None
    #

    shortcut = deepcopy(default_shortcut)

    def back_default(self):
        self.shortcut = deepcopy(default_shortcut)
        self.to_file()

    def __init__(self):
        self.path = config_path
        with open(self.path, 'r')as fp:
            data = fp.read()
            if data:
                self.update(json.loads(data))

    def update(self, data: dict):
        for k, v in data.items():
            if hasattr(self, k):
                setattr(self, k, v)

    def to_dict(self):
        pr = {}
        for name in dir(self):
            value = getattr(self, name)
            if not name.startswith('__') and not callable(value):
                pr[name] = value
        return pr

    def to_file(self):
        with open(self.path, 'w')as f:
            json.dump(self.to_dict(), f)


class G(dict):
    mainwindow = None
    user_path = None
    #
    current_page = None
    #
    config = Config()
    # log
    log_history = []
    # market
    all_contracts = {}
    subscribes = {}
    market_tick = {}
    market_tick_row_map = []
    # account
    current_account = None
    account = {}
    account_row_map = []
    # order
    choice_local_symbol = None
    order_tick_row_map = []  # with tick ={}
    order_position_row_map = []

    # kline
    kline_folder = "/static/kline.html"
    pool_done = False
    tick_queue = Queue()
