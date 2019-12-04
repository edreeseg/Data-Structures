import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
            # Because we will only ever have to add and remove elements from the head (or tail) of our list, no need for other access.
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size+=1
        self.storage.add_to_head(value)

    def pop(self):
        if self.storage:
            self.size-=1
            return self.storage.remove_from_head()

    def len(self):
        return self.size
