# LC 242 (Easy): Valid Anagram

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
