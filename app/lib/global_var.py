class G(dict):
    mainwindow = None
    # market
    all_contracts = {}
    subscribes = {}
    market_tick = {}
    market_tick_row_map = {}
    # account
    account = {}
    account_row_map = {}
    # order
    order_signal_switch = "position"  # 默认渲染持仓数据
    choice_local_symbol = None
    order_tick_row_map = {}  # with tick ={}
    ## position
    order_position_row_map = {}
    order_position = {}
    ## activate
    order_activate = {}
    order_activate_row_map = {}
    ## order
    order_order = {}
    order_order_row_map = {}
    ## trade
    order_trade = {}
    order_trade_row_map = {}
