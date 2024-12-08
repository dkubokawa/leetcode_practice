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
### [036. Valid Sudoku](https://leetcode.com/problems/valid-sudoku)
#### Description
<!-- description:start -->
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
* Each row must contain the digits 1-9 without repetition. 
* Each column must contain the digits 1-9 without repetition. 
* Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:
* A Sudoku board (partially filled) could be valid but is not necessarily solvable. 
* Only the filled cells need to be validated according to the mentioned rules.
<!-- description:end -->

#### Tags
Array, Hash-Table, Matrix

#### Example: 
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

#### Approach
##### Solution 1: OOP problem: O(N)
* Treat as an object orientated programming problem and define methods to check all the validation conditions 
* A valid Sudoku board has all valid_rows, valid_cols, and valid_squares
```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid(values: List[str]) -> bool:
            nums = []
            for v in values:
                if v != '.':
                    nums.append(v)
            return len(nums) == len(set(nums))

        def is_valid_row(board):
            for r in board:
                if not is_valid(r):
                    return False
            return True
        
        def is_valid_col(board) -> bool:
            for c in zip(*board):
                if not is_valid(c):
                    return False
            return True

        def is_valid_square(board) -> bool:
            corners = (0, 3, 6)
            for row_index in corners:
                for col_index in corners:
                    square = []
                    for i in range(row_index, row_index + 3):
                        for j in range(col_index, col_index + 3):
                            square.append(board[i][j])
                    if not is_valid(square):
                        return False
            return True

        def is_valid_sudoku(board) -> bool:
            if is_valid_row(board) and is_valid_col(board) and is_valid_square(board):
                return True
            return False

        return is_valid_sudoku(board)
```

### [049. Group Anagrams](https://leetcode.com/problems/group-anagrams)
#### Description
<!-- description:start -->
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
<!-- description:end -->

#### Tags
Array, Hash Table, Matrix

#### Example: 
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
* There is no string in strs that can be rearranged to form "bat". 
* The strings "nat" and "tan" are anagrams as they can be rearranged to form each other. 
* The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

#### Approach
##### Solution 1: Hashmap: O(N)
* Traverse the string array, sort each string in character dictionary order to get a new string.
* Use the new string as key and [str] as value, and store them in the hash table
* When encountering the same key during subsequent traversal, add it to the corresponding to the list.
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time-Complexity: O(m*nlogn) because sorting is nlogn times m-strings
        # Space-Complexity: O(m*n) because we use O(n) for the dict
        anagrams = collections.defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            anagrams[sorted_s].append(s)
        return list(anagrams.values())
```

### [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence)
#### Description
<!-- description:start -->
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
<!-- description:end -->

#### Tags
Union Find, Array, Hash Table

#### Example: 
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Thus, the length is 4.

#### Approach
##### Solution 1: Brute-Force: O(N^2)
* Create a set out of the input list, which removes the duplicates 
* Iterate over every number in the hashset. For the start of each number, use a while loop to scan the entire array looking for the next integer
* Keep a streak variable that keeps the current streak we are on
```python
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time-Complexity: O(n^2) because w.c. scan twice i.e. [1, 2, ..., n]
        # Space-Complexity: O(n) because length of n for the set
        nums_set = set(nums)
        result = 0
        for n in nums:
            curr = n
            streak = 0
            while curr in nums_set:
                streak += 1
                curr += 1
            result = max(streak, result)
        return result
```

##### Solution 2: Hash Set: O(N)
* Same setup as the brute-force method, but do not double scan the set.
* We check that the previous number is not in the hashset, since if the previous number is in the hashset, that would have a greater streak than the current number
```python
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time-Complexity: O(2N) = O(N) because we visit each number at most twice
        #   This would be for [1, 2, ..., n] we visit once in the for loop, once in the while loop
        #   But it is not O(N^2) since we exit if we find the prev in the set (i.e. we saw it already!)
        # Space-Complexity: O(n) because length of n for the set
        # The optimization is to check the previous number, since we DO not want to recount
        nums_set = set(nums)
        result = 0
        for n in nums:
            if n - 1 not in nums_set:
                streak = 0
                while n + streak in nums_set:
                    streak += 1
                result = max(streak, result)
        return result
```

### [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self)
#### Description
<!-- description:start -->
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
<!-- description:end -->

#### Tags
Array, Prefix Sum

#### Example: 
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

#### Approach
##### Solution 1: Brute-Force: O(N^2)
* Brute Force, so use two for loops to iterate over all the possible values.
* We skip if the indices are the same, since we are looking for product except for self
```python
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time-Complexity: O(n^2) because we loop twice
        # Space-Complexity: O(n) because we store n-results in a List
        results = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                product = product * nums[j]
            results.append(product)
        return results
