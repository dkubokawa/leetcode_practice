# Leetcode 1431 (Easy): Kids With the Greatest Number of Candies
from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        :param candies: list of integers representing the number of candies each kid has
        :param extraCandies: integer representing the number of extra candies you have
        :return: list of booleans representing whether each kid can have the greatest number of candies
        Implementation:
            - Find the max number of candies in the list
            - Iterate through the list and add extraCandies to each kid's number of candies
        Time complexity: O(n) because we iterate through the list of length n
        Space complexity: O(n) because we create a new list of length n
        """

        max_amt = max(candies)
        return_list = []
        for candy in candies:
            return_list.append(candy + extraCandies >= max_amt)
        return return_list
