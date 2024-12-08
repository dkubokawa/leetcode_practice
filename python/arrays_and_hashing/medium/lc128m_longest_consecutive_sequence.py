# LC 128 (Medium): Longest Consecutive Sequence
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        :param List[int] nums: Input list of numbers.
        :return int: the length of the longest sequence of consequctive integers
        Time Complexity: Average case: O(n + nlogn) = O(nlogn), since using a sort and traversing once.
        Space Complexity: Using sorted  is a solution with O(n). Since we are storing a second sorted list of numbers.
            Instead, make this O(1) by using the original list and sorting in place.
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        nums.sort()
        longest = 1
        current = 1
        for index, num in enumerate(nums):
            next_index = index + 1
            if next_index < len(nums):
                next_value = nums[next_index]
                if num == next_value:
                    continue
                elif num == next_value - 1:
                    current += 1
                    longest = max(current, longest)
                else:
                    current = 1
        return longest

        # """
        # :param List[int] nums: Input list of numbers.
        # :return int: the length of the longest sequence of consequctive integers
        # Time Complexity: O(2N) = O(N), since we visit each number at most twice.
        # Space Complexity: O(N). Since we are creating a set.
        # """
        # num_set = set(nums)
        # longest = 0
        # for n in nums:
        #     if n - 1 not in num_set:
        #         length = 0
        #         while n + length in num_set:
        #             length += 1
        #         longest = max(length, longest)
        # return longest
