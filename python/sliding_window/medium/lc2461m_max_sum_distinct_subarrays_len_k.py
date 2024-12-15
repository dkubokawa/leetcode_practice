# LC 2461 (Medium): Maximum Sum of Distinct Subarrays With Length K

from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # Fixed-Length Sliding Window
        # Time: O(n) because we make a single pass
        # Space: O(k) because we will store at most k-keys
        state = {} # k,v -> num, cnt
        start = 0
        max_sum = 0
        curr_sum = 0

        for end in range(len(nums)):
            # extend the window by adding nums[end]
            curr_num = nums[end]
            curr_sum += curr_num
            state[curr_num] = 1 + state.get(curr_num, 0)

            # Fill until we get a size subarray of length k
            if end - start + 1 == k:

                # only update max_sum if we have distinct values in our dict
                if len(state) == k:
                    max_sum = max(max_sum, curr_sum)

                # contract the window by removing nums[start]
                start_num = nums[start]
                curr_sum -= start_num
                state[start_num] -= 1
                if state[start_num] == 0:
                    del state[start_num]
                start += 1
        return max_sum