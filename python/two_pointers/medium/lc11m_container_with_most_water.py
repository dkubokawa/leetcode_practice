# Leetcode 11 (Medium): Container With Most Water

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
