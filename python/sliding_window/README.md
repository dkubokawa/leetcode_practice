## Sliding Window LC Problems
### Difficulty: Easy
* [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)
* [2016. Maximum Difference Between Increasing Elements](https://leetcode.com/problems/maximum-difference-between-increasing-elements)

### Difficulty: Medium
* [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters)
* [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement)


## LC Easy - Solution and Notes
### [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)
#### Description
<!-- description:start -->
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
<!-- description:end -->

#### Tags
Array, Dynamic Programming

#### Lists
* Blind 75, Neetcode 150

#### Example: 
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

#### Approach
##### Solution 1: Brute-Force: O(N^2)
* The naive approach is to test every element in the array. Use two <code>for</code> loops to iterate over all the values.

##### Solution 2: Sliding Window: O(N)
* Use a Sliding Window / Pointer approach to make a single pass through the array.
* Invalid Window:
  * Occurs when prices[end] < prices[start]
```python
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
```

### [2016. Maximum Difference Between Increasing Elements](https://leetcode.com/problems/maximum-difference-between-increasing-elements)
#### Description
<!-- description:start -->
Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].
Return the maximum difference. If no such i and j exists, return -1.
<!-- description:end -->

#### Tags
Array

#### Lists
* None

#### Example: 
Input: nums = [7,1,5,4]
Output: 4
Explanation:
The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid.

#### Approach
##### Solution 1: Sliding Window: O(N)
* Use a Sliding Window / Pointer approach to make a single pass through the array.
* Invalid Window:
  * Occurs when nums[end] < nums[start]
```python
    def maximumDifference(self, nums: List[int]) -> int:
        # Variable length Sliding Window 
        # Time-Complexity: O(n) makes a single pass through the list
        # Space-Complexity: O(1) uses constant space
        start = 0
        max_diff = -1
        curr_diff = 0
        for end in range(len(nums)):
            curr_diff = nums[end] - nums[start]
            if nums[end] < nums[start]:
                start = end
            max_diff = max(max_diff, curr_diff)

        # Case where there are two elements that are the same (i.e. no diff), instructions say to return -1
        if max_diff == 0:
            return -1
        else:
            return max_diff
```

## LC Medium - Solution and Notes
### [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters)
#### Description
<!-- description:start -->
Given a string s, find the length of the longest substring without repeating characters.
<!-- description:end -->

#### Tags
Hash Table, String, Sliding Window

#### Lists
* Blind 75, Grind 75, Neetcode 150

#### Example: 
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

#### Approach
##### Solution 1: Sliding Window: O(N)
* Use a variable-sliding window to make a single pass through the array
* Invalid window: 
  * <code>seen</code> hashmap has a value with a count > 1. 
  * This can only occur at <code>end</code> because we update on every iteration
* We fix the window by moving the index <code>start</code> past the duplicate value.
```python
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Variable-length Sliding Window
        # Time-Complexity: O(n)
        # Space-Complexity: O(n)
        
        # hashmap with k:v, value:cnt
        seen: Dict[int, int] = {}
        start = 0
        max_len = 0
        for end in range(len(s)):
            # extend the window
            seen[s[end]] = 1 + seen.get(s[end], 0)

            # state is invalid when we have char of cnt > 2
            while seen[s[end]] > 1:
                # handle by moving the start index so that it is past the point of the left-most duplicate index
                seen[s[start]] -= 1
                start += 1

            # know the state is valid, can update the max-length now
            # Compare to the current window length or end - start + 1
            max_len = max(max_len, end - start + 1)
        return max_len
```

### [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement)
#### Description
<!-- description:start -->
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.
<!-- description:end -->

#### Tags
Hash Table, String, Sliding Window

#### Lists
* Blind 75, Neetcode 150

#### Example: 
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

#### Approach
##### Solution 1: Sliding Window: O(N)
* Use a variable-sliding window to make a single pass through the array
* Invalid window: 
  * when <code>(end - start + 1) - max_freq > k: </code> or when
  * winow_len - max_freq > k (number of replacements allowed) we are invalid!
* We fix the window by moving the index <code>start</code> to a valid index where we fulfill a valid window
```python
    def characterReplacement(self, s: str, k: int) -> int:
        # Variable Length Sliding Window
        # Time-Complexity: O(N)
        # Space-Complexity: O(N) but technically O(26) = O(1) since we will at most store 26 keys for 26 letters 
        
        # state has k:v -> str:cnt within the window
        state = {}
        start = 0
        max_len = 0
        max_freq = 0
        for end in range(len(s)):
            # extend window
            state[s[end]] = state.get(s[end], 0) + 1
            
            # the most frequent char might be the latest addition
            max_freq = max(max_freq, state[s[end]])

            # (end - start + 1) is our current window length
            # win_len - max_freq is number of replacements needed to get a repeating substr
            # if win_len - max_freq > k (number of replacements allowed) we are invalid!
            while (end - start + 1) - max_freq > k:
                state[s[start]] -= 1
                start += 1

            # in a valid window, so can update max_len
            max_len = max(max_len, end - start + 1)
        return max_len
```