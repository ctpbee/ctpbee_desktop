from PySide2.QtCore import Slot
from PySide2.QtWidgets import QWidget, QTableWidgetItem, QTableWidget, QHeaderView
from app.ui.ui_account import Ui_Account
from app.lib.global_var import G


def key_zn(key):
    map = {
        "accountid": "账户名",
        "available": "账户可用",
        "balance": "余额",
        "frozen": "冻结",
        "gateway_name": "接口",
        "local_account_id": "本地账户名",
    }
    return map[key]


class AccountWidget(QWidget, Ui_Account):
    def __init__(self, mainwindow):
        super(AccountWidget, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("账户")
        self.row = 0
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)  # 单元格不可编辑
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自适应表格宽度

        #
        self.fill_table()

        #
        self.obj = mainwindow.job
        self.obj.account_signal.connect(self.set_item)

    def fill_table(self):
        """
        必须按序填充
        :return:
        """
        d = G.account_row_map
        for k in sorted(d, key=d.__getitem__):  # 必须按顺序插入row ,否则渲染失败
            row = d[k]
            self.tableWidget.insertRow(row)
            key = key_zn(k)
            value = G.account[k]  # 获取值
            self.tableWidget.setItem(row, 0, QTableWidgetItem(key))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(value)))

    @Slot(dict)
    def set_item(self, account: dict):
        for k, v in account.items():
            if k not in G.account_row_map:
                row = self.row
                G.account_row_map[k] = row
                self.tableWidget.insertRow(row)
                self.row += 1
            else:
                row = G.account_row_map[k]
            key = key_zn(k)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(key))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(v)))
