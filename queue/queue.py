"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
import os
import sys
doubly_linked_path = os.path.normpath(os.path.join(__file__, '../../doubly_linked_list'))
sys.path.append(doubly_linked_path)
from doubly_linked_list import DoublyLinkedList, ListNode

# will not work with the TK import style, use CRTL+K S to save
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def __len__(self):
        return self.size
        # return len(self.storage)

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if not self.storage.head:
            return None
        else:
            self.size -= 1
            return self.storage.remove_from_head()