```

##### Solution 2: With Division: O(N)
* Fails the constraint if we cannot use division
* On the first-pass, we keep track of the product of all values (except for zeros) and the amount of zeros in the array
* We can return early if there are more than 1 zero, since the entire array will always be all zeros for > 1
* If there is exactly one zero in the array, we handle that case, since at the index of the zero, it will be the product. But 0 everywhere else.
```python
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time-Complexity: O(n + n) = O(2n) = O(n)
        # Space-Complexity: O(n) since we store a results array of length n
        product = 1
        num_of_zeroes = 0
        for index, value in enumerate(nums):
            if value == 0:
                num_of_zeroes = num_of_zeroes + 1
            else:
                product = product * value
        if num_of_zeroes > 1:
            return [0] * len(nums)
        
        results = [0] * len(nums)
        for index, value in enumerate(nums):
            if num_of_zeroes == 1:
                if value == 0:
                    results[index] = product
                else:
                    results[index] = 0
            else:
                results[index] = product // value
        return results
```

##### Solution 3: Prefix Sum: O(N)
* We define two variables prefix and postfix , which represent the product of all elements to the left and right of the current element respectively. 
* Initially, prefix = postfix = 1. We also keep an results array of length n.
* We first traverse the array from left to right, for the i-th element we update results[i] with prefix, then update prefix for the next number by multiplying it by the current number.
* Then, we traverse the array from right to left, for the i-th element, we update results[i] to results[i] * postifx, then update postfix by multiplying by the current number.
* After the traversal, the array results is the answer.
```python
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time-Complexity: O(n+n) = O(2n) = O(n)
        # Space-Complexity: O(n) since we keep a results array
        n = len(nums)
        results = [0] * n
        prefix = postfix = 1
        for i, x in enumerate(nums):
            results[i] = prefix
            prefix = prefix * x
        for i in range(n - 1, -1, -1):
            results[i] = results[i] * postfix
            postfix = postfix * nums[i]
        return results
```

### [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements)
#### Description
<!-- description:start -->
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
<!-- description:end -->

#### Tags
Array, Hash Table, Divide and Conquer, Bucket Sort, Counting, Quick Sort, Heap (Priority Queue)

#### Example: 
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

#### Approach
##### Solution 1: Sorting: O(nlogn)
* First use a hashmap to get the frequencies/counts of each number. Alt: use collections.Counter() 
* We then build a List[cnt, num] to make it easier to sort. Alt: could use a lambda function
* Finally, we build a results array. We pop off the end of the list, since we are sorted in increasing order, so the most frequent are at the top of the list
```python
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time-Complexity: O(n + n + nlogn + n) = O(3n + nlogn) = O(nlogn)
        # Space-Complexity: O(n + n + n) = O(3n) = O(n)

        nums_map: Dict[int, int] = {}
        for n in nums:
            nums_map[n] = 1 + nums_map.get(n, 0)
        
        cnt_nums = []
        for value, count in nums_map.items():
            cnt_nums.append([count, value])
        cnt_nums.sort()
        
        results = []
        for i in range(k):
            count, value = cnt_nums.pop()
            results.append(value)
        return results
```

##### Solution 2: Bucket Sort: O(n)
* Instead of a List that we need to sort, use bucket sort and build a List of Lists ahead of time
* Note: this form: freq = [[] for i in range(len(nums) + 1)] since we are creating a list of lists
* We know that at most we will have len(nums) + 1 indices, since the 0 index will be unused. If all the same number, we would have cnt of = n, where n is the length of the list.
* Finally, we build a results array. We pop off the end of the list, since we are sorted in increasing order, so the most frequent are at the top of the list
```python
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Need the + 1 because for a list we really dont use the 0 index
        # Use the fact that the index implies the count of the objects!
        # Ex: list of length 2, we will have one object twice, or two different objects once
        # i.e. [7, 7] would be [[], [], [7]] and [6, 7] would be [[], [6, 7], []] 
        freq = [[] for i in range(len(nums) + 1)]
        count = {}
        
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        results = []
        # Our stop can be end=0 (or index 1) since we will not have values in index 0
        for i in range(len(freq) - 1, 0, -1):
            # We skip over the empty indices, since we will not evaluate a num for an empty list
            for num in freq[i]:
                results.append(num)
                if len(results) == k:
                    return results
```