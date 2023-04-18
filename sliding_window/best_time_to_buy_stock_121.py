from typing import List

def maxProfit(self, prices: List[int]) -> int:
    min_price = prices[0]
    profit = 0
    max_profit = 0

    for i in range(1, len(prices)):
        profit = prices[i] - min_price
        max_profit = max(profit, max_profit)
        min_price = min(min_price, prices[i])

    return max_profit