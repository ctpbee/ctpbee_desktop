import time

from PySide2.QtCore import Slot, QTimer
from PySide2.QtWidgets import QWidget, QTableWidgetItem, QPushButton, QMessageBox, QListWidgetItem, QTableWidget, \
    QHeaderView
from app.ui.ui_market import Ui_Market
from app.lib.global_var import G


class MarketWidget(QWidget, Ui_Market):
    def __init__(self, mainwindow):
        super(MarketWidget, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("行情")

        self.item_row = 0
        self.bee_ext = mainwindow.bee_ext
        self.mainwindow = mainwindow
        self.progressBar = self.mainwindow.progressbar
        self.load_status = self.mainwindow.status_msg
        # ctpbee
        for local_symbol in sorted(G.all_contracts):
            self.symbol_list.addItem(local_symbol)  # 添加下拉框
        self.progressBar.setMaximum(len(G.subscribes))
        #
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)  # 单元格不可编辑
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自适应表格宽度
        self.fill_table()
        self.load_time = time.time()
        self.tableWidget.setEnabled(False)
        # 渲染table
        self.obj = self.mainwindow.job
        self.obj.market_signal.connect(self.set_item_slot)
        # 订阅
        self.subscribe_singel.clicked.connect(self.subscribe_slot)
        # timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timer_slot)
        self.timer.start(500)

        self.pushButton_test.clicked.connect(self.test_all)

    @Slot()
    def test_all(self):
        for local_symbol in sorted(G.all_contracts):
            self.bee_ext.app.subscribe(local_symbol)  # 订阅 可去除  ，下同
            G.subscribes.update({local_symbol: G.all_contracts[local_symbol]})  # 更新订阅列表
        self.mainwindow.market_handle()

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
            self.tableWidget.setEnabled(True)
            self.timer.stop()
            self.progressBar.setValue(len(G.subscribes))
            self.load_status.setText("订阅合约列表加载完成")

    @Slot()
    def subscribe_slot(self):
        local_symbol = self.symbol_list.currentText()
        if local_symbol:
            res = self.bee_ext.app.subscribe(local_symbol)
            if res == 0:
                G.subscribes.update({local_symbol: G.all_contracts[local_symbol]})
                self.progressBar.setMaximum(len(G.subscribes))  # 更新进度条
                QMessageBox().information(self, "提示", "订阅成功", QMessageBox.Ok, QMessageBox.Ok)
            else:
                QMessageBox().warning(self, "提示", "订阅失败", QMessageBox.Ok, QMessageBox.Ok)

    def fill_table(self):
        """
        必须按序填充
        :return:
        """
        self.load_status.setText("加载订阅合约...")
        d = G.market_tick_row_map
        count = len(d)
        for index, k in enumerate(sorted(d, key=d.__getitem__)):
            row = d[k]
            self.tableWidget.insertRow(row)
            tick = G.market_tick[k]
            name = tick['name']
            local_symbol = tick['local_symbol']
            last_price = tick['last_price']
            self.tableWidget.setItem(row, 0, QTableWidgetItem(name))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(local_symbol))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(last_price)))
            btn = QPushButton('前往下单')
            btn.clicked.connect(self.go_order)
            self.tableWidget.setCellWidget(row, 3, btn)
            # 反馈
            self.progressBar.setValue((index + 1 // count))
            self.load_status.setText(f"加载 {name}")

    #
    @Slot()
    def set_item_slot(self, tick: dict):
        name = tick['name']
        local_symbol = tick['local_symbol']
        last_price = tick['last_price']
        if local_symbol not in G.market_tick_row_map:  # 不在table ,插入row
            row = self.item_row
            G.market_tick_row_map[local_symbol] = row
            self.tableWidget.insertRow(row)
            self.item_row += 1
            self.load_time = time.time()
            self.progressBar.setValue(row)

        else:  # 已在table中 ,更新对应row
            row = G.market_tick_row_map[local_symbol]

        self.tableWidget.setItem(row, 0, QTableWidgetItem(name))
        self.tableWidget.setItem(row, 1, QTableWidgetItem(local_symbol))
        self.tableWidget.setItem(row, 2, QTableWidgetItem(str(last_price)))
        btn = QPushButton('前往下单')
        btn.clicked.connect(self.go_order)
        self.tableWidget.setCellWidget(row, 3, btn)
