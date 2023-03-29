import pytest
from arrays_and_hashing.two_sum_1 import Solution as two_sum
from arrays_and_hashing.valid_anagram_242 import Solution as valid_anagram
from arrays_and_hashing.contains_duplicate_217 import Solution as contains_duplicate

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
    assert True == contains_duplicate().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
