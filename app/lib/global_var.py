class G(dict):
    mainwindow = None
    # log
    log_history = []
    # market
    all_contracts = {}
    subscribes = {}
    market_tick = {}
    market_tick_row_map = []
    # account
    current_account = None
    account = {}
    account_row_map = []
    # order
    choice_local_symbol = None
    order_tick_row_map = []  # with tick ={}

    # kline
    kline_folder = "/static/kline.html"
