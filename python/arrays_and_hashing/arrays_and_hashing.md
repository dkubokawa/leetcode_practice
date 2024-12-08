## LC Problems Solved
### Difficulty: Easy
* [001. Two Sum](https://leetcode.com/problems/two-sum)
* [026. Remove Duplicates From Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array)
* [066. Plus One](https://leetcode.com/problems/plus-one)
* [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate)
* [242. Valid Anagram](https://leetcode.com/problems/valid-anagram)
* [1431. Kids with Greatest Amount of Candy](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies)

### Difficulty: Medium
* [036. Valid Sudoku](https://leetcode.com/problems/valid-sudoku)
* [049. Group Anagrams](https://leetcode.com/problems/group-anagrams)
* [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence)
* [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self)
* [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements)


## LC Easy - Solution and Notes
### [001. Two Sum](https://leetcode.com/problems/two-sum)
#### Description
<!-- description:start -->
Given an array of integers <code>nums</code>&nbsp;and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.</p>
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
<!-- description:end -->

#### Tags
Array, Hash Table

#### Example: 
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Eplanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#### Approach
##### Solution 1: Brute-Force: O(N^2)
* The naive approach is to test every element in the array. Use two <code>for</code> loops to iterate over all the values.
```python
class Solution:
        # Time-Complexity: O(N^2)
        # Space-Complexity: O(1)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

##### Solution 2: Hashmap/Hashset O(N)
* A better approach is to use a hashmap to keep track of values we have visited. This allows us to perform only 1 pass. 
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time-Complexity: O(n)
        # Space-Complexity: O(n)
        if len(nums) < 2:
            return []
        nums_map: Dict[int, int] = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_map:
                return [nums_map[complement], i]
            nums_map[nums[i]] = i 
```

### [026. Remove Duplicates From Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array)
#### Description
<!-- description:start -->
Given an integer array <code>nums</code> sorted in <strong>non-decreasing order</strong>, remove the duplicates such that each unique element appears only <strong>once</strong>. The <strong>relative order</strong> of the elements should be kept the <strong>same</strong>. Then return <em>the number of unique elements in </em><code>nums</code>.
<!-- description:end -->

#### Tags
Array, Two Pointers

#### Example: 
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

#### Approach
##### Solution 1: One-Pass on the List: O(N)
* We use a variable k to record the current length of the processed array. Initially, k = 0 represents an empty array.
* Then we traverse the array from left to right. 
* For each element x we encounter, if k = 0 or x ≠ nums[k−1], we place x in the position of nums[k], and then increment k by 1 . 
* Otherwise, x is the same as nums[k−1], so we skip this element. Continue to traverse until the entire array is traversed.
* When the traversal ends, the first k elements in nums are the answer we are looking for, and k is the length.
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Time: O(n), since we are iterating over nums which has length n
        # Space: O(1), since we use constant space
        k = 0
        for x in nums:
            if k == 0 or x != nums[k - 1]:
                nums[k] = x
                k += 1
        return k
```

### [066. Plus One](https://leetcode.com/problems/plus-one)
#### Description
<!-- description:start -->
You are given a large integer represented as an integer array digits, where each digits[i] is the i-th digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
<!-- description:end -->

#### Tags
Array, Math

#### Example: 
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.  Incrementing by one gives 123 + 1 = 124.  Thus, the result should be [1,2,4].

#### Approach
##### Solution 1: Math
* We start traversing from the last element of the array, add one to the current element. 
* If the digit is a 9, then we set the digit to a zero (and we know we have a carry).
* Otherwise, we can add one to the last digit and return early.
* If we still haven't returned after traversing the array, it means that all elements in the array are 0 , and we need to insert a 1 at the beginning of the array.
```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Time-Complexity: O(n)
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        return [1] + digits
```

### [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate)
#### Description
<!-- description:start -->
Given an integer array <code>nums</code>, return <code>true</code> if any value appears at least twice in the array, and return <code>false</code> if every element is distinct.
<!-- description:end -->

#### Tags
Array, Hash Table, Sorting

#### Example: 
Input: nums = [1,2,3,1], Output: True
Explanation: The element 1 occurs at the indices 0 and 3.

#### Approach
##### Solution 1: Brute-Force: O(N^2)
* The naive approach is to test every element in the array. Use two <code>for</code> loops to iterate over all the values.
```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Time: O(n), iterate over n-length list in the for-loop
        # Space: O(n), storing n objects in the hashset
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
```

##### Solution 2: Hashmap/Hashset O(N)
* A better approach is to use a hashset (or hashmap) to keep track of values we have visited. This allows us to perform only 1 pass. 
```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Time: O(n^2), iterating over n*n objects in the nested for-loop
        # Space: O(1), using constant space
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```

### [242. Valid Anagram](https://leetcode.com/problems/valid-anagram)
#### Description
<!-- description:start -->
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
<!-- description:end -->

#### Tags
Hash Table, String, Sorting

#### Example: 
Input: s = "anagram", t = "nagaram", 
Output: true

#### Approach
##### Solution 1: Hashmap: O(n)
* Look to return early if the lengths of the strings are not equal
* Use a hashmap for string s, and a different hashmap for string t, fill these in a single <code>for</code> loop
* Check the contents of all the keys in hashmap of str s and verify that the key exists and has the same value 
* Alt: Could use the collections.Counter() structure, which counts frequency of characters/nums
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time-Complexity: O(2n) = O(n), loop twice of length n, reduces to O(n)
        # Space-Complexity: O(2n) = O(n), uses 2n additional memory, reduces to O(n)
        if len(s) != len(t):
            return False

        characters_s = {}
        characters_t = {}

        for i in range(len(s)):
            characters_s[s[i]] = characters_s.get(s[i], 0) + 1
            characters_t[t[i]] = characters_t.get(t[i], 0) + 1

        for key in characters_s:
            if key not in characters_t or characters_s[key] != characters_t[key]:
                return False
        return True
```

### [1431. Kids with Greatest Amount of Candy](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies)
#### Description
<!-- description:start -->
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
Note that multiple kids can have the greatest number of candies.
<!-- description:end -->

#### Tags
Array

#### Example: 
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

#### Approach
##### Solution 1: Array
* Take the max out of the candies, we use this for reference to check as a comparison after we give out candy
* Use a results array. For each kid we check if the candy + extraCandies >= the max, this evals to a boolean
```python
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Time complexity: O(n) because we iterate through the list of length n
        # Space complexity: O(n) because we create a new list of length n
        max_amt = max(candies)
        return_list = []
        for candy in candies:
            return_list.append(candy + extraCandies >= max_amt)
        return return_list
```

## LC Medium - Solution and Notes