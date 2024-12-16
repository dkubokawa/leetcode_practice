## LC Problems Solved
### Difficulty: Easy
* N/A

### Difficulty: Medium
* [45. Jump Game II](https://leetcode.com/problems/jump-game-ii)
* [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray)
* [55. Jump Game](https://leetcode.com/problems/jump-game)
* [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self)



## LC Medium - Solution and Notes
### [45. Jump Game II](https://leetcode.com/problems/jump-game-ii)
#### Description
<!-- description:start -->
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
* 0 <= j <= nums[i] and 
* i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
<!-- description:end -->

#### Tags
Array, Dynamic Programming, Greedy

#### Lists
* Neetcode 150

#### Example: 
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

#### Approach
##### Solution 1: Greedy Algorithm: O(N)
* Implement a Breadth First Search greedy algorithm using 2 Pointers
* We mark the interval set by [l, r] as the window of possible locations we can jump to
* For every object in that interval, we calculate the next possible furthest jump
* On each pass (breadth) we move the ptrs and update min_jumps by 1
```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        # Greedy Algorithm roughly implementing Breadth First Search
        # Time-Complexity: O(n)
        # Space-Complexity: O(1)
        
        l = r = 0
        min_jumps = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            min_jumps += 1
        return min_jumps
```

### [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray)
#### Description
<!-- description:start -->
Given an integer array nums, find the subarray with the largest sum, and return its sum.
<!-- description:end -->

#### Tags
Array, Divide and Conquer, Dynamic Programming, Greedy

#### Lists
* Blind 75, Neetcode 150

#### Example: 
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

#### Approach
##### Solution 1: Brute Force: O(N^2)
* Implement the Naive Approach by using two <code>for</code> loops to find EVERY subarray
```python
  def maxSubArray(self, nums: List[int]) -> int:
        # Brute-Force Approach
        # Time-Complexity: O(n^2)
        # Space-Complexity: O(1)
        max_sum = nums[0]
        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
            max_sum = max(curr_sum, max_sum)
        return max_sum
```

##### Solution 2: Greedy/Kadane's Algorithm/aka Bottom-Up Dynamic Programming : O(N)
* Use Kadane's Algorithm, a Greedy Algorithm, that is similiar to approaching using Bottom-Up Dynamic Programming
* We make use of the fact that we would never use a subarray that sums to less than 0, since we are looking for the max of the array
  * i.e. [1, -3, 4, ...] we can discard the [1, -3 ...] portion since it sums to -2
  * The max sum will never include that portion, especially since the idx=2 has a positive value
* This simple fact allows us to use a single <code>for</code> loop and a single pass
```python
    def maxSubArray(self, nums: List[int]) -> int:
        # Greedy (Kadane's Algorithm) Approach
        # Also a Bottom-Up Dynamic Programming Approach
        # Time-Complexity: O(n)
        # Space-Complexity: O(1)
        max_sum = float("-inf")
        curr_sum = 0
        for i in range(len(nums)):
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += nums[i]
            max_sum = max(curr_sum, max_sum)
        return max_sum
```


### [55. Jump Game](https://leetcode.com/problems/jump-game)
#### Description
<!-- description:start -->
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
<!-- description:end -->

#### Tags
Array, Dynamic Programming, Greedy

#### Lists
* Blind 75, Neetcode 150

#### Example: 
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

#### Approach
##### Solution 1: Greedy Algorithm: O(N)
* Work backwards from the 2nd to last index in a for loop
* We know the goal is the last index, so we check if the 2nd to last index + its jump value can reach the goal
* If it can, then we set it as the new goal (since if we can get here we can get to the end), then continue the loop
```python
    def canJump(self, nums: List[int]) -> bool:
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
```

##### Solution 2: Greedy/Kadane's Algorithm/aka Bottom-Up Dynamic Programming : O(N)
* Similiar to the first solution but think about the "reach" of how far we can jump
* Only update reach if the current jump value is greater than the stored value of reach
* Decrement reach as we move through the array
```python
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
```

### [134. Gas Station](https://leetcode.com/problems/gas-station)
#### Description
<!-- description:start -->
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.
<!-- description:end -->

#### Tags
Array, Greedy

#### Lists
* Neetcode 150

#### Example: 
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

#### Approach
##### Solution 1: Greedy Algorithm: O(N)
* Calculate totals, since at each index, we gain +gas and lose -cost
* This works partially because we know there is a unique solution to be found
* If we have a negative total at the current index, move the result to the next index and reset total, since it cannot be the solution
* Is considered a greedy solution because if we cannot fill at one of the current station, we go to the next station, because at the current index, all previous indices will have the same problem.
```python
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
```

##### Solution 2: Greedy Algorithm: O(N)
* Alt: Slightly better format
```python
  def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost):
      return -1
  
    start, fuel = 0, 0
    for i in range(len(gas)):
      if fuel + gas[i] - cost[i] < 0:
        # can't reach next station:
        # try starting from next station
        start, fuel = i + 1, 0
      else:
        # can reach next station:
        # update remaining fuel
        fuel += gas[i] - cost[i]
  
    return start
```