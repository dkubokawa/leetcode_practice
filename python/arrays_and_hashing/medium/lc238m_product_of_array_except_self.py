# LC 238 (Medium): Product of Array Except Self
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        :type List[int] nums: List of numbers
        :return List[int] results: List of products of all numbers except the current number

        Implementation
        If we could use division, the solution is  simple. Could simply iterate through the array and
             divide the product by the current number.
        Because no division, do the same thing by using a prefix and postfix array. Every result will
            be the product of the prefix (numbers before) and postfix (numbers after).
            The prefix array at the current index will be the product of all the numbers before the current index.
            The postfix array at the current index will be the product of all the numbers after the current index.
        Time Complexity: O(2N) = O(N) because we iterate through the array twice
        Space Complexity: O(3N) = O(N) because we create three arrays, prefix, postfix, and results.
        """
        if len(nums) == 2:
            return [nums[1], nums[0]]
        if nums.count(0) > 1:
            return [0] * len(nums)

        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        prefix[0] = 1
        postfix[-1] = 1

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]

        return [prefix[i] * postfix[i] for i in range(len(nums))]
