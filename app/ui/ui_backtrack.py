# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'backtrack.ui',
# licensing of 'backtrack.ui' applies.
#
# Created: Sun Dec 22 14:31:15 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(723, 492)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidgetPage1 = QtWidgets.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.gridLayout = QtWidgets.QGridLayout(self.tabWidgetPage1)
        self.gridLayout.setObjectName("gridLayout")
        self.initial_capital_label = QtWidgets.QLabel(self.tabWidgetPage1)
        self.initial_capital_label.setObjectName("initial_capital_label")
        self.gridLayout.addWidget(self.initial_capital_label, 0, 0, 1, 1)
        self.initial_capital = QtWidgets.QLineEdit(self.tabWidgetPage1)
        self.initial_capital.setObjectName("initial_capital")
        self.gridLayout.addWidget(self.initial_capital, 0, 1, 1, 1)
        self.deal_pattern_label = QtWidgets.QLabel(self.tabWidgetPage1)
        self.deal_pattern_label.setObjectName("deal_pattern_label")
        self.gridLayout.addWidget(self.deal_pattern_label, 0, 2, 1, 1)
        self.deal_pattern = QtWidgets.QComboBox(self.tabWidgetPage1)
        self.deal_pattern.setEditable(True)
        self.deal_pattern.setObjectName("deal_pattern")
        self.deal_pattern.addItem("")
        self.gridLayout.addWidget(self.deal_pattern, 0, 3, 1, 1)
        self.commission_label = QtWidgets.QLabel(self.tabWidgetPage1)
        self.commission_label.setObjectName("commission_label")
        self.gridLayout.addWidget(self.commission_label, 1, 0, 1, 1)
        self.commission = QtWidgets.QLineEdit(self.tabWidgetPage1)
        self.commission.setObjectName("commission")
        self.gridLayout.addWidget(self.commission, 1, 1, 1, 1)
        self.close_pattern_label = QtWidgets.QLabel(self.tabWidgetPage1)
        self.close_pattern_label.setObjectName("close_pattern_label")
        self.gridLayout.addWidget(self.close_pattern_label, 1, 2, 1, 1)
        self.close_pattern = QtWidgets.QComboBox(self.tabWidgetPage1)
        self.close_pattern.setEditable(True)
        self.close_pattern.setObjectName("close_pattern")
        self.close_pattern.addItem("")
        self.gridLayout.addWidget(self.close_pattern, 1, 3, 1, 1)
        self.close_commission_label = QtWidgets.QLabel(self.tabWidgetPage1)
        self.close_commission_label.setObjectName("close_commission_label")
        self.gridLayout.addWidget(self.close_commission_label, 2, 0, 1, 1)
        self.close_commission = QtWidgets.QLineEdit(self.tabWidgetPage1)
        self.close_commission.setObjectName("close_commission")
        self.gridLayout.addWidget(self.close_commission, 2, 1, 1, 1)
        self.slippage_sell_label = QtWidgets.QLabel(self.tabWidgetPage1)
        self.slippage_sell_label.setObjectName("slippage_sell_label")
        self.gridLayout.addWidget(self.slippage_sell_label, 2, 2, 1, 1)
        self.slippage_sell = QtWidgets.QLineEdit(self.tabWidgetPage1)
        self.slippage_sell.setObjectName("slippage_sell")
        self.gridLayout.addWidget(self.slippage_sell, 2, 3, 1, 1)
        self.today_commission_label = QtWidgets.QLabel(self.tabWidgetPage1)
        self.today_commission_label.setObjectName("today_commission_label")
        self.gridLayout.addWidget(self.today_commission_label, 3, 0, 1, 1)
        self.today_commission = QtWidgets.QLineEdit(self.tabWidgetPage1)
        self.today_commission.setObjectName("today_commission")
        self.gridLayout.addWidget(self.today_commission, 3, 1, 1, 1)
        self.slippage_cover_label = QtWidgets.QLabel(self.tabWidgetPage1)
        self.slippage_cover_label.setObjectName("slippage_cover_label")
        self.gridLayout.addWidget(self.slippage_cover_label, 3, 2, 1, 1)
        self.slippage_cover = QtWidgets.QLineEdit(self.tabWidgetPage1)
        self.slippage_cover.setObjectName("slippage_cover")
        self.gridLayout.addWidget(self.slippage_cover, 3, 3, 1, 1)
        self.yesterday_commission_label = QtWidgets.QLabel(self.tabWidgetPage1)
        self.yesterday_commission_label.setObjectName("yesterday_commission_label")
        self.gridLayout.addWidget(self.yesterday_commission_label, 4, 0, 1, 1)
        self.yesterday_commission = QtWidgets.QLineEdit(self.tabWidgetPage1)
        self.yesterday_commission.setObjectName("yesterday_commission")
        self.gridLayout.addWidget(self.yesterday_commission, 4, 1, 1, 1)
        self.slippage_buy_label = QtWidgets.QLabel(self.tabWidgetPage1)
        self.slippage_buy_label.setObjectName("slippage_buy_label")
        self.gridLayout.addWidget(self.slippage_buy_label, 4, 2, 1, 1)
        self.slippage_buy = QtWidgets.QLineEdit(self.tabWidgetPage1)
        self.slippage_buy.setObjectName("slippage_buy")
        self.gridLayout.addWidget(self.slippage_buy, 4, 3, 1, 1)
        self.slippage_short_label = QtWidgets.QLabel(self.tabWidgetPage1)
        self.slippage_short_label.setObjectName("slippage_short_label")
        self.gridLayout.addWidget(self.slippage_short_label, 5, 2, 1, 1)
        self.slippage_short = QtWidgets.QLineEdit(self.tabWidgetPage1)
        self.slippage_short.setObjectName("slippage_short")
        self.gridLayout.addWidget(self.slippage_short, 5, 3, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QtWidgets.QWidget()
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabWidgetPage2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.add_data_btn = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.add_data_btn.setObjectName("add_data_btn")
        self.gridLayout_2.addWidget(self.add_data_btn, 0, 1, 1, 1)
        self.add_backtrack_btn = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.add_backtrack_btn.setObjectName("add_backtrack_btn")
        self.gridLayout_2.addWidget(self.add_backtrack_btn, 0, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.local_symbol_box = QtWidgets.QComboBox(self.tabWidgetPage2)
        self.local_symbol_box.setEditable(True)
        self.local_symbol_box.setObjectName("local_symbol_box")
        self.horizontalLayout.addWidget(self.local_symbol_box)
        self.label = QtWidgets.QLabel(self.tabWidgetPage2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.size_map = QtWidgets.QSpinBox(self.tabWidgetPage2)
        self.size_map.setObjectName("size_map")
        self.horizontalLayout.addWidget(self.size_map)
        self.add_sm_btn = QtWidgets.QToolButton(self.tabWidgetPage2)
        self.add_sm_btn.setObjectName("add_sm_btn")
        self.horizontalLayout.addWidget(self.add_sm_btn)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.data_list = QtWidgets.QListWidget(self.tabWidgetPage2)
        self.data_list.setObjectName("data_list")
        self.gridLayout_2.addWidget(self.data_list, 3, 1, 2, 1)
        self.backtrack_list = QtWidgets.QListWidget(self.tabWidgetPage2)
        self.backtrack_list.setObjectName("backtrack_list")
        self.gridLayout_2.addWidget(self.backtrack_list, 3, 2, 2, 1)
        self.size_map_table = QtWidgets.QTableWidget(self.tabWidgetPage2)
        self.size_map_table.setObjectName("size_map_table")
        self.size_map_table.setColumnCount(2)
        self.size_map_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.size_map_table.setHorizontalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        self.size_map_table.setHorizontalHeaderItem(1, item)
        self.gridLayout_2.addWidget(self.size_map_table, 3, 0, 2, 1)
        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.tabWidgetPage3 = QtWidgets.QWidget()
        self.tabWidgetPage3.setObjectName("tabWidgetPage3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabWidgetPage3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tabWidgetPage3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.tabWidget.addTab(self.tabWidgetPage3, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.run_btn = QtWidgets.QPushButton(Form)
        self.run_btn.setObjectName("run_btn")
        self.verticalLayout.addWidget(self.run_btn)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.initial_capital_label.setText(QtWidgets.QApplication.translate("Form", "initial_capital", None, -1))
        self.initial_capital.setText(QtWidgets.QApplication.translate("Form", "100000", None, -1))
        self.deal_pattern_label.setText(QtWidgets.QApplication.translate("Form", "deal_pattern", None, -1))
        self.deal_pattern.setItemText(0, QtWidgets.QApplication.translate("Form", "price", None, -1))
        self.commission_label.setText(QtWidgets.QApplication.translate("Form", "commission", None, -1))
        self.commission.setText(QtWidgets.QApplication.translate("Form", "0.005", None, -1))
        self.close_pattern_label.setText(QtWidgets.QApplication.translate("Form", "close_pattern", None, -1))
        self.close_pattern.setItemText(0, QtWidgets.QApplication.translate("Form", "yesterday", None, -1))
        self.close_commission_label.setText(QtWidgets.QApplication.translate("Form", "close_commission", None, -1))
        self.close_commission.setText(QtWidgets.QApplication.translate("Form", "0.005", None, -1))
        self.slippage_sell_label.setText(QtWidgets.QApplication.translate("Form", "slippage_sell", None, -1))
        self.slippage_sell.setText(QtWidgets.QApplication.translate("Form", "0", None, -1))
        self.today_commission_label.setText(QtWidgets.QApplication.translate("Form", "today_commission", None, -1))
        self.today_commission.setText(QtWidgets.QApplication.translate("Form", "0.005", None, -1))
        self.slippage_cover_label.setText(QtWidgets.QApplication.translate("Form", "slippage_cover", None, -1))
        self.slippage_cover.setText(QtWidgets.QApplication.translate("Form", "0", None, -1))
        self.yesterday_commission_label.setText(QtWidgets.QApplication.translate("Form", "yesterday_commission", None, -1))
        self.yesterday_commission.setText(QtWidgets.QApplication.translate("Form", "0.002", None, -1))
        self.slippage_buy_label.setText(QtWidgets.QApplication.translate("Form", "slippage_buy", None, -1))
        self.slippage_buy.setText(QtWidgets.QApplication.translate("Form", "0", None, -1))
        self.slippage_short_label.setText(QtWidgets.QApplication.translate("Form", "slippage_short", None, -1))
        self.slippage_short.setText(QtWidgets.QApplication.translate("Form", "0", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), QtWidgets.QApplication.translate("Form", "参数", None, -1))
        self.add_data_btn.setText(QtWidgets.QApplication.translate("Form", "添加数据", None, -1))
        self.add_backtrack_btn.setText(QtWidgets.QApplication.translate("Form", "回测API", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "+", None, -1))
        self.add_sm_btn.setText(QtWidgets.QApplication.translate("Form", "↓", None, -1))
        self.size_map_table.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("Form", "local_symbol", None, -1))
        self.size_map_table.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("Form", "size_map", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), QtWidgets.QApplication.translate("Form", "api", None, -1))
        self.tableWidget.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("Form", "-", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage3), QtWidgets.QApplication.translate("Form", "报告", None, -1))
        self.run_btn.setText(QtWidgets.QApplication.translate("Form", "🚀 开始回测", None, -1))

