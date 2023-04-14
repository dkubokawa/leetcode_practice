from two_pointers.container_with_most_water_11 import (
    Solution as container_with_most_water,
)
from two_pointers.three_sum_15 import Solution as three_sum
from two_pointers.two_sum_2_input_array_is_sorted_167 import Solution as two_sum_2
from two_pointers.valid_palindrome_125 import Solution as valid_palindrome


def test_valid_palindrome_simple():
    s1 = "A man, a plan, a canal: Panama"
    assert True == valid_palindrome().isPalindrome(s1)

    s2 = "race a car"
    assert False == valid_palindrome().isPalindrome(s2)

    s3 = " "
    assert True == valid_palindrome().isPalindrome(s3)


def test_two_sum_2_simple():
    numbers = [2, 7, 11, 15]
    target = 9
    assert [1, 2] == two_sum_2().twoSum(numbers, target)

    numbers = [2, 3, 4]
    target = 6
    assert [1, 3] == two_sum_2().twoSum(numbers, target)

    numbers = [-1, 0]
    target = -1
    assert [1, 2] == two_sum_2().twoSum(numbers, target)


def test_three_sum_simple():
    nums = [-1, 0, 1, 2, -1, -4]
    assert [[-1, -1, 2], [-1, 0, 1]] == three_sum().threeSum(nums)

    nums = [0, 1, 1]
    assert [] == three_sum().threeSum(nums)

    nums = [0, 0, 0]
    assert [[0, 0, 0]] == three_sum().threeSum(nums)

    nums = [0, 0]
    assert [] == three_sum().threeSum(nums)


def test_container_with_most_water_simple():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert 49 == container_with_most_water().maxArea(height)

    height = [1, 1]
    assert 1 == container_with_most_water().maxArea(height)

    height = [4, 3, 2, 1, 4]
    assert 16 == container_with_most_water().maxArea(height)

    height = [1, 2, 1]
    assert 2 == container_with_most_water().maxArea(height)
