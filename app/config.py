from PySide2 import QtGui
from PySide2.QtGui import QCloseEvent
from PySide2.QtWidgets import QMessageBox, QDialog, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel
from PySide2.QtCore import Qt, Slot

from app.lib.global_var import G
from app.tip import TipDialog
from app.ui.ui_config import Ui_Config
from ctpbee import current_app as bee_current_app
from app.ui import config_qss

keys = [
    "REFRESH_INTERVAL",
    "INSTRUMENT_INDEPEND",
    "SLIPPAGE_SHORT",
    "SLIPPAGE_BUY",
    "SLIPPAGE_COVER",
    "SLIPPAGE_SELL",
    "CLOSE_PATTERN",
    "SHARED_FUNC"]

zn = {
    "home": "首页",
    "market": "行情",
    "order": "下单",
    "strategy": "策略",
    "backtrack": "回测",
    "log": "日志",
    "config": "设置",
}


class ConfigDialog(QDialog, Ui_Config):
    def __init__(self, mainwindow):
        super(ConfigDialog, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(config_qss)
        self.mainwindow = mainwindow
        # btn
        self.default_btn.clicked.connect(self.default_sc_slot)
        self.submit_btn.clicked.connect(self.update_config)
        self.init_config()
        self.init_shortcut()

    def init_config(self):
        self.REFRESH_INTERVAL.setValue(float(bee_current_app.config['REFRESH_INTERVAL']))
        self.SLIPPAGE_SHORT.setValue(float(bee_current_app.config['SLIPPAGE_SHORT']))
        self.SLIPPAGE_BUY.setValue(float(bee_current_app.config['SLIPPAGE_BUY']))
        self.SLIPPAGE_COVER.setValue(float(bee_current_app.config['SLIPPAGE_COVER']))
        self.SLIPPAGE_SELL.setValue(float(bee_current_app.config['SLIPPAGE_SELL']))
        self.INSTRUMENT_INDEPEND.setCheckState(
            Qt.Checked if bee_current_app.config["INSTRUMENT_INDEPEND"] else Qt.Unchecked)
        self.SHARED_FUNC.setCheckState(
            Qt.Checked if bee_current_app.config["SHARED_FUNC"] else Qt.Unchecked)
        self.CLOSE_PATTERN.setCurrentText(bee_current_app.config["CLOSE_PATTERN"])

    def init_shortcut(self):
        for name, sc in G.config.shortcut.items():
            h_layout = QHBoxLayout(self)
            label = QLabel(self)
            label.setStyleSheet("font: 9pt")
            label.setText(zn[name])
            shortcut = ShortCutEdit(self, name, sc)
            shortcut.setStyleSheet("font: 9pt")
            h_layout.addWidget(label)
            h_layout.addWidget(shortcut)
            self.sc_layout.addLayout(h_layout)

    def default_sc_slot(self):
        G.config.back_default()
        self.mainwindow.update_shortcut()
        self.close()
        TipDialog('已恢复')


    @Slot()
    def update_config(self):
        G.config.REFRESH_INTERVAL = bee_current_app.config['REFRESH_INTERVAL'] = float(self.REFRESH_INTERVAL.text())
        G.config.SLIPPAGE_SHORT = bee_current_app.config['SLIPPAGE_SHORT'] = float(self.SLIPPAGE_SHORT.text())
        G.config.SLIPPAGE_BUY = bee_current_app.config['SLIPPAGE_BUY'] = float(self.SLIPPAGE_BUY.text())
        G.config.SLIPPAGE_COVER = bee_current_app.config['SLIPPAGE_COVER'] = float(self.SLIPPAGE_COVER.text())
        G.config.SLIPPAGE_SELL = bee_current_app.config['SLIPPAGE_SELL'] = float(self.SLIPPAGE_SELL.text())
        G.config.INSTRUMENT_INDEPEND = bee_current_app.config[
            'INSTRUMENT_INDEPEND'] = True if self.INSTRUMENT_INDEPEND.isChecked() else False
        G.config.SHARED_FUNC = bee_current_app.config[
            'SHARED_FUNC'] = True if self.SHARED_FUNC.isChecked() else False
        G.config.CLOSE_PATTERN = bee_current_app.config['CLOSE_PATTERN'] = str(self.CLOSE_PATTERN.currentText())
        G.config.to_file()
        TipDialog('修改成功')

    def closeEvent(self, arg__1: QCloseEvent):
        self.mainwindow.cfg_dialog = None
        arg__1.accept()


modmap = {
    Qt.ControlModifier: "Ctrl",
    Qt.AltModifier: "Alt",
    Qt.ShiftModifier: "Shift",
}


class ShortCutEdit(QLineEdit):
    def __init__(self, parent_widget, name, sc):
        super(self.__class__, self).__init__(parent_widget)
        self.parent_widget = parent_widget
        self.setText(sc)
        self.name = name

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        if event.key() == Qt.Key_Backspace:
            self.setText("--")
            return
        sequence = []
        for modifier, text in modmap.items():
            if event.modifiers() & modifier:
                sequence.append(text)
        if Qt.Key_A <= event.key() <= Qt.Key_Z:
            sequence.append(chr(event.key()))
        self.setText("+".join(sequence))

    def keyReleaseEvent(self, event: QtGui.QKeyEvent):
        sp = self.text().split("+")[-1]
        if len(sp) != 1:
            self.setText("--")
        G.config.shortcut.update({self.name: self.text()})
        G.config.to_file()
        self.parent_widget.mainwindow.update_shortcut()
        TipDialog("修改成功")
