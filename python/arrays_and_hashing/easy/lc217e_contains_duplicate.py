# LC 217 (Easy): Contains Duplicate
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        :param List[int] nums: List of integers to check for duplicates
        :return: True if there are duplicates, False otherwise
        :rtype: bool
        Implementation: Use a set to store the numbers we've seen so far.
            If we find a number that is already in the set, we know we've seen it before and can return True.
            If we reach the end of the list and haven't found a duplicate, return False.
        Time Complexity: O(n) due to the for loop
        Space Complexity: O(n) due to the set
        """
        set_of_nums = set()
        for num in nums:
            if num in set_of_nums:
                return True
            set_of_nums.add(num)
        return False
