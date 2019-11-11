from PySide2.QtWidgets import QMessageBox, QDialog
from PySide2.QtCore import Qt, Slot
from app.ui.ui_config import Ui_Config
from ctpbee import current_app as bee_current_app

keys = [
    "REFRESH_INTERVAL",
    "INSTRUMENT_INDEPEND",
    "SLIPPAGE_SHORT",
    "SLIPPAGE_BUY",
    "SLIPPAGE_COVER",
    "SLIPPAGE_SELL",
    "CLOSE_PATTERN",
    "SHARED_FUNC"]


class ConfigDialog(QDialog, Ui_Config):
    def __init__(self, mainwindow):
        super(ConfigDialog, self).__init__()
        self.setupUi(self)
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

        self.pushButton.clicked.connect(self.update_config)

    @Slot()
    def update_config(self):
        bee_current_app.config['REFRESH_INTERVAL'] = float(self.REFRESH_INTERVAL.text())
        bee_current_app.config['SLIPPAGE_SHORT'] = float(self.SLIPPAGE_SHORT.text())
        bee_current_app.config['SLIPPAGE_BUY'] = float(self.SLIPPAGE_BUY.text())
        bee_current_app.config['SLIPPAGE_COVER'] = float(self.SLIPPAGE_COVER.text())
        bee_current_app.config['SLIPPAGE_SELL'] = float(self.SLIPPAGE_SELL.text())
        bee_current_app.config['INSTRUMENT_INDEPEND'] = True if self.INSTRUMENT_INDEPEND.isChecked() else False
        bee_current_app.config['SHARED_FUNC'] = True if self.SHARED_FUNC.isChecked() else False
        bee_current_app.config['CLOSE_PATTERN'] = str(self.CLOSE_PATTERN.currentText())
        QMessageBox.information(self, '提示', '修改成功', QMessageBox.Ok, QMessageBox.Ok)
