"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[
k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not
matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
 3 <= nums.length <= 3000
-10⁵ <= nums[i] <= 10⁵
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        :param List[int] nums: input array
        :return: List[List[int]]. All triplets that add up to 0.
        Implementation:
            We sort the array.
            We iterate through the array, and for each element, we use two pointers
            to find the other two numbers that add up to 0.
            We use a list to keep track of the triplets we have already seen.
            We return the list of triplets.
        Time Complexity: O(nlogn) + O(n^2) = O(n^2) since we will iterate through the array once, and for each
            element, we will iterate through the rest of the array using two pointers.
        Space Complexity: O(n) since we are using a list to keep track of the triplets.
        """


        if len(nums) < 2:
            return []

        nums = sorted(nums)
        triples = []

        for index, value in enumerate(nums):
            # No duplicates, so can't re-use same starting val
            if index > 0 and value == nums[index - 1]:
                continue
            l = index + 1
            r = len(nums) - 1
            while l < r:
                total_sum = value + nums[l] + nums[r]
                if total_sum == 0:
                    triples.append([nums[index], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif total_sum < 0:
                    l += 1
                else:
                    r -= 1
        return triples
