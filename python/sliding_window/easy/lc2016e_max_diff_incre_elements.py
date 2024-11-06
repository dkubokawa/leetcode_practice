class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return -1

        lowest_num = nums[0]
        max_diff = -1
        for i in range(1, len(nums)):
            lowest_num = min(nums[i], lowest_num)
            max_diff = max(nums[i] - lowest_num, max_diff)

        # Handles the case where our biggest diff is the same number. This case we return -1.
        if max_diff == 0:
            return -1
        return max_diff