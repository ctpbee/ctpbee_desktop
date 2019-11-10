import json
from copy import deepcopy
from time import sleep
from PySide2.QtCore import QRegExp, Slot, QTimer, Qt
from PySide2.QtGui import QRegExpValidator, QMovie
from PySide2.QtWidgets import QWidget, QMessageBox

from app.lib.global_var import G
from app.ui.ui_signin import Ui_SignIn
from ctpbee import CtpBee, VLogger
from app.lib.get_path import user_account_path
from app.loading import LoadingDialog


class Vlog(VLogger):
    def handler_record(self, record):
        msg = f"{record['created'].split(' ')[1]}   {record['name']} " \
              f"  {record['levelname']}   {record['owner']}   {record['message']}"
        G.mainwindow.job.order_log_signal.emit(msg)


class SignInWidget(QWidget, Ui_SignIn):

    def __init__(self, mainwindow):
        super(SignInWidget, self).__init__()
        self.mainwindow = mainwindow
        self.progressbar = mainwindow.progressbar
        self.status_msg = mainwindow.status_msg
        self.setupUi(self)
        self.setWindowTitle("ctpbee客户端")
        # loading
        self.loading = LoadingDialog()
        self.loading.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏整个头部
        #
        self.load_remember()
        # 设置验证
        reg = QRegExp("PB[0~9]{8}")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg)
        self.userid_1.setValidator(pValidator)
        self.userid_2.setValidator(pValidator)

        reg = QRegExp("[a-zA-z0-9]+$")
        pValidator.setRegExp(reg)
        self.password_1.setValidator(pValidator)
        self.password_2.setValidator(pValidator)

        self.sign_in_btn_1.clicked.connect(self.sign_in_check)
        self.sign_in_btn_2.clicked.connect(self.sign_in_check)
        self.password_1.returnPressed.connect(self.sign_in_check)
        # 检测是否为空
        # 普通
        self.userid_1.textChanged[str].connect(self.check_disable)
        self.password_1.textChanged[str].connect(self.check_disable)
        # 详细
        self.userid_2.textChanged[str].connect(self.check_disable)
        self.password_2.textChanged[str].connect(self.check_disable)
        self.auth_code_2.textChanged[str].connect(self.check_disable)
        self.td_address_2.textChanged[str].connect(self.check_disable)
        self.md_address_2.textChanged[str].connect(self.check_disable)
        self.appid_2.textChanged[str].connect(self.check_disable)
        self.brokerid_2.textChanged[str].connect(self.check_disable)
        # timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.close_load)

    @Slot()
    def check_disable(self):
        if self.login_tab.currentIndex() == 0:
            if self.userid_1.text() and self.password_1.text():
                self.sign_in_btn_1.setEnabled(True)
                self.sign_in_btn_1.setStyleSheet("QPushButton{background-color:green}")
            else:
                self.sign_in_btn_1.setEnabled(False)
        if self.login_tab.currentIndex() == 1:
            if self.userid_2.text() and self.password_2.text() and self.auth_code_2.text() and self.brokerid_2.text() \
                    and self.td_address_2.text() and self.md_address_2.text() and self.appid_2.text():
                self.sign_in_btn_2.setEnabled(True)
                self.sign_in_btn_2.setStyleSheet("QPushButton{background-color:green}")
            else:
                self.sign_in_btn_2.setEnabled(False)

    def load_remember(self):
        with open(user_account_path, 'r')as f:
            info = f.read()
        if info:
            info = json.dumps(info)
            self.userid_2.setText(info.get('userid'))
            self.brokerid_2.setText(info.get('brokerid'))
            self.auth_code_2.setText(info.get('auth_code'))
            self.appid_2.setText(info.get('appid'))
            self.td_address_2.setText(info.get('td_address'))
            self.md_address_2.setText(info.get('md_address'))
            self.interface_2.setCurrentText(info.get('interface'))

    def close_load(self):
        self.loading.close()
        self.timer.stop()

    def sign_in(self, info):
        self.progressbar.setRange(0, 100)
        bee_app = CtpBee(name=info.get("username"), import_name=__name__, refresh=True, logger_class=Vlog)
        login_info = {
            "CONNECT_INFO": info,
            "INTERFACE": info.get('interface'),
            "TD_FUNC": True,
            "MD_FUNC": True,
        }
        bee_app.config.from_mapping(login_info)
        bee_app.start()
        self.progressbar.setValue(20)
        self.status_msg.setText("正在连接服务器...")
        self.progressbar.setValue(60)
        self.timer.start(2000)  # ms
        self.loading.msg.setText("正在连接服务器...")
        self.loading.exec_()
        self.progressbar.setValue(100)
        if bee_app and \
                bee_app.trader and \
                bee_app.td_login_status:
            self.status_msg.setText("登录成功！")
            self.mainwindow.sign_in_success(bee_app)
        else:
            # bee_app.release()
            self.status_msg.setText("请重试")
            QMessageBox.warning(self, "提示", "登录出现错误", QMessageBox.Ok, QMessageBox.Ok)

    def sign_in_check(self):
        info = None
        if self.login_tab.currentIndex() == 0:  # 普通登录
            info = dict(
                userid=self.userid_1.text(),
                password=self.password_1.text(),
                interface=self.interface_1.currentText(),
            )
            if self.other.currentText() == 'simnow24小时':
                info.update(dict(
                    brokerid="9999",
                    md_address="tcp://180.168.146.187:10131",
                    td_address="tcp://180.168.146.187:10130",
                    product_info="",
                    appid="simnow_client_test",
                    auth_code="0000000000000000",
                ))
            if self.other.currentText() == 'simnow移动':
                info.update(dict(
                    brokerid="9999",
                    md_address="tcp://218.202.237.33:10112",
                    td_address="tcp://218.202.237.33:10102",
                    product_info="",
                    appid="simnow_client_test",
                    auth_code="0000000000000000",
                ))
        if self.login_tab.currentIndex() == 1:  # 详细登录
            info = dict(
                userid=self.userid_2.text(),
                password=self.password_2.text(),
                brokerid=self.brokerid_2.text(),
                md_address=self.md_address_2.text(),
                td_address=self.td_address_2.text(),
                product_info="",
                appid=self.appid_2.text(),
                auth_code=self.auth_code_2.text(),
                interface=self.interface_2.currentText(),
            )
            if self.rember_me.isChecked():
                with open(user_account_path, 'w') as f:
                    account = deepcopy(info)
                    account.pop('password')
                    json.dump(account, f)

        self.sign_in(info)
