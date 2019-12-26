import json
from app.lib.get_path import join_path, get_user_path
from copy import deepcopy
from cryptography.fernet import Fernet

key = lambda: Fernet.generate_key()

default_shortcut = {
    "home": "Ctrl+H",
    "market": "Ctrl+Q",
    "order": "Ctrl+X",
    "kline": "Ctrl+K",
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
    SHORTCUT = deepcopy(default_shortcut)  # 快捷键
    #
    STRATEGYS = {}  # 策略
    #
    CONTRACT = {}  # 收藏合约
    LOCAL_SOURCE = True  # 本地数据源
    WHICH_DB = ""
    DB_INFO = {}

    def back_default(self):
        self.SHORTCUT = deepcopy(default_shortcut)
        self.to_file()

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
        with open(G.config_path, 'w')as f:
            json.dump(self.to_dict(), f)


class G(dict):
    mainwindow = None  # 主窗口
    #
    current_page = None  # 主窗口显示的当前页面index
    #
    config = Config()  # 用户配置
    # log
    log_history = []  # 历史日志
    # market
    all_contracts = {}  # 所有合约
    subscribes = {}  # 订阅合约
    market_tick_row_map = []  # 合约对应表格 row
    ticks = {}  # 最新推送的所有订阅合约tick
    # account
    current_account = None  # 当前账户
    user_path = None  # 当前账户路径
    config_path = None  # 当前账户配置路径
    account = {}  # 账户信息
    account_row_map = []  # 账户对应表格 row
    # order
    choice_local_symbol = None  # 选择的合约，用于k线选择读取哪个合约数据
    order_tick_row_map = []  # 下单界面tick对应表格row
    # kline
    kline_folder = "/static/e_kline.html"
    pool_done = False  # 对线程发送停止信号
    #
    db = None

    @staticmethod
    def signin_success(uid):
        G.current_account = uid
        G.user_path = get_user_path(uid)
        G.config_path = join_path(G.user_path, '.config.json')

        try:
            with open(G.config_path, 'r')as f:
                data = f.read()
                cfg = json.loads(data)
                if isinstance(cfg, dict):
                    G.config.update(cfg)
        except Exception:
            with open(G.config_path, 'w'):
                pass
