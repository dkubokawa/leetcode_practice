"""
Leetcode 141 (Easy): Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by
continuously following the next pointer. Internally, pos is used to denote the index of the node
that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
"""

from typing import Optional
from python.linked_list.linked_list import ListNode

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        :param head: The head of the ListNode
        :return: bool: Returns if the Nodes form a cycle

        Implementation: Use two pointers a slow and a fast pointer. We exit if we reach the end, which indicates
            that we do not have a cycle. Or when slow=fast, which can only occur if we have a cycle.
        Time Complexity: O(n) since we may iterate over the full list (if no cycle occurs)
        Space Complexity:  O(1) since we are using no additional memory
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False