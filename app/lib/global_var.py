def update_(mapp, new_list):
    """
    按mapp里的顺序排序newlist
    :param mapp:
    :param new_list:
    :return:
    """
    temp = []
    for i in new_list:
        if i in mapp:
            temp.insert(mapp.index(i), i)
        else:
            temp.append(i)
    return temp


class G(dict):
    mainwindow = None
    # market
    all_contracts = {}
    subscribes = {}
    market_tick = {}
    market_tick_row_map = []
    # account
    account = {}
    account_row_map = []
    # order
    choice_local_symbol = None
    order_tick_row_map = []  # with tick ={}

    ## position
    order_position_row_map = []
    ## activate
    order_activate_row_map = []
    ## order
    order_order_row_map = []
    ## trade
    order_trade_row_map = []

    @classmethod
    def update_order_position_row_map(cls, new_list: list):
        cls.order_position_row_map = update_(cls.order_position_row_map, new_list)

    @classmethod
    def update_order_activate_row_map(cls, new_list: list):
        cls.order_activate_row_map = update_(cls.order_activate_row_map, new_list)

    @classmethod
    def update_order_order_row_map(cls, new_list: list):
        cls.order_order_row_map = update_(cls.order_order_row_map, new_list)

    @classmethod
    def update_order_trade_row_map(cls, new_list: list):
        cls.order_trade_row_map = update_(cls.order_trade_row_map, new_list)