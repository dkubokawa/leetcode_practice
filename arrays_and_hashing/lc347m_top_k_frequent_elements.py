"""
Leetcode 347 (Medium): Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent
elements. You may return the answer in any order.


 Example 1:
 Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

 Example 2:
 Input: nums = [1], k = 1
Output: [1]


 Constraints:


 1 <= nums.length <= 10⁵
 -10⁴ <= nums[i] <= 10⁴
 k is in the range [1, the number of unique elements in the array].
 It is guaranteed that the answer is unique.



 Follow up: Your algorithm's time complexity must be better than O(n log n),
where n is the array's size.
"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        :param List[int] nums: List of integers to search
        :param int k: Number of most frequent elements to return
        :return: List[int]: List of k most frequent elements in nums
        Implementation:
            Build a hashmap to store the frequency of each element. Time O(n) and space O(n).
            Then sort the hashmap by value in descending order. Time O(nlogn) and space O(n).
            Finally, return the first k elements. Time O(k) and space O(k).
        The total time complexity is O(nlogn) because O(n) + O(nlogn) + O(k) = O(nlogn).
        The total space complexity is O(n) because O(n) + O(n) + O(k) = O(n).
        """

        # Build a hashmap to store the frequency of each element
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        # Sort the hashmap based on the values
        sorted_hashmap = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)

        # Return the first k elements
        return [sorted_hashmap[i][0] for i in range(k)]
