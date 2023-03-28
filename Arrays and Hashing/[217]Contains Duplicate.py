"""
Given an integer array nums, return true if any value appears at least twice
in the array, and return false if every element is distinct.

 Example 1:
 Input: nums = [1,2,3,1]
Output: true

 Example 2:
 Input: nums = [1,2,3,4]
Output: false

 Example 3:
 Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

 Constraints:
 1 <= nums.length <= 10⁵
 -10⁹ <= nums[i] <= 10⁹
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        :param List[int] nums: List of integers to check for duplicates
        :return: True if there are duplicates, False otherwise
        :rtype: bool
        Implementation: Use a set to store the numbers we've seen so far.
            If we find a number that is already in the set, we know we've seen it before and can return True.
            If we reach the end of the list and haven't found a duplicate, return False.
        Time Complexity: O(n) due to the for loop
        Space Complexity: O(n) due to the set
        """
        set_of_nums = set()
        for num in nums:
            if num in set_of_nums:
                return True
            set_of_nums.add(num)
        return False
        
# leetcode submit region end(Prohibit modification and deletion)
