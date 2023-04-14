"""
You are given an integer array height of length n. There are n vertical lines
drawn such that the two endpoints of the iᵗʰ line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the
container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,
3,7]. In this case, the max area of water (blue section) the container can
contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 10⁵
0 <= height[i] <= 10⁴
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        :type height: List[int] the list of heights
        :return: int the max area
        Implementation:
         Use two pointers, one at the beginning and one at the end of the list
         Calculate the area of the container
         Move the pointer with the smaller height
         Repeat until the two pointers meet
        Time Complexity: O(n) since we only iterate through the list once
        Space Complexity: O(1) since we only use three variables
        """
        if len(height) < 2:
            return 0

        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            min_height = min(height[left], height[right])
            width = right - left
            max_area = max(max_area, min_height * width)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
