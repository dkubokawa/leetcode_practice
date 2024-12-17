# LC 125 (Easy): Valid Palindrome

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
