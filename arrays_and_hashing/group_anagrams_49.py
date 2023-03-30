"""
Given an array of strings strs, group the anagrams together. You can return
the answer in any order.

 An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly once.

 Example 1:
 Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

 Example 2:
 Input: strs = [""]
Output: [[""]]

 Example 3:
 Input: strs = ["a"]
Output: [["a"]]


 Constraints:
 1 <= strs.length <= 10⁴
 0 <= strs[i].length <= 100
 strs[i] consists of lowercase English letters.
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        1. Sort the string and use it as the key
        2. Use a hashmap to store the key and the list of strings
        3. Return the values of the hashmap
        Time: O(n * klogk) because we sort each string (klogk) and iterate through the list (n)
        Space: O(n * k) because we store the strings (k) in the hashmap (n)
        """

        # Handle the two edge cases correctly
        if len(strs) == 0:
            return [""]
        if len(strs) == 1:
            return [strs]

        hashmap = defaultdict(list)
        for s in strs:
            hashmap["".join(sorted(s))].append(s)
        return hashmap.values()
