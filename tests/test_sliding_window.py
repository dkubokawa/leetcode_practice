from sliding_window.best_time_to_buy_stock_121 import Solution as best_time_to_buy_stock
from sliding_window.longest_repeating_character_replacement_424 import (
    Solution as longest_repeating_character_replacement,
)


def test_best_time_to_buy_stock_simple():
    assert 5 == best_time_to_buy_stock().maxProfit([7, 1, 5, 3, 6, 4])
    assert 0 == best_time_to_buy_stock().maxProfit([7, 6, 4, 3, 1])


def test_longest_repeating_character_replacement_simple():
    assert 4 == longest_repeating_character_replacement().characterReplacement(
        "ABAB", 2
    )
    assert 4 == longest_repeating_character_replacement().characterReplacement(
        "AABABBA", 1
    )
    assert 2 == longest_repeating_character_replacement().characterReplacement(
        "AABABBA", 0
    )


def test_longest_repeating_character_replacement_complex():
    assert 2 == longest_repeating_character_replacement().characterReplacement(
        "ABCD", 1
    )
    assert 3 == longest_repeating_character_replacement().characterReplacement(
        "ABCD", 2
    )
    assert 4 == longest_repeating_character_replacement().characterReplacement(
        "ABCD", 3
    )
