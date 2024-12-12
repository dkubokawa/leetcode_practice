# LC 347 (Medium): Top K Frequent Elements
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
