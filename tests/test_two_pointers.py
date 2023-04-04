from two_pointers.valid_palindrome_125 import Solution as valid_palindrome


def test_valid_palindrome_simple():
    s1 = "A man, a plan, a canal: Panama"
    assert True == valid_palindrome().isPalindrome(s1)

    s2 = "race a car"
    assert False == valid_palindrome().isPalindrome(s2)

    s3 = " "
    assert True == valid_palindrome().isPalindrome(s3)
