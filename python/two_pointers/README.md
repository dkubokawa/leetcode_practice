## LC Problems Solved
### Difficulty: Easy
* [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome)

### Difficulty: Medium
* [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
* [15. 3Sum](https://leetcode.com/problems/3sum)

## LC Easy - Solution and Notes
### [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome)
#### Description
<!-- description:start -->
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
<!-- description:end -->

#### Tags
Two Pointers, String

#### Lists
* Blind 75, Neetcode 150, LC Top Interview 150

#### Example: 
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

#### Approach
##### Solution 1: Two Pointers: O(n)
* Use Two Pointers. Start Left Pointer at index 0, Right Pointer at the Len(n) - 1 aka the End
* Note: Use <code>.isalnum()</code> string method to check if a character is not 'a' through 'z' and move the ptr if it is not
* Note: Use <code>.lower()</code> string method to check for string equivalence, since lower 'a' != upper 'A'.
```python
    def isPalindrome(self, s: str) -> bool:
        # Time Complexity: O(n) since we will only iterate through the string once
        # Space Complexity: O(1) since we are not using any extra space
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
```

## LC Medium - Solution and Notes
### [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
#### Description
<!-- description:start -->
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
<!-- description:end -->

#### Tags
Arrays, Two Pointers, Greedy

#### Lists
* Blind 75, Neetcode 150, LC Top Interview 150

#### Example: 
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water  the container can contain is 49 = 7 * (8-1) = 7 * 7

#### Approach
##### Solution 1: Brute Force: O(n^2)
* Use two <code>for</code> loops to iterate over every pair in the array heights
* Keep and return a max_area variable that is compared to the current area calculation, only keeping the max

```python
    def maxArea(self, height: List[int]) -> int:
        # Approach: Brute-Force, loop over every iteration
        # Time: O(n^2) since 2 for loops
        # Space: O(1)
        max_area = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                min_height = min(height[i], height[j])
                width = j - i
                curr_area = min_height * width
                max_area = max(max_area, curr_area)
        return max_area
```

##### Solution 2: Sort and then use Two Pointers: O(n^2)
* Use Two Pointers. Start Left Pointer at index 0, Right Pointer at the Len(n) - 1 aka the End
* Do not move the ptr if its the higher of the two heights. This allows us to visit each value in height only once
```python
    def maxArea(self, height: List[int]) -> int:
        # Approach: Traverse the list once using ptrs
        # Time: O(n) since we visit every number at most once
        # Space: O(1)
        max_area = 0
        l = 0
        r = len(height) - 1
        while l < r:
            min_height = min(height[l], height[r])
            width = r - l
            curr_area = min_height * width
            max_area = max(max_area, curr_area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
```

### [15. 3Sum](https://leetcode.com/problems/3sum)
#### Description
<!-- description:start -->
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
<!-- description:end -->

#### Tags
Arrays, Two Pointers, Sorting

#### Lists
* Blind 75, Neetcode 150, LC Top Interview 150

#### Example: 
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

#### Approach
##### Solution 1: Brute Force: O(n^3)
* Use a set to keep the unique results
* Still need to sort the nums array because (-1, 0, 1) and (1, 0, -1) would show up as different unique triples. But, sorting puts all the negative values left of zero, positive right of zero, etc.
* Add the triples pair as a tuple, since lists are unhashable. But re-put into a list when returning results. 
```python
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triples = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]
                        triples.add(tuple(tmp))
        results = [list(i) for i in triples]
        return results
```

##### Solution 2: Sort and then use Two Pointers: O(n^2)
* Use a for-loop and two-pointers. Can use two pointers, since after sorting, we know if we need to increase or decrease our values to get the total_sum = 0
* Early break for if the current value at nums[i] > 0, this implies we can stop enumerating, since we cannot sum to 0
* Also <code>continue</code> the for loop if the previous value is the same the current value. This implies we already added that triple to the results.
* Need to also remember to update the pointers of either j or k once we find a triple, otherwise we would keep endlessly looping.
```python
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time-Complexity: O(n^2), 1 for the outer loop, one for the inner while loop
        # Space-Complexity: O(n)
        triples = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]
                if total_sum > 0:
                    k -= 1
                elif total_sum < 0:
                    j += 1
                else: 
                    triples.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1
        return triples
```
