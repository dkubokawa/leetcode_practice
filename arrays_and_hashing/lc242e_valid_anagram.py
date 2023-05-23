"""
LeetCode 242 (Easy): Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false
otherwise.

 An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly once.

 Example 1:
 Input: s = "anagram", t = "nagaram"
Output: true

 Example 2:
 Input: s = "rat", t = "car"
Output: false

 Constraints:
 1 <= s.length, t.length <= 5 * 10⁴
 s and t consist of lowercase English letters.
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        :param s: word 1
        :param t: word 2
        :return: True if t is an anagram of s, and False otherwise
        Time Complexity: O(n) or O(s + t) where s and t are the lengths of s and t
        Space Complexity: O(n) or O(s + t) where s and t are the lengths of s and t
        """
        if len(s) != len(t):
            return False

        characters_s = {}
        characters_t = {}

        for i in range(len(s)):
            characters_s[s[i]] = characters_s.get(s[i], 0) + 1
            characters_t[t[i]] = characters_t.get(t[i], 0) + 1

        for key in characters_s:
            if key not in characters_t or characters_s[key] != characters_t[key]:
                return False
        return True
        
# leetcode submit region end(Prohibit modification and deletion)
