from sliding_window.best_time_to_buy_stock_121 import Solution as best_time_to_buy_stock
from sliding_window.longest_substring_without_repeating_characters_3 import \
    Solution as longest_substring_without_repeating_characters


def test_best_time_to_buy_stock_simple():
    assert 5 == best_time_to_buy_stock().maxProfit([7, 1, 5, 3, 6, 4])
    assert 0 == best_time_to_buy_stock().maxProfit([7, 6, 4, 3, 1])


def test_longest_substring_without_repeating_characters_simple():
    assert 3 == longest_substring_without_repeating_characters().lengthOfLongestSubstring("abcabcbb")
    assert 1 == longest_substring_without_repeating_characters().lengthOfLongestSubstring("bbbbb")
    assert 3 == longest_substring_without_repeating_characters().lengthOfLongestSubstring("pwwkew")


def test_longest_substring_without_repeating_characters_empty():
    assert 0 == longest_substring_without_repeating_characters().lengthOfLongestSubstring("")
    assert 1 == longest_substring_without_repeating_characters().lengthOfLongestSubstring(" ")
    assert 1 == longest_substring_without_repeating_characters().lengthOfLongestSubstring("a")
    assert 4 == longest_substring_without_repeating_characters().lengthOfLongestSubstring("abcd")
