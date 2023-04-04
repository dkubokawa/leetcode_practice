"""
# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads the same
# forward and backward. Alphanumeric characters include letters and numbers.
#
#  Given a string s, return true if it is a palindrome, or false otherwise.
#
# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric
# characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
#
#  Constraints:
#  1 <= s.length <= 2 * 10⁵
#  s consists only of printable ASCII characters.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Implementation:
        Plan to use two pointers, one at the beginning and one at the end.
        We will compare the characters at each pointer and if they are not equal, return False
        If they are equal, we will move the pointers inwards and continue comparing
        We will stop when the pointers meet in the middle or pass each other
        Time Complexity: O(n) since we will only iterate through the string once
        Space Complexity: O(1) since we are not using any extra space
        """
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

        # """
        # Implementation: Using python builtins. Uses some extra memory but is more readable.
        # """
        # new_str = ''.join([c.lower() for c in s if c.isalnum()])
        # return new_str == new_str[::-1]
