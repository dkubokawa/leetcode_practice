# LC 121 (Easy): Best Time to Buy and Sell Stock

from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        # Sliding Window
        # Time-Complexity: O(n)
        # Space-Complexity: O(1)
        start = 0
        profit = 0
        max_profit = 0
        for end in range(len(prices)):
            profit = prices[end] - prices[start]
            if prices[end] < prices[start]:
                start = end
            max_profit = max(max_profit, profit)
        return max_profit

    def maxProfit1(self, prices: List[int]) -> int:
        """
        Dynamic Programming Method
        :param prices: List[int]: the price of a given stock on the iᵗʰ day
        :return max_profit int: the maximum profit you can achieve from this transaction
        Time Complexity: O(n) since we are iterating through the list once
        Space Complexity: O(1) since we are using two variables to store the min price and max profit
        """
        min_price = prices[0]
        max_profit = 0

        for index, value in enumerate(prices):
            if index == 0:
                continue
            profit = value - min_price
            max_profit = max(profit, max_profit)
            min_price = min(min_price, value)
        return max_profit
