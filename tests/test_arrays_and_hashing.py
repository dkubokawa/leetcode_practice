from arrays_and_hashing.lc217e_contains_duplicate import Solution as contains_duplicate
from arrays_and_hashing.lc49m_group_anagrams import Solution as group_anagrams
from arrays_and_hashing.lc128m_longest_consecutive_sequence import (
    Solution as longest_consecutive_sequence,
)
from arrays_and_hashing.lc238m_product_of_array_except_self import (
    Solution as product_of_array_except_self,
)
from arrays_and_hashing.lc347m_top_k_frequent_elements import (
    Solution as top_k_frequent_elements,
)
from arrays_and_hashing.lc1_two_sum import Solution as two_sum
from arrays_and_hashing.lc242e_valid_anagram import Solution as valid_anagram
from arrays_and_hashing.lc36m_valid_sudoku import Solution as valid_sudoku


def test_two_sum_simple():
    assert [0, 1] == two_sum().twoSum([2, 7, 11, 15], 9)
    assert [0, 3] == two_sum().twoSum([2, 7, 11, 15], 17)
    assert [1, 2] == two_sum().twoSum([2, 7, 11, 15], 18)


def test_two_sum_complex():
    assert [0, 1] == two_sum().twoSum([3, 3], 6)


def test_valid_anagram_simple():
    assert True == valid_anagram().isAnagram("anagram", "nagaram")
    assert False == valid_anagram().isAnagram("rat", "car")


def test_valid_anagram_complex():
    assert False == valid_anagram().isAnagram("aacc", "ccac")


def test_contains_duplicate_simple():
    assert True == contains_duplicate().containsDuplicate([1, 2, 3, 1])
    assert False == contains_duplicate().containsDuplicate([1, 2, 3, 4])


def test_contains_duplicate_complex():
    assert True == contains_duplicate().containsDuplicate(
        [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    )


def test_valid_sudoku_simple():
    assert True == valid_sudoku().isValidSudoku(
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
    assert False == valid_sudoku().isValidSudoku(
        [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )


def test_is_valid_sudoku_complex():
    assert False == valid_sudoku().isValidSudoku(
        [
            [".", ".", ".", ".", "5", ".", ".", "1", "."],
            [".", "4", ".", "3", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "3", ".", ".", "1"],
            ["8", ".", ".", ".", ".", ".", ".", "2", "."],
            [".", ".", "2", ".", "7", ".", ".", ".", "."],
            [".", "1", "5", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "2", ".", ".", "."],
            [".", "2", ".", "9", ".", ".", ".", ".", "."],
            [".", ".", "4", ".", ".", ".", ".", ".", "."],
        ]
    )


def test_group_anagrams_simple():
    results = group_anagrams().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert ["eat", "tea", "ate"] in results
    assert ["tan", "nat"] in results
    assert ["bat"] in results


def test_group_anagrams_complex():
    assert [["a"]] == group_anagrams().groupAnagrams(["a"])
    assert [[""]] == group_anagrams().groupAnagrams([""])


def test_top_k_frequent_elements_simple():
    assert [1, 2] == top_k_frequent_elements().topKFrequent([1, 1, 1, 2, 2, 3], 2)
    assert [1, 2, 3] == top_k_frequent_elements().topKFrequent([1, 1, 1, 2, 2, 3], 3)
    assert [1] == top_k_frequent_elements().topKFrequent([1], 1)


def test_top_k_frequent_elements_complex():
    assert [1, 2] == top_k_frequent_elements().topKFrequent([1, 2], 2)


def test_longest_consecutive_sequence_simple():
    assert 4 == longest_consecutive_sequence().longestConsecutive(
        [100, 4, 200, 1, 3, 2]
    )
    assert 9 == longest_consecutive_sequence().longestConsecutive(
        [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    )


def test_longest_consecutive_sequence_complex():
    assert 1 == longest_consecutive_sequence().longestConsecutive([1])
    assert 0 == longest_consecutive_sequence().longestConsecutive([])
    assert 3 == longest_consecutive_sequence().longestConsecutive([0, 1, 2, 0, 1, 2])


def test_product_of_array_except_self_simple():
    assert [24, 12, 8, 6] == product_of_array_except_self().productExceptSelf(
        [1, 2, 3, 4]
    )
    assert [0, 0, 40, 0, 0] == product_of_array_except_self().productExceptSelf(
        [1, 2, 0, 4, 5]
    )
    assert [0, 0, 0, 0] == product_of_array_except_self().productExceptSelf(
        [0, 0, 0, 0]
    )
    assert [0, 0, 0, 0] == product_of_array_except_self().productExceptSelf(
        [1, 0, 3, 0]
    )
    assert [1, 2] == product_of_array_except_self().productExceptSelf([2, 1])
