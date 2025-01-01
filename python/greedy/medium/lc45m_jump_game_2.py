# LC 45 (Medium): Jump Game II

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        # Greedy Algorithm roughly implementing Breadth First Search
        # Time-Complexity: O(n)
        # Space-Complexity: O(1)

        l = r = 0
        min_jumps = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            min_jumps += 1
        return min_jumps
