# LC 239 (Hard): Sliding Window Maximum

from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Fixed-Length Sliding Window
        # Time-Complexity: O(n)
        # Space-Complexity: O(n)

        state = deque()  # Monotonic deque to store indices of useful elements
        start = 0
        max_result = []  # To store the maximums of each window

        for end in range(len(nums)):
            # Extend window: Maintain the monotonic decreasing property in the deque
            # Monotonically decreasing because if for ex: [8 7 6 9], k = 3
            # state =  max is at index 0 -> [8 7 6] <- need to check the tail to check monotonically decr
            # so if the currend number is GREATER then pop the queue
            # EX: end = 0, state = [0 1 2] because val [8 7 6] is valid monotonically decr
            #     end = 1, state = [3] but we popped all the values since 9 >= [7 6] so no use holding them
            while state and nums[state[-1]] <= nums[end]:
                state.pop()
            state.append(end)

            # Remove elements not in the current window from the deque
            # Since we stored the indices, we use this to check if its in window bounds
            if state[0] < end - k + 1:
                state.popleft()

            # window length = k
            if end - start + 1 == k:
                max_result.append(nums[state[0]])  # The front of the deque is the maximum
                # Contract window
                start += 1

        return max_result

    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        # Brute-Force
        # Time-Complexity: O(n^2)
        # Space-Complexity: O(n)
        results = []
        for i in range(len(nums) - k + 1):
            window_max = nums[i]
            for j in range(i, i + k):
                window_max = max(nums[j], window_max)
            results.append(window_max)
        return results