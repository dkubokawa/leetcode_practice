"""
# Given a string s, find the length of the longest substring without repeating
# characters.
#
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
#
#  Constraints:
#  0 <= s.length <= 5 * 10⁴
#  s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :param s: str of characters
        :return: int

        Implementation:
        - Use a dictionary to store the index of each char
        - Use a left pointer to keep track of the left boundary of the current window
        - Use a right pointer to keep track of the right boundary of the current window
        - Use a res variable to keep track of the longest substring without repeating characters
        - Iterate through the string
            - If char is not in seen, add it to seen and update res
            - If char is in seen, update left
        - Return res
        Time Complexity: O(n) since we are iterating through the string once
        Space Complexity: O(n) since we are using a dictionary to store the index of each char
        """
        seen = {}
        res = 0
        left = 0

        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        for right, char in enumerate(s):
            # If char is not in seen, add it to seen and update res
            if char not in seen:
                res = max(res, right - left + 1)
            else:
                # Scenario 1: char is in seen, but it is not in the current window. Update res
                if seen[char] < left:
                    res = max(res, right - left + 1)
                # Scenario 2: char is in seen and it is in the current window. Update left to the next index of char
                else:
                    left = seen[char] + 1
            seen[char] = right
        return res
