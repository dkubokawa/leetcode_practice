# LC 134 (Medium): Gas Station

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Greedy algorithm
        # Time-Complexity: O(n)
        # Space-cComplexity: O(1)
        if sum(gas) < sum(cost):
            return -1

        total = 0
        result = 0
        for i in range(len(gas)):
            total = total + gas[i] - cost[i]
            if total < 0:
                total = 0
                result = i + 1
        return result
