# LC 53 (Medium): Maximum Subarray

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Greedy (Kadane's Algorithm) Approach
        # Also a Bottom-Up Dynamic Programming Approach
        # Time-Complexity: O(n)
        # Space-Complexity: O(1)
        max_sum = nums[0] # Could also use float("-inf")
        curr_sum = 0
        for i in range(len(nums)):
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += nums[i]
            max_sum = max(curr_sum, max_sum)
        return max_sum

    def maxSubArray1(self, nums: List[int]) -> int:
        # Brute-Force Approach
        # Time-Complexity: O(n^2)
        # Space-Complexity: O(1)
        max_sum = nums[0]
        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
            max_sum = max(curr_sum, max_sum)
        return max_sum