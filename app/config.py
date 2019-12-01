from PySide2.QtGui import QCloseEvent
from PySide2.QtWidgets import QMessageBox, QDialog
from PySide2.QtCore import Qt, Slot

from app.lib.global_var import G
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
qss = """QWidget{
background:#ffffff;
color:#000000;
margin:0px;
}

QComboBox,QLineEdit,QDoubleSpinBox,QSpinBox{
    color:#000000;
    border:1px solid #1b89ca;
    border-radius:5px;
}

QPushButton{
background:#ffffff;
color:#000000;
padding:10px

}

QPushButton:hover{
    background:#1b89ca;
    color:#000000
}

QCheckBox{
    border-radius:5px;
}

QCheckBox::indicator:checked {
    color:#1b89ca;
 }"""

class ConfigDialog(QDialog, Ui_Config):
    def __init__(self, mainwindow):
        super(ConfigDialog, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(qss)
        self.mainwindow = mainwindow
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
        QMessageBox.information(self, '提示', '修改成功', QMessageBox.Ok, QMessageBox.Ok)

    def closeEvent(self, arg__1: QCloseEvent):
        self.mainwindow.cfg_dialog = None
        arg__1.accept()
