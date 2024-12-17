# Leetcode 167 (Medium): Two Sum II - Input array is sorted

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        :param List[int] numbers: input array
        :param int target: the target sum
        :return: List[int, int]. Two indices of the two numbers that add up to target.
        Implementation:
            We use two pointers, one at the beginning and one at the end. We add the two numbers.
            If it is less than the target, we move the left pointer to the right.
            If it is greater than the target, we move the right pointer to the left.
            We keep doing this until we find the two numbers that add up to the target.
            We return the indices of the two numbers.
        Time Complexity: O(n) since we will only iterate through the array once
        Space Complexity: O(1) since we are not using any extra space
        """
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                # Leetcode wants the index to start at 1. So we add 1 to both.
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
