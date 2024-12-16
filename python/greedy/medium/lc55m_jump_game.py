# LC 55 (Medium): Jump Game
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy Algorithm
        # Time-Complexity: O(n)
        # Space-Complexity: O(1)
        reach = 0
        for jump in nums:
            if reach < 0:
                return False
            elif jump > reach:
                # Concept here is we only keep the larger of the jumps
                # So we can cover a larger range
                reach = jump
            reach -= 1
        return True

    def canJump1(self, nums: List[int]) -> bool:
        # Greedy Algorithm
        # Time-Complexity: O(n)
        # Space-Complexity: O(1)

        goal = len(nums) - 1

        # iterate backwards from 2nd to last element
        for i in range(len(nums) - 2, -1, -1):

            # if the current index plus the number there (the jump) allows us to get to the goal
            # we can move the goal to the current index
            # the idea being here that if we can reach the goal from this position, we can now move the goal
            # then we work backwards to see if we can reach it from the first index
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False
