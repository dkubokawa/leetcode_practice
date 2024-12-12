# LC 1 (Easy): Two Sum
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :param List[int] nums: List of integers to search
        :param int target: Target sum. Expected sum of two numbers in nums to sum to target.
        :return: List[int]: Indices of two numbers in nums that sum to target.

        Implementation: Use a dictionary to store the list of numbers. The key is the number and the value is the index.
            We calculate the complement of the current number (target - value) and check if it is in the dictionary.
            We return the index of the complement and the current index if we find it.
        Time Complexity: O(n) due to the for loop
        Space Complexity:  O(n) due to the dictionary
        """
        numbers = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in numbers.keys():
                return [numbers[complement], index]
            numbers[value] = index
