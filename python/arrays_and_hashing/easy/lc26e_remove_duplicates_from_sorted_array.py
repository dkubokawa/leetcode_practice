# Leetcode 26 (Easy): Remove Duplicates from Sorted Array
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        :param List[List[str]] nums: sorted array of integers
        :return: int: number of unique elements in nums
        Time Complexity: O(N) since we iterate over nums once
        Space Complexity: O(1) since we don't use any extra space
        """

        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
