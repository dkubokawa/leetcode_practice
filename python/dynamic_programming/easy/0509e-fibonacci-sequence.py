class Solution:
    def fib0(self, n: int) -> int:
        # Initial attempt, without looking at solutions, using a generic loop
        if n == 0 or n == 1:
            return n
        first_num = 0
        second_num = 1
        for i in range(2, n + 1):
            next_num = first_num + second_num
            first_num = second_num
            second_num =  next_num
        return second_num

    def fib1(self, n: int) -> int:
        # Solution 1: Recursive approach
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-2) + self.fib(n-1)
    def fib2(self, n: int) -> int:
        # Solution 2: Top-Down Memoization Approach (DP)
        # Time: O(n), Space: O(n)
        # Top-Down b/c we are calculating from the top to the base case
        memo = {0:0, 1:1}
        def f(x: int):
            if x in memo:
                return memo[x]
            else:
                memo[x] = f(x-2) + f(x-1)
                return memo[x]
        return f(n)

    def fib3(self, n: int) -> int:
        # Solution 3: Bottom-Up (Tabulation) DP Approach
        # Create an array where we fill an array/table
        # [0 1 1 2 3 5 8 13] <- vals
        # [0 1 2 3 4 5 6 7 ] <- indices
        # Time: O(n), Space: O(n)
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]

    def fib4(self, n: int) -> int:
        # Solution 4: Bottom-Up DP with better space
        # Time: O(n), Space: O(1)
        if n == 0: return 0
        if n == 1: return 1
        prev = 0
        curr = 1
        for i in range(2, n + 1):
            prev, curr = curr, prev + curr
        return curr






