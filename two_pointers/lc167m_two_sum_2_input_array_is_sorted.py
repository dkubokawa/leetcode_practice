"""
Leetcode 167 (Medium): Two Sum II - Input array is sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target
number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1
 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an
integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not
use the same element twice.
Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We
return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We
return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We
return [1, 2].


Constraints:
2 <= numbers.length <= 3 * 10⁴
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        :param List[int] numbers: input array
        :param int target: the target sum
        :return: List[int, int]. Two indices of the two numbers that add up to target.
        Implementation:
            We use two pointers, one at the beginning and one at the end. We add the two numbers.
            If it is less than the target, we move the left pointer to the right.
            If it is greater than the target, we move the right pointer to the left.
            We keep doing this until we find the two numbers that add up to the target.
            We return the indices of the two numbers.
        Time Complexity: O(n) since we will only iterate through the array once
        Space Complexity: O(1) since we are not using any extra space
        """

        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                # Leetcode wants the index to start at 1. So we add 1 to both.
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
