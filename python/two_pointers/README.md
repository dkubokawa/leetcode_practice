## LC Problems Solved
### Difficulty: Easy
* [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome)

### Difficulty: Medium


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