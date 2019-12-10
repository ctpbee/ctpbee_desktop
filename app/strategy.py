import os
import re

from PySide2.QtCore import Slot, QUrl
from PySide2.QtGui import QDesktopServices
from PySide2.QtWidgets import QWidget, QTableWidgetItem, QPushButton, QMessageBox, QTableWidget, QHeaderView, \
    QFileDialog

from app.lib.global_var import G
from app.tip import TipDialog
from app.ui import strategy_qss
from app.ui.ui_strategy import Ui_Strategy
from ctpbee import current_app as bee_current_app, dynamic_loading_api
from app.lib.strategy_lib import check_code, strategy_template

strategy_table_column = ("name", "status", "operator", "delete")


class StrategyWidget(QWidget, Ui_Strategy):
    def __init__(self, mainwindow):
        super(StrategyWidget, self).__init__(parent=mainwindow)
        self.setupUi(self)
        self.setStyleSheet(strategy_qss)
        self.row = 0
        self.strategy_table.setEditTriggers(QTableWidget.NoEditTriggers)  # 单元格不可编辑
        self.strategy_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch);  # 所有列自适应表格宽度
        self.strategy_table.verticalHeader().setVisible(False)  # 所有列自适应表格宽度
        self.load_strategy()
        self.add_strategy_btn.clicked.connect(self.add_strategy_slot)
        self.gen_strategy.clicked.connect(self.gen_strategy_slot)

    def load_strategy(self):
        for name, path in G.config.strategys.items():
            if os.path.exists(path):
                with open(path, 'r') as f:
                    try:
                        ext = dynamic_loading_api(f)
                        bee_current_app.add_extension(ext)
                        bee_current_app.suspend_extension(ext.extension_name)  # 停止
                        # bee_current_app.suspend_extension(path)  # 停止
                    except Exception as e:
                        pass
        self.fill_table()

    @Slot()
    def add_strategy_slot(self):
        pattern = r"ext\s*=\s*\w*[(][\"\'](.*)[\"\'][)]"
        filename, _ = QFileDialog.getOpenFileName(self, '选择文件', '', 'Python files(*.py)')
        if not filename:
            return
        with open(filename, 'r') as f:
            try:
                ext = dynamic_loading_api(f)
                bee_current_app.add_extension(ext)
                G.config.strategys.update({ext.extension_name: filename})
                G.config.to_file()
                TipDialog("策略添加成功")
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
            TipDialog(f"策略模板已生成")
            QDesktopServices.openUrl(QUrl(os.path.dirname(filename)))

    def fill_table(self):
        self.strategy_table.setRowCount(0)
        self.row = 0
        for k, v in bee_current_app.extensions.items():
            if v.frozen:
                status = "停止"
                s_btn = QPushButton("开启")
                s_btn.setStyleSheet("background-color:green;padding:10px;border-radius:5px;")
                s_btn.clicked.connect(self.open_strategy_slot)
            else:
                status = "运行中"
                s_btn = QPushButton("停止")
                s_btn.setStyleSheet("background-color:red;padding:10px;border-radius:5px;")
                s_btn.clicked.connect(self.close_strategy_slot)

            d_btn = QPushButton("删除")
            d_btn.setStyleSheet("background-color:#e9bc1b;padding:10px;border-radius:5px;")
            d_btn.clicked.connect(self.delete_strategy_slot)
            self.strategy_table.insertRow(self.row)
            self.strategy_table.setItem(self.row, 0, QTableWidgetItem(k))
            self.strategy_table.setItem(self.row, 1, QTableWidgetItem(status))
            if k != 'default_setting':
                self.strategy_table.setCellWidget(self.row, 2, s_btn)
                self.strategy_table.setCellWidget(self.row, 3, d_btn)
            self.row += 1

    @Slot()
    def close_strategy_slot(self):
        row = self.strategy_table.currentRow()
        name = self.strategy_table.item(row, strategy_table_column.index('name')).text()
        res = bee_current_app.suspend_extension(name)
        if res:
            TipDialog("停止成功")
            self.fill_table()
        else:
            TipDialog("停止失败")

    @Slot()
    def open_strategy_slot(self):
        row = self.strategy_table.currentRow()
        name = self.strategy_table.item(row, strategy_table_column.index('name')).text()
        res = bee_current_app.enable_extension(name)
        if res:
            TipDialog("开启成功")
            self.fill_table()
        else:
            TipDialog("开启失败")

    @Slot()
    def delete_strategy_slot(self):
        reply = QMessageBox.question(self, '策略提示', "确定删除吗？",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.No:
            return
        row = self.strategy_table.currentRow()
        name = self.strategy_table.item(row, strategy_table_column.index('name')).text()
        bee_current_app.del_extension(name)
        G.config.strategys.pop(name)
        G.config.to_file()
        TipDialog("删除成功")
        self.fill_table()
