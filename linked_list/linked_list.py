from typing import Optional


class ListNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value: int):
        new_node = ListNode(value)
        self.head = new_node 
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value: int):
        new_node = ListNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self) -> Optional[ListNode]:
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        
        curr = self.head
        prev = self.head
        while curr.next is not None:
            prev = curr
            curr = curr.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        return curr
