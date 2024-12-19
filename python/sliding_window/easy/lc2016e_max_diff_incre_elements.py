# LC 2016 (Easy): Maximum Difference Between Increasing Elements
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # Variable length Sliding Window
        # Time-Complexity: O(n) makes a single pass through the list
        # Space-Complexity: O(1) uses constant space
        start = 0
        max_diff = -1
        curr_diff = 0
        for end in range(len(nums)):
            curr_diff = nums[end] - nums[start]
            if nums[end] < nums[start]:
                start = end
            max_diff = max(max_diff, curr_diff)

        # Case where there are two elements that are the same (i.e. no diff), instructions say to return -1
        if max_diff == 0:
            return -1
        else:
            return max_diff