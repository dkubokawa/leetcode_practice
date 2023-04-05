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
