import json
import os
from copy import deepcopy

from PySide2 import QtGui, QtCore
from PySide2.QtCore import QRegExp, Slot, QTimer, Qt, QEvent, QObject
from PySide2.QtGui import QRegExpValidator, QMovie, QCloseEvent, QBitmap, QPainter, QKeySequence
from PySide2.QtWidgets import QWidget, QMessageBox, QLineEdit

from app.lib.global_var import G
from app.ui.ui_signin import Ui_SignIn
from ctpbee import CtpBee, VLogger, current_app
from app.lib.get_path import get_user_path, desktop_path, join_path, config_path
from app.loading import LoadingDialog
from app.main import MainWindow
from app.ui import qss


class Vlog(VLogger):
    def handler_record(self, record):
        msg = f"{record['created'].split(' ')[1]}   {record['name']} " \
              f"  {record['levelname']}   {record['owner']}   {record['message']}"
        G.log_history.append(msg)
        if G.mainwindow:
            G.mainwindow.job.log_signal.emit(msg)
        if G.loading:
            try:
                msg1 = json.loads(record['message'].replace("\'", "\""))
                G.loading.msg.setText(msg1['ErrorMsg'])
            except Exception as e:
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
        # self.setWindowFlag(Qt.FramelessWindowHint)  # 去边框
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setStyleSheet(qss)
        # tab
        self.setTabOrder(self.userid_sim, self.password_sim)
        self.setTabOrder(self.password_sim, self.interface_sim)
        self.setTabOrder(self.interface_sim, self.other)
        self.setTabOrder(self.other, self.remember_me)
        #
        self.setTabOrder(self.userid, self.password)
        self.setTabOrder(self.password, self.brokerid)
        self.setTabOrder(self.brokerid, self.auth_code)
        self.setTabOrder(self.auth_code, self.appid)
        self.setTabOrder(self.appid, self.td_address)
        self.setTabOrder(self.td_address, self.md_address)
        self.setTabOrder(self.md_address, self.interface_)
        self.setTabOrder(self.interface_, self.remember_me)
        self.setTabOrder(self.remember_me, self.sign_in_btn)
        self.icon.installEventFilter(self)
        self.icon.setText('快速登录')
        self.icon.setStyleSheet("""
        QLabel{
        image: url(:/menu/images/bee_temp_grey.png);
        }
        QLabel:hover{
        color:#1B89CA;
        border:1px solid #2B2B2B;
        border-radius: 5px;
        }
        """)
        #
        self.sign_in_btn.clicked.connect(self.sign_in_slot)
        self.sign_in_btn.setDisabled(True)
        #
        for i in self.__dict__.values():
            if isinstance(i, QLineEdit):
                i.setContextMenuPolicy(Qt.NoContextMenu)  ######不允许右键产生子菜单
        self.login_tab.currentChanged.connect(self.check_disable)
        # 普通
        self.userid_sim.currentTextChanged.connect(self.check_disable)
        self.password_sim.textChanged.connect(self.check_disable)
        #
        self.userid.currentTextChanged.connect(self.check_disable)
        self.password.textChanged.connect(self.check_disable)
        self.brokerid.currentTextChanged.connect(self.check_disable)
        self.auth_code.currentTextChanged.connect(self.check_disable)
        self.appid.currentTextChanged.connect(self.check_disable)
        self.td_address.currentTextChanged.connect(self.check_disable)
        self.td_address.editTextChanged.connect(self.editTextChanged_slot)
        self.md_address.editTextChanged.connect(self.editTextChanged_slot)
        self.md_address.currentTextChanged.connect(self.check_disable)
        # timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.close_load)
        self.load_remember()

    def submask(self):
        self.bmp = QBitmap(self.size())
        self.bmp.fill()
        self.p = QPainter(self.bmp)
        self.p.setPen(Qt.black)
        self.p.setBrush(Qt.black)
        self.p.drawRoundedRect(self.bmp.rect(), 10, 10)
        self.setMask(self.bmp)

    @Slot()
    def check_disable(self):
        if self.login_tab.currentIndex() == 0:
            if self.userid_sim.currentText() and self.password_sim.text():
                self.sign_in_btn.setEnabled(True)
            else:
                self.sign_in_btn.setDisabled(True)
        if self.login_tab.currentIndex() == 1:
            if self.userid.currentText() and \
                    self.password.text() and \
                    self.brokerid.currentText() and \
                    self.auth_code.currentText() and \
                    self.appid.currentText() and \
                    self.td_address.currentText() and \
                    self.md_address.currentText():
                self.sign_in_btn.setEnabled(True)
            else:
                self.sign_in_btn.setDisabled(True)

    def editTextChanged_slot(self):
        td = self.td_address.currentText()
        md = self.md_address.currentText()
        k = 'tcp://'
        if not md.startswith(k):
            self.md_address.setCurrentText(k + md)
        if not td.startswith(k):
            self.td_address.setCurrentText(k + td)

    def load_remember(self):

        def get_account(path):
            data = {}
            with open(path, 'r')as f:
                info = f.read()
            if info:
                try:
                    data = json.loads(info)
                    if not isinstance(info, dict):
                        raise Exception
                except Exception:
                    pass
            return data

        path_list = os.listdir(desktop_path)
        for i in path_list:
            path = join_path(desktop_path, i, '.account.json')
            if os.path.exists(path):
                info = get_account(path)
                self.userid.addItem(info.get('userid'))
                self.brokerid.addItem(info.get('brokerid'))
                self.auth_code.addItem(info.get('auth_code'))
                self.appid.addItem(info.get('appid'))
                self.td_address.addItem(info.get('td_address'))
                self.md_address.addItem(info.get('md_address'))
                self.interface_.addItem(info.get('interface'))
            path = join_path(desktop_path, i, '.sim.json')
            if os.path.exists(path):
                info = get_account(path)
                self.userid_sim.addItem(info.get('userid'))
                self.password_sim.setText(info.get('password'))
                self.remember_me_sim.setChecked(True)

    def load_config(self):
        for k, v in G.config.to_dict().items():
            if v:
                current_app.config.update({k: v})

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
        self.timer.start(2000)  # ms
        self.loading.msg.setText("正在连接服务器...")
        self.loading.exec_()
        if bee_app and \
                bee_app.trader and \
                bee_app.td_login_status:
            ##
            G.signin_success(info['userid'])
            ##
            self.load_config()
            ###
            mainwindow = MainWindow()
            mainwindow.sign_in_success()
            mainwindow.show()
            self.close()
            return True
        else:
            return False

    def sign_in_slot(self):
        if self.login_tab.currentIndex() == 0:
            self.common_sign_in()
        elif self.login_tab.currentIndex() == 1:
            self.detailed_sign_in()

    def common_sign_in(self):
        info = dict(
            userid=self.userid_sim.currentText(),
            password=self.password_sim.text(),
            interface=self.interface_sim.currentText(),
        )
        which_ = self.other.currentText()
        if which_ == 'simnow24小时':
            info.update(simnow_24)
        elif which_ == 'simnow移动':
            info.update(simnow_yd)
        if self.sign_in(info):
            if self.remember_me_sim.isChecked():
                account_path = os.path.join(G.user_path, ".sim.json")
                with open(account_path, 'w') as f:
                    json.dump(info, f)
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
                self.interface_sim.setCurrentText(msg)
                if not self.sign_in(info):
                    QMessageBox.information(self, "提示", "登录失败")

    def detailed_sign_in(self):
        info = dict(
            userid=self.userid.currentText(),
            password=self.password.text(),
            brokerid=self.brokerid.currentText(),
            md_address=self.md_address.currentText(),
            td_address=self.td_address.currentText(),
            product_info="",
            appid=self.appid.currentText(),
            auth_code=self.auth_code.currentText(),
            interface=self.interface_.currentText(),
        )
        if self.sign_in(info):
            if self.remember_me.isChecked():
                account_path = os.path.join(G.user_path, ".account.json")
                with open(account_path, 'w') as f:
                    account = deepcopy(info)
                    account.pop('password')
                    json.dump(account, f)
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

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if watched == self.icon:
            if event.type() == QEvent.MouseButtonPress:
                if self.login_tab.currentIndex() == 0:
                    self.login_tab.setCurrentIndex(1)
                    self.icon.setText('详细登录')
                else:
                    self.login_tab.setCurrentIndex(0)
                    self.icon.setText('快速登录')

        return super().eventFilter(watched, event)

    # def mousePressEvent(self, event):
    #     if event.button() == Qt.LeftButton:
    #         self.m_flag = True
    #         self.r_flag = False
    #         self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
    #         event.accept()
    #
    # def mouseReleaseEvent(self, event):
    #     self.r_flag = True
    #     event.accept()
    #
    # def mouseMoveEvent(self, QMouseEvent):
    #     try:
    #         if Qt.LeftButton and self.m_flag and not self.r_flag:
    #             self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
    #             QMouseEvent.accept()
    #     except:
    #         pass
