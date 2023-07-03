#!/usr/bin/env python
# -*- coding: utf-8 -*-

print('Importing linked_list.py...')


class OutOfBoundsException(Exception):
    
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class LinkedListNode():

    def __init__(self, value: int) -> None:
        self._value = value
        self._next: 'LinkedListNode' = None
        
    def set_next(self, node: 'LinkedListNode') -> None:
        self._next = node
        
    def get_next(self) -> 'LinkedListNode':
        return self._next


class LinkedList():
    
    def __init__(self) -> None:
        self._first_node = None
    
    def insert_last(self, value: int):
        insert_node = LinkedListNode(value)
        if self.is_empty():
            self._first_node = insert_node
            return
        previous_node = self._first_node
        while(previous_node.get_next() != None):
            previous_node = previous_node.get_next()
        previous_node.set_next(insert_node)
        
    def insert_first(self, value: int):
        insert_node = LinkedListNode(value)
        if self.is_empty():
            self._first_node = insert_node
        insert_node.set_next(self._first_node)
        self._first_node = insert_node
        
    def insert_at(self, position: int, value: int) -> None:
        if self.is_empty() and position != 0:
            raise OutOfBoundsException
        insert_node = LinkedListNode(value)
        if position == 0:
            self.insert_first(insert_node)
        previous_node = self._first_node
        i = 0
        while i < position:
            if previous_node.get_next() == None:
                raise OutOfBoundsException()
            previous_node = previous_node.get_next()
            i = i + 1
        if previous_node.get_next() == None:
            previous_node.set_next(insert_node)
            return
        insert_node.set_next(previous_node.get_next())
        previous_node.set_next(insert_node)
        
    def is_empty(self):
        if self._first_node == None:
            return True
        return False


if __name__ == '__main__':
    print('Main on linked_list.py executed!')
