from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time Complexity: O(logn)
        # Space Complexity: O(1)
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                # number is bigger, want to search left half
                r = m - 1
            elif nums[m] < target:
                # number too small, want to search the right half
                l = m + 1
            else:
                return m
        return -1