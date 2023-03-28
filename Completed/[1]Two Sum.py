"""
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

 You may assume that each input would have exactly one solution, and you may
not use the same element twice.

 Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

 Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

 Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

 Constraints:
 2 <= nums.length <= 10⁴
 -10⁹ <= nums[i] <= 10⁹
 -10⁹ <= target <= 10⁹
 Only one valid answer exists.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :param List[int] nums: List of integers to search
        :param int target: Target sum. Expected sum of two numbers in nums to sum to target.
        :return: List[int]: of indices of two numbers in nums that sum to target.
        """
        numbers = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in numbers.keys():
                return [numbers[complement], index]
            numbers[value] = index


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print([0, 1], Solution().twoSum(nums, target))

    nums = [2, 7, 11, 15]
    target = 17
    print([0, 3], Solution().twoSum(nums, target))

    nums = [2, 7, 11, 15]
    target = 18
    print([1, 2], Solution().twoSum(nums, target))
