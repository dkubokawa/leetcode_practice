class Solution:
    def climbStairs(self, n: int) -> int:
        # Solution 4: Bottom-up - Tabulation Approach - Space Optimized (DP)
        # Time: O(n)
        # Space: O(1)
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev = 1
        curr = 2
        for i in range(2, n):
            prev, curr = curr, prev + curr
        return curr

    def climbStairs1(self, n: int) -> int:
        # Solution 1: Recursive
        # Time: O(2^n)
        # Space: O(n)
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-2) + self.climbStairs(n-1)

    def climbStairs2(self, n: int) -> int:
        # Solution 2: Top-Down Approach - Memoization (DP)
        # Time: O(n)
        # Space: O(n)

        memo = {
            1:1,
            2:2
        }
        def f(n: int):
            if n in memo:
                return memo[n]
            else:
                memo[n] = f(n-2) + f(n-1)
                return memo[n]
        return f(n)

    def climbStairs3(self, n: int) -> int:
        # Solution 3: Bottom-up - Tabulation Approach (DP)
        # Time: O(n)
        # Space: O(n)
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n-1]
