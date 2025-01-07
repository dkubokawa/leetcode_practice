# LC1884M: Egg Drop with 2 Eggs and N Floors

class Solution:
    def twoEggDrop(self, n: int) -> int:
        # Memoization dictionary to store results of subproblems for optimization
        memo = {}

        # Recursive helper function to calculate minimum moves
        def getMin(numFloors, numEggs):
            # Base case 1: Only one floor left, takes exactly 1 drop to test it
            if numFloors == 1:
                return 1

            # Base case 2: Only one egg left, we must test each floor sequentially
            # So it takes numFloors drops in the worst case (1 drop per floor)
            if numEggs == 1:
                return numFloors

            # Check if this subproblem was previously solved
            if (numFloors, numEggs) in memo:
                return memo[(numFloors, numEggs)]

            # Initialize minimum moves to a large number for comparison
            minimum_moves = math.inf

            # Try dropping from each floor (1 through numFloors)
            for current_floor in range(1, numFloors + 1):
                # Case 1: Egg breaks -> we need to test floors below (i-1) with one less egg
                # + 1 accounts for the current drop
                moves_if_broke = 1 + getMin(current_floor - 1, numEggs - 1)

                # Case 2: Egg doesn't break -> we need to test floors above (numFloors - i)
                # with the same number of eggs
                # + 1 accounts for the current drop
                moves_if_not_broke = 1 + getMin(numFloors - current_floor, numEggs)

                # We take the maximum of the two cases because we're trying to minimize
                # the worst-case number of drops
                worst_case_moves = max(moves_if_broke, moves_if_not_broke)

                # Update minimum moves with the smallest worst-case scenario
                minimum_moves = min(minimum_moves, worst_case_moves)

            # Memoize the result for this specific combination of floors and eggs
            memo[(numFloors, numEggs)] = minimum_moves

            return minimum_moves

        # Start the calculation with n floors and 2 eggs
        return getMin(n, 2)