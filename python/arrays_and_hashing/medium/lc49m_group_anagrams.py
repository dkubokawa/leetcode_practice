# LC 49 (Medium): Group Anagrams
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        :param List[str] strs: list of strings to group
        :return: List[List[str]]: list of lists of strings grouped by anagrams
        Implementation:
            Sort the string and use it as the key
            Use a hashmap to store the key and the list of strings
            Return the values of the hashmap
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
