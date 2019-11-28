import os
from app.lib.get_path import join_path


class QssHelper:
    qss_path = join_path(os.getcwd(), 'app', 'ui', 'qss')
    print(qss_path)
    signin = join_path(qss_path, 'signin.qss')
    account = join_path(qss_path, 'account.qss')
    order = join_path(qss_path, 'order.qss')
    mainwindow = join_path(qss_path, 'mainwindow.qss')
    home = join_path(qss_path, 'home.qss')

    @classmethod
    def read_signin(cls):
        with open(cls.signin, 'r')as f:
            return f.read()

    @classmethod
    def read_order(cls):
        with open(cls.order, 'r')as f:
            return f.read()

    @classmethod
    def read_mainwindow(cls):
        with open(cls.mainwindow, 'r')as f:
            return f.read()

    @classmethod
    def read_home(cls):
        with open(cls.home, 'r')as f:
            return f.read()
