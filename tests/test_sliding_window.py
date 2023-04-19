from sliding_window.best_time_to_buy_stock_121 import Solution as best_time_to_buy_stock


def test_best_time_to_buy_stock_simple():
    assert 5 == best_time_to_buy_stock().maxProfit([7, 1, 5, 3, 6, 4])
    assert 0 == best_time_to_buy_stock().maxProfit([7, 6, 4, 3, 1])
