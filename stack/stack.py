import os
import sys
doubly_linked_path = os.path.normpath(os.path.join(__file__, '../../doubly_linked_list'))
sys.path.append(doubly_linked_path)
from doubly_linked_list import DoublyLinkedList, ListNode

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 
1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
#You can index and append arrays, whereas linked lists use nodes and connect to each value

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def __len__(self):
        return self.storage.length 

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size <= 0:
            return None
        self.size -= 1
        self.storage.remove_from_tail()
