import os
from app.lib.get_path import join_path


class QssHelper:
    qss_path = join_path(os.getcwd(), 'app', 'ui', 'qss')
    print(qss_path)
    debug = True
    signin = None
    order = None
    account = None
    mainwindow = None
    home = None
    strategy = None
    market = None
    config = None
    log = None

    @classmethod
    def read_log(cls):
        if not cls.log:
            with open(join_path(cls.qss_path, 'log.qss'), 'r')as f:
                cls.log = f.read()
        return cls.log

    @classmethod
    def read_config(cls):
        if not cls.config:
            with open(join_path(cls.qss_path, 'config.qss'), 'r')as f:
                cls.config = f.read()
        return cls.config

    @classmethod
    def read_signin(cls):
        if not cls.signin:
            with open(join_path(cls.qss_path, 'signin.qss'), 'r')as f:
                cls.signin = f.read()
        return cls.signin

    @classmethod
    def read_order(cls):
        if not cls.order:
            with open(join_path(cls.qss_path, 'order.qss'), 'r')as f:
                cls.order = f.read()
        return cls.order

    @classmethod
    def read_mainwindow(cls):
        if not cls.mainwindow:
            with open(join_path(cls.qss_path, 'mainwindow.qss'), 'r')as f:
                cls.mainwindow = f.read()
        return cls.mainwindow

    @classmethod
    def read_home(cls):
        if not cls.home:
            with open(join_path(cls.qss_path, 'home.qss'), 'r')as f:
                cls.home = f.read()
        return cls.home

    @classmethod
    def read_account(cls):
        if not cls.account:
            with open(join_path(cls.qss_path, 'account.qss'), 'r')as f:
                cls.account = f.read()
        return cls.account

    @classmethod
    def read_market(cls):
        if not cls.market:
            with open(join_path(cls.qss_path, 'market.qss'), 'r')as f:
                cls.market = f.read()
        return cls.market

    @classmethod
    def read_strategy(cls):
        if not cls.strategy:
            with open(join_path(cls.qss_path, 'strategy.qss'), 'r')as f:
                cls.strategy = f.read()
        return cls.strategy
