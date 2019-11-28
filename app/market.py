import time

from PySide2.QtCore import Slot, QTimer
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QWidget, QTableWidgetItem, QPushButton, QMessageBox, QListWidgetItem, QTableWidget, \
    QHeaderView
from app.ui.ui_market import Ui_Market
from app.lib.global_var import G
from app.loading import LoadingDialog

contract_space = " " * 2
market_table_column = ['name', 'local_symbol', 'last_price', 'operator']


class MarketWidget(QWidget, Ui_Market):
    def __init__(self, mainwindow):
        super(MarketWidget, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("行情")
        self.item_row = len(G.market_tick_row_map)
        self.bee_ext = mainwindow.bee_ext
        self.mainwindow = mainwindow
        self.progressBar = self.mainwindow.progressbar
        self.load_status = self.mainwindow.status_msg
        # ctpbee
        for local_symbol in sorted(G.all_contracts):
            self.symbol_list.addItem(local_symbol + contract_space + G.all_contracts[local_symbol])  # 添加下拉框
        self.progressBar.setMaximum(len(G.subscribes))
        #
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)  # 单元格不可编辑
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自适应表格宽度
        self.fill_table()
        self.load_time = time.time()
        self.tableWidget.setEnabled(False)
        # load动画
        self.loading = LoadingDialog()
        self.loading.msg.setText('正在加载合约列表...')
        self.loading.show()
        # 渲染table
        self.obj = self.mainwindow.job
        self.obj.market_signal.connect(self.set_item_slot)
        # 订阅
        self.subscribe_singel.clicked.connect(self.subscribe_slot)
        self.subscribe_type.clicked.connect(self.subscribe_type_slot)
        self.subscribe_all.clicked.connect(self.subscribe_all_slot)
        # self.unsubscribe.clicked.connect(self.unsubscribe_slot)

        # timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timer_slot)
        self.timer.start(500)

    @Slot()
    def go_order(self):
        row = self.tableWidget.currentRow()
        name = self.tableWidget.item(row, 0).text()
        local_symbol = self.tableWidget.item(row, 1).text()
        msg = QMessageBox(QMessageBox.Question, "提示", f"您选择的是 {name} [ {local_symbol} ] 是否进入下单界面?",
                          QMessageBox.NoButton,
                          self)
        yr_btn = msg.addButton(self.tr("是"), QMessageBox.YesRole)
        msg.addButton(self.tr("否"), QMessageBox.NoRole)
        msg.exec_()
        if msg.clickedButton() == yr_btn:
            G.choice_local_symbol = local_symbol
            self.mainwindow.order_handle()
        else:
            return

    @Slot()
    def timer_slot(self):
        if time.time() - self.load_time > 0.5:
            self.progressBar.setValue(len(G.subscribes))
            self.load_status.setText("订阅合约列表加载完成")
            self.timer.stop()
            self.loading.close()
            self.tableWidget.setEnabled(True)

    @Slot()
    def unsubscribe_slot(self):
        for i in G.subscribes:
            self.bee_ext.app.market.unsubscribe(i.split('.')[0])
        self.mainwindow.market_handle()

    @Slot()
    def subscribe_slot(self):
        local_symbol = self.symbol_list.currentText().split(contract_space)[0]
        name = self.symbol_list.currentText().split(contract_space)[1]
        if local_symbol:
            res = self.bee_ext.app.subscribe(local_symbol)
            if res == 0:
                G.subscribes.update({local_symbol: name})
                self.progressBar.setMaximum(len(G.subscribes))  # 更新进度条
                QMessageBox().information(self, "提示", "订阅成功", QMessageBox.Ok, QMessageBox.Ok)
            else:
                QMessageBox().warning(self, "提示", "订阅失败", QMessageBox.Ok, QMessageBox.Ok)

    @Slot()
    def subscribe_type_slot(self):
        local_symbol_ = self.symbol_list.currentText().split(contract_space)[0]
        symbol = ''.join([x for x in local_symbol_.split('.')[0] if x.isalpha()])  # AP
        for local_symbol in G.all_contracts:
            if symbol in local_symbol:
                res = self.bee_ext.app.subscribe(local_symbol)
                if res == 0:
                    G.subscribes.update({local_symbol: G.all_contracts[local_symbol]})
                    self.progressBar.setMaximum(len(G.subscribes))  # 更新进度条
        self.mainwindow.market_handle()

    @Slot()
    def subscribe_all_slot(self):
        for local_symbol in sorted(G.all_contracts):
            self.bee_ext.app.subscribe(local_symbol)  # 订阅
            G.subscribes.update({local_symbol: G.all_contracts[local_symbol]})  # 更新订阅列表
        self.mainwindow.market_handle()

    def insert_(self, row, tick):
        for i, col in enumerate(market_table_column):
            if col == 'operator':
                btn = QPushButton('前往下单')
                btn.clicked.connect(self.go_order)
                self.tableWidget.setCellWidget(row, i, btn)
            else:
                self.tableWidget.setItem(row, i, QTableWidgetItem(str(tick[col])))

    def fill_table(self):
        """
        必须按序填充
        :return:
        """
        self.load_status.setText("加载订阅合约...")
        d = G.market_tick_row_map
        count = len(d)
        for index, local_symbol in enumerate(d):
            row = index
            self.tableWidget.insertRow(row)
            tick = G.market_tick[local_symbol]
            self.insert_(row, tick)
            # 反馈
            self.progressBar.setValue((index + 1 // count))
            self.load_status.setText("加载中...")

    #
    @Slot()
    def set_item_slot(self, tick: dict):
        local_symbol = tick['local_symbol']
        if local_symbol not in G.market_tick_row_map:  # 不在table ,插入row
            row = self.item_row
            G.market_tick_row_map.append(local_symbol)
            self.tableWidget.insertRow(row)
            self.item_row += 1
            # 渲染
            self.load_time = time.time()  # 刷新关闭渲染动画计时
            self.progressBar.setValue(row)
            self.insert_(row, tick)
        else:  # 已在table中 ,更新对应row
            row = G.market_tick_row_map.index(local_symbol)
            for i, col in enumerate(market_table_column):
                if col == 'operator':  # 按钮无需更新
                    continue
                if col == "last_price":  # 对最新价动态颜色表示涨跌
                    old = self.tableWidget.item(row, i)
                    new = float(tick[col])
                    if old:  # 非空表
                        space_ = " " * 3
                        old = float(old.text().split(space_)[0])
                        difference = new - old
                        if difference > 0:  # 涨
                            it = QTableWidgetItem(f"{str(new)}{space_}↑≈{'%0.2f' % abs(difference)}")
                            it.setTextColor(QColor('red'))
                        elif difference < 0:  # 跌
                            it = QTableWidgetItem(f"{str(new)}{space_}↓≈{'%0.2f' % abs(difference)}")
                            it.setTextColor(QColor('green'))
                        else:
                            continue
                    else:
                        it = QTableWidgetItem(str(tick[col]))
                    self.tableWidget.setItem(row, i, it)
                else:
                    self.tableWidget.setItem(row, i, QTableWidgetItem(str(tick[col])))
