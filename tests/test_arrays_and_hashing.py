from arrays_and_hashing.contains_duplicate_217 import Solution as contains_duplicate
from arrays_and_hashing.group_anagrams_49 import Solution as group_anagrams
from arrays_and_hashing.top_k_frequent_elements_347 import (
    Solution as top_k_frequent_elements,
)
from arrays_and_hashing.two_sum_1 import Solution as two_sum
from arrays_and_hashing.valid_anagram_242 import Solution as valid_anagram
from arrays_and_hashing.valid_sudoku_36 import Solution as valid_sudoku


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
