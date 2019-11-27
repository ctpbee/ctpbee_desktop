import json
import os
from copy import deepcopy
from PySide2.QtCore import QRegExp, Slot, QTimer, Qt
from PySide2.QtGui import QRegExpValidator, QMovie, QCloseEvent
from PySide2.QtWidgets import QWidget, QMessageBox

from app.lib.global_var import G
from app.ui.ui_signin import Ui_SignIn
from ctpbee import CtpBee, VLogger, current_app
from app.lib.get_path import get_user_path, desktop_path, join_path
from app.loading import LoadingDialog
from app.main import MainWindow


class Vlog(VLogger):
    def handler_record(self, record):
        msg = f"{record['created'].split(' ')[1]}   {record['name']} " \
              f"  {record['levelname']}   {record['owner']}   {record['message']}"
        G.log_history.append(msg)
        if G.mainwindow:
            G.mainwindow.job.order_log_signal.emit(msg)
        if G.loading:
            G.loading.msg.setText(record['message'])


simnow_yd = dict(
    brokerid="9999",
    md_address="tcp://218.202.237.33:10112",
    td_address="tcp://218.202.237.33:10102",
    product_info="",
    appid="simnow_client_test",
    auth_code="0000000000000000",
)

simnow_24 = dict(
    brokerid="9999",
    md_address="tcp://180.168.146.187:10131",
    td_address="tcp://180.168.146.187:10130",
    product_info="",
    appid="simnow_client_test",
    auth_code="0000000000000000",
)


class SignInWidget(QWidget, Ui_SignIn):

    def __init__(self):
        super(SignInWidget, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("ctpbee客户端")
        #
        self.load_remember()
        self.sign_in_btn_1.clicked.connect(self.common_sign_in)
        self.sign_in_btn_2.clicked.connect(self.detailed_sign_in)
        self.sign_in_btn_2.setEnabled(True)
        self.sign_in_btn_2.setStyleSheet("QPushButton{background-color:green}")
        self.password_1.returnPressed.connect(self.common_sign_in)
        # 普通
        self.userid_1.textChanged[str].connect(self.check_disable)
        self.password_1.textChanged[str].connect(self.check_disable)
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

    def load_remember(self):
        path_list = os.listdir(desktop_path)
        for i in path_list:
            path = join_path(desktop_path, i, '.account.json')
            if not os.path.exists(path):
                continue
            with open(path, 'r')as f:
                info = f.read()
            if info:
                try:
                    info = json.loads(info)
                    if not isinstance(info, dict):
                        raise Exception
                except Exception:
                    info = {}
                self.userid_2.setText(info.get('userid'))
                self.brokerid_2.setText(info.get('brokerid'))
                self.auth_code_2.setText(info.get('auth_code'))
                self.appid_2.setText(info.get('appid'))
                self.td_address_2.setText(info.get('td_address'))
                self.md_address_2.setText(info.get('md_address'))
                self.interface_2.setCurrentText(info.get('interface'))
            return

    def load_config(self):
        config_path = os.path.join(G.user_path, ".config.json")
        if not os.path.exists(config_path):
            return
        with open(config_path, 'r')as f:
            data = f.read()
            try:
                cfg = json.loads(data)
                if not isinstance(cfg, dict):
                    raise Exception
            except Exception:
                return
            for k, v in cfg.items():
                current_app.config[k] = v

    def close_load(self):
        self.loading.close()
        self.timer.stop()

    def sign_in(self, info):
        bee_app = CtpBee(name=info.get("username"), import_name=__name__, refresh=True, logger_class=Vlog)
        login_info = {
            "CONNECT_INFO": info,
            "INTERFACE": info.get('interface'),
            "TD_FUNC": True,
            "MD_FUNC": True,
        }
        bee_app.config.from_mapping(login_info)
        bee_app.start()
        # loading
        self.loading = LoadingDialog()
        G.loading = self.loading
        self.timer.start(3000)  # ms
        self.loading.msg.setText("正在连接服务器...")
        self.loading.exec_()
        if bee_app and \
                bee_app.trader and \
                bee_app.td_login_status:
            ##
            return True
        else:
            return False

    def common_sign_in(self):
        info = dict(
            userid=self.userid_1.text(),
            password=self.password_1.text(),
            interface=self.interface_1.currentText(),
        )
        which_ = self.other.currentText()
        if which_ == 'simnow24小时':
            info.update(simnow_24)
        elif which_ == 'simnow移动':
            info.update(simnow_yd)
        if self.sign_in(info):
            G.current_account = info['userid']
            G.user_path = get_user_path(info['userid'])
            ##
            self.load_config()
            ###
            mainwindow = MainWindow()
            mainwindow.sign_in_success()
            mainwindow.show()
            self.close()
        else:
            if which_ == 'simnow24小时':
                msg = 'simnow移动'
                info.update(simnow_yd)
            else:
                msg = 'simnow24小时'
                info.update(simnow_24)
            reply = QMessageBox.question(self, '登录出现错误', "是否尝试" + msg,
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                self.sign_in(info)

    def detailed_sign_in(self):
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
        if self.sign_in(info):
            G.current_account = info['userid']
            G.user_path = get_user_path(info['userid'])
            ##
            self.load_config()
            ###
            if self.rember_me.isChecked():
                account_path = os.path.join(get_user_path(G.current_account), f".account.json")
                with open(account_path, 'w') as f:
                    account = deepcopy(info)
                    account.pop('password')
                    json.dump(account, f)
            mainwindow = MainWindow()
            mainwindow.sign_in_success()
            mainwindow.show()
            self.close()
        else:
            QMessageBox.information(self, '提示', "登录出现错误",
                                    QMessageBox.Ok, QMessageBox.Ok)

    def closeEvent(self, event: QCloseEvent):
        G.loading = None
        if G.mainwindow is None:
            try:
                current_app.release()
            except Exception:
                pass
        event.accept()
