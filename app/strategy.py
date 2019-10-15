import re

from PySide2.QtCore import Slot
from PySide2.QtWidgets import QWidget, QTableWidgetItem, QPushButton, QMessageBox, QTableWidget, QHeaderView, \
    QFileDialog

from app.ui.ui_strategy import Ui_Strategy
from ctpbee import current_app as bee_current_app, dynamic_loading_api
from app.lib.strategy_lib import check_code, strategy_template

strategy_table_column = ("name", "status", "operator", "delete")


class StrategyWidget(QWidget, Ui_Strategy):
    def __init__(self, mainwindow):
        super(StrategyWidget, self).__init__()
        self.setupUi(self)
        self.row = 0
        self.strategy_table.setEditTriggers(QTableWidget.NoEditTriggers)  # 单元格不可编辑
        self.strategy_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch);  # 所有列自适应表格宽度
        self.fill_table()
        self.add_strategy_btn.clicked.connect(self.add_strategy_slot)
        self.gen_strategy.clicked.connect(self.gen_strategy_slot)

    @Slot()
    def add_strategy_slot(self):
        pattern = r"ext\s*=\s*\w*[(][\"\'](.*)[\"\'][)]"
        filename, _ = QFileDialog.getOpenFileName(self, '选择文件', '', 'Python files(*.py)')
        if not filename:
            return
        # msg = check_code(filename)
        # if msg:
        # return QMessageBox.warning(self, 'CtpBee策略', msg, QMessageBox.Ok, QMessageBox.Ok)
        with open(filename, 'r') as f:
            try:
                ext = dynamic_loading_api(f)
                bee_current_app.add_extension(ext)
                QMessageBox.information(self, 'ctpbee策略', "策略添加成功", QMessageBox.Ok, QMessageBox.Ok)
                self.fill_table()
            except Exception as e:
                print("添加更新策略文件：", e)
                QMessageBox.warning(self, 'ctpbee策略', str(e), QMessageBox.Ok, QMessageBox.Ok)

    @Slot()
    def gen_strategy_slot(self):
        filename, _ = QFileDialog.getSaveFileName(self, "策略模板", "", "Python files(*.py)")
        if filename:
            filename = filename if filename.endswith('.py') else filename + '.py'
            with open(filename, 'w') as f:
                f.write(strategy_template)
            return QMessageBox.information(self, 'CtpBee策略', "策略模板已生成", QMessageBox.Ok, QMessageBox.Ok)

    def fill_table(self):
        self.strategy_table.setRowCount(0)
        self.row = 0
        for k, v in bee_current_app.extensions.items():
            if v.frozen:
                status = "停止"
                s_btn = QPushButton("开启")
                s_btn.setStyleSheet("QPushButton{background-color:green}")
                s_btn.clicked.connect(self.open_strategy_slot)
            else:
                status = "运行中"
                s_btn = QPushButton("停止")
                s_btn.setStyleSheet("QPushButton{background-color:red}")
                s_btn.clicked.connect(self.close_strategy_slot)

            d_btn = QPushButton("删除")
            d_btn.clicked.connect(self.delete_strategy_slot)
            self.strategy_table.insertRow(self.row)
            self.strategy_table.setItem(self.row, 0, QTableWidgetItem(k))
            self.strategy_table.setItem(self.row, 1, QTableWidgetItem(status))
            if k == 'default_setting':
                s_btn.setEnabled(False)
                d_btn.setEnabled(False)
            self.strategy_table.setCellWidget(self.row, 2, s_btn)
            self.strategy_table.setCellWidget(self.row, 3, d_btn)
            self.row += 1

    @Slot()
    def close_strategy_slot(self):
        row = self.strategy_table.currentRow()
        name = self.strategy_table.item(row, strategy_table_column.index('name')).text()
        res = bee_current_app.suspend_extension(name)
        if res:
            QMessageBox().information(self, "提示", "'停止成功'", QMessageBox.Ok, QMessageBox.Ok)
            self.fill_table()
        else:
            QMessageBox().warning(self, "提示", "'停止失败", QMessageBox.Ok, QMessageBox.Ok)

    @Slot()
    def open_strategy_slot(self):
        row = self.strategy_table.currentRow()
        name = self.strategy_table.item(row, strategy_table_column.index('name')).text()
        res = bee_current_app.enable_extension(name)
        if res:
            QMessageBox().information(self, "提示", "'开启成功'", QMessageBox.Ok, QMessageBox.Ok)
            self.fill_table()
        else:
            QMessageBox().warning(self, "提示", "'开启失败", QMessageBox.Ok, QMessageBox.Ok)

    @Slot()
    def delete_strategy_slot(self):
        row = self.strategy_table.currentRow()
        name = self.strategy_table.item(row, strategy_table_column.index('name')).text()
        bee_current_app.del_extension(name)
        QMessageBox().information(self, "提示", "'删除成功'", QMessageBox.Ok, QMessageBox.Ok)
        self.fill_table()
