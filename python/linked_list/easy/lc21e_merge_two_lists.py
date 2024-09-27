from typing import Optional
from python.linked_list.linked_list import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        :param List[ListNode] list1: head node of list1
        :param List[ListNode] list2: head node of list2
        :return: List[ListNode]: head node of the merged combination of list1 and list2
        Implementation: Iterate over the LinkedLists while each has objects. Compare in place, moving the head obj
            as we iterate through both lists. Once one of the lists empties, append the other to the end of the combined list.
        Time Complexity: O(n + m) because we need to iterate over the combined length of list1 (len n) and list2 (len m)
        Space Complexity:  O(1) since we do not use additional memory
        """
        dummy = ListNode()
        head = dummy

        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next

        if list1:
            head.next = list1
        elif list2:
            head.next = list2

        return dummy.next