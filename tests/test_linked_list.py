from python.linked_list.linked_list import ListNode
from python.linked_list.easy.lc141e_linked_list_cycle import Solution as linked_list_cycle
from python.linked_list.easy.lc21e_merge_two_lists import Solution as merge_two_lists

def test_linked_list_cycle_simple():
    # Input: head = [3,2,0,-4], pos = 1, expect True
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    assert (True, linked_list_cycle().hasCycle(node1))

    node4.next = None
    assert (False, linked_list_cycle().hasCycle(node1))

def test_linked_list_cycle_edge_cases():
    # Input: head = [1,2], pos = 0, expect True
    node5 = ListNode(1)
    node6 = ListNode(2)
    node5.next = node6
    node6.next = node5
    assert (True, linked_list_cycle().hasCycle(node5))

def test_merge_two_lists_simple():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node3
    node2.next = node4
    merge = merge_two_lists().mergeTwoLists(node1, node2)
    result = []
    while merge is not None:
        result.append(merge.val)
        merge = merge.next
    assert [1,2,3,4] == result