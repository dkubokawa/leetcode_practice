from sliding_window.easy.lc121e_best_time_to_buy_stock import Solution as best_time_to_buy_stock
from sliding_window.medium.lc424m_longest_repeating_character_replacement import (
    Solution as longest_repeating_character_replacement,
)
from sliding_window.medium.lc3m_longest_substring_without_repeating_characters import \
    Solution as longest_substring_without_repeating_characters


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


def test_longest_substring_without_repeating_characters_simple():
    assert 3 == longest_substring_without_repeating_characters().lengthOfLongestSubstring("abcabcbb")
    assert 1 == longest_substring_without_repeating_characters().lengthOfLongestSubstring("bbbbb")
    assert 3 == longest_substring_without_repeating_characters().lengthOfLongestSubstring("pwwkew")


def test_longest_substring_without_repeating_characters_empty():
    assert 0 == longest_substring_without_repeating_characters().lengthOfLongestSubstring("")
    assert 1 == longest_substring_without_repeating_characters().lengthOfLongestSubstring(" ")
    assert 1 == longest_substring_without_repeating_characters().lengthOfLongestSubstring("a")
    assert 4 == longest_substring_without_repeating_characters().lengthOfLongestSubstring("abcd")
