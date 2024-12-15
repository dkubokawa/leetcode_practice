## Sliding Window LC Problems
### Difficulty: Easy
* [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)
* [2016. Maximum Difference Between Increasing Elements](https://leetcode.com/problems/maximum-difference-between-increasing-elements)

### Difficulty: Medium
* [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters)
* [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement)
* [567. Permutation in String](https://leetcode.com/problems/permutation-in-string)
* [1423. Maximum Points You Can Obtain from Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards)
* [2461. Maximum Sum of Distinct Subarrays With Length K](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k)

### Difficulty: Hard
* [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring)
* [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum)

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
* Invalid Window condition:
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
* Invalid Window condition:
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
* Use a variable-length window to make a single pass through the array
* Invalid window condition: 
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
* Use a variable-length sliding window to make a single pass through the array
* Invalid window condition: 
  * when <code>(end - start + 1) - max_freq > k: </code> or when
  * window_len - max_freq > k (number of replacements allowed) we are invalid!
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

### [567. Permutation in String](https://leetcode.com/problems/permutation-in-string)
#### Description
<!-- description:start -->
Given two strings s1 and s2, return true if s2 contains a
permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.
<!-- description:end -->

#### Tags
Hash Table, Two Pointers, String, Sliding Window

#### Lists
* Neetcode 150

#### Example: 
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

#### Approach
##### Solution 1: Sliding Window: O(N)
* Use a fixed-length sliding window to make a single pass through the array
* Valid window condition: 
  * when <code>(end - start + 1) == len(s1: </code> or when
* We use a hashmap mapping the chars of s1 to counts
  * Alt: could use Counter() or s1_count = [0] * 26 and place in the array using: s1_count[ord(s1[i]) - ord('a')] += 1
* We use a sliding window a hashmap for the state of the window as we walk s2. 
* Exit early if we find a match, otherwise, need to update the state on every iteration. Need to delete the key if cnt falls to 0.
```python
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Fixed-Length Sliding Window
        # Time-Complexity: O(n)
        # Space-Complexity: O(2n) = O(n) because we use 2 hashmaps

        if len(s1) > len(s2):
            return False

        char_s1 = {}
        for value in s1:
            char_s1[value] = 1 + char_s1.get(value, 0)
        
        start = 0
        state = {}
        for end in range(len(s2)):
            state[s2[end]] = 1 + state.get(s2[end], 0)

            if end - start + 1 == len(s1):
                if state == char_s1:
                    return True
                state[s2[start]] -= 1
                if state[s2[start]] == 0:
                    del state[s2[start]]
                start += 1
        return False
```

### [1423. Maximum Points You Can Obtain from Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards)
#### Description
<!-- description:start -->
There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.
In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
Your score is the sum of the points of the cards you have taken.
Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
<!-- description:end -->

#### Tags
Array, Sliding Window, Prefix Sum

#### Lists
* N/A

#### Example: 
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. 
The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.

#### Approach
##### Solution 1: Sliding Window: O(N)
* Use a fixed-length sliding window to make a single pass through the array
* Valid Window condition: 
  * when <code>end - start + 1 == n - k</code> or when
  * window_len == number_of_discards (i.e. len(cardPoints) - cards_kept)
* Once we have a valid window, update the max and fix the state/start
* Corner case occurs when k >= n, since if we enter the algorithm we would get total_points = 0! Handle early. 
```python
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # Trick here is we can "discard" n - k cards
        # i.e. for cardPoints = [1,2,3,4,5,6,7], k = 3
        # our valid hands are [1,2,3], [1,6,7], [1,2,7], [5,6,7]  
        # so we discard a sliding window of length n - k = 4 cards
        # Time-Complexity: O(N)
        # Space-Complexity: O(1)

        total = sum(cardPoints)
        n = len(cardPoints)
        if k >= n:
            return total
        
        start = 0 
        state = 0
        max_window = 0
        for end in range(n):
            state += cardPoints[end]

            if end - start + 1 == n - k:
                max_window = max(max_window, total - state)
                state -= cardPoints[start]
                start += 1

        return max_window
```

### [2461. Maximum Sum of Distinct Subarrays With Length K](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k)
#### Description
<!-- description:start -->
You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:
* The length of the subarray is k, and
* All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.
A subarray is a contiguous non-empty sequence of elements within an array.
<!-- description:end -->

#### Tags
Array, Hash Table, Sliding Window

#### Lists
* N/A

#### Example: 
Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions
- 
#### Approach
##### Solution 1: Sliding Window: O(N)
* Use a fixed-length sliding window to make a single pass through the array
* Valid Window condition: 
  * when <code>end - start + 1 == k</code> or when we have a subarray of length k
* Can only update the max when have distinct values in the state dict
```python
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # Fixed-Length Sliding Window
        # Time: O(n) because we make a single pass
        # Space: O(k) because we will store at most k-keys
        state = {} # k,v -> num, cnt
        start = 0
        max_sum = 0
        curr_sum = 0

        for end in range(len(nums)):
            # extend the window by adding nums[end]
            curr_num = nums[end]
            curr_sum += curr_num
            state[curr_num] = 1 + state.get(curr_num, 0)

            # Fill until we get a size subarray of length k
            if end - start + 1 == k:

                # only update max_sum if we have distinct values in our dict
                if len(state) == k:
                    max_sum = max(max_sum, curr_sum)

                # contract the window by removing nums[start]
                start_num = nums[start]
                curr_sum -= start_num
                state[start_num] -= 1
                if state[start_num] == 0:
                    del state[start_num]
                start += 1
        return max_sum
```

## LC Hard - Solution and Notes
### [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring)
#### Description
<!-- description:start -->
Given two strings s and t of lengths m and n respectively, return the minimum window
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.
<!-- description:end -->

#### Tags
Hash Table, String, Sliding Window

#### Lists
* Blind 75, Neetcode 150

#### Example: 
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
- 
#### Approach
##### Solution 1: Sliding Window: O(N)
* Use a variable-length sliding window to make a single pass through the array
* Check Window condition: 
  * when <code>found == need</code> or we have a character match for the substr to the desired result
* Can only update the max when the current window is less than the min_window
* Otherwise, we update the state on every iteration
```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Variable-Length Sliding Window
        # Time-Complexity: O(n) where n is the length of s
        # Space-Complexity: O(m) is the total number of unique characters in t or s, whichever is greater
        if not s or not t:
            return ""

        # Use dictionary to track character frequencies
        count_t = {}
        for char in t:
            count_t[char] = 1 + count_t.get(char, 0)
        
         # Result tracking vars
        need = len(count_t)
        found = 0
        result_l_idx = None
        result_r_idx = None
        min_window = float('inf') # Need inf so any valid window is less than it

        # Window variables
        start = 0
        state = {} 

        for end in range(len(s)):
            # Expand window
            curr_char = s[end]
            state[curr_char] = 1 + state.get(curr_char, 0)

            # To check we have found all the chars in a window must have the same count
            if curr_char in count_t and state[curr_char] == count_t[curr_char]:
                found += 1
            
            # Once we have found chars == need chars, we have a valid window
            while found == need:
                start_char = s[start]
                
                # Update result if current window is smaller
                if end - start + 1 < min_window:
                    min_window = end - start + 1
                    result_l_idx = start
                    result_r_idx = end

                # Contract window
                state[start_char] -= 1
                # Do not have a count match for the character anymore
                if start_char in count_t and state[start_char] < count_t[start_char]:
                    found -= 1
                start += 1
        
        return "" if min_window == float('inf') else s[result_l_idx : result_r_idx + 1]
```

### [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum)
#### Description
<!-- description:start -->
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.
<!-- description:end -->

#### Tags
Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue

#### Lists
* Neetcode 150

#### Example: 
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

#### Approach
##### Solution 1: Brute Force: O(N^2)
* Can Brute Force by checking every substring and appending the results
```python
class Solution:
    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        # Brute-Force
        # Time-Complexity: O(n^2)
        # Space-Complexity: O(n)
        results = []
        for i in range(len(nums) - k + 1):
            window_max = nums[i]
            for j in range(i, i + k):
                window_max = max(nums[j], window_max)
            results.append(window_max)
        return results
```

##### Solution 2: Sliding Window: O(N)
* Use a fixed-length sliding window to make a single pass through the array
* Valid Window condition: 
  * when <code>end - start + 1 == k</code> 
* Use a monotonically decreasing double-ended queue storing the indices to keep local max as we move
* Monotonically decreasing because if for ex: [8 7 6 9], k = 3
  * state =  max is at index 0 -> [8 7 6] <- need to check the tail to check monotonically decr 
  * so if the currend number is GREATER then pop the queue 
  * EX: end = 0, state = [0 1 2] because val [8 7 6] is valid monotonically decr 
  * end = 1, state = [3] but we popped all the values since 9 >= [7 6] so no use holding them
  * But if for example it was [8 7 6 5] we would have want to keep [7 6 5] since max is still at the left

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Fixed-Length Sliding Window
        # Time-Complexity: O(n)
        # Space-Complexity: O(n)
        
        state = deque()  # Monotonic deque to store indices of useful elements
        start = 0
        max_result = []  # To store the maximums of each window

        for end in range(len(nums)):
            # Extend window: Maintain the monotonic decreasing property in the deque
            # Monotonically decreasing because if for ex: [8 7 6 9], k = 3 
            # state =  max is at index 0 -> [8 7 6] <- need to check the tail to check monotonically decr
            # so if the currend number is GREATER then pop the queue
            # EX: end = 0, state = [0 1 2] because val [8 7 6] is valid monotonically decr
            #     end = 1, state = [3] but we popped all the values since 9 >= [7 6] so no use holding them
            while state and nums[state[-1]] <= nums[end]:
                state.pop()
            state.append(end)

            # Remove elements not in the current window from the deque
            # Since we stored the indices, we use this to check if its in window bounds
            if state[0] < end - k + 1:
                state.popleft()

            # window length = k 
            if end - start + 1 == k:
                max_result.append(nums[state[0]])  # The front of the deque is the maximum
                # Contract window
                start += 1

        return max_result
```