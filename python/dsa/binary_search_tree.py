#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import Any, Callable


class BinarySearchTreeNode:
    
    def __init__(self,
                 value: int,
                 left_value: int = None,
                 right_value: int = None) -> None:
        self._value = value
        self._left_child: 'BinarySearchTreeNode' = None
        self._right_child: 'BinarySearchTreeNode' = None
        if left_value is not None:
            self._left_child = BinarySearchTreeNode(value=left_value)
        if right_value is not None:
            self._right_child = BinarySearchTreeNode(value=right_value)
        
    def get_value(self) -> int:
        return self._value
    
    def set_left_child(self, bst_node: 'BinarySearchTreeNode') -> None:
        self._left_child = bst_node
        
    def get_left_child(self) -> 'BinarySearchTreeNode':
        return self._left_child
    
    def set_left_child_by_value(self, value: int) -> None:
        self._left_child = BinarySearchTreeNode(value=value)

    def get_left_child_value(self) -> int|None:
        if self._left_child is not None:
            return self._left_child.get_value()
        return None
    
    def set_right_child(self, bst_node: 'BinarySearchTreeNode') -> None:
        self._right_child = bst_node
        
    def get_right_child(self) -> 'BinarySearchTreeNode':
        return self._right_child
    
    def set_right_child_by_value(self, value: int) -> None:
        self._right_child = BinarySearchTreeNode(value=value)

    def get_right_child_value(self) -> int|None:
        if self._right_child is not None:
            return self._right_child.get_value()
        return None
        
    def traverse(self, callback_function: Callable):
        callback_function(self)
        if self._left_child is not None:
            self._left_child.traverse(callback_function)
        if self._right_child is not None:
            self._right_child.traverse(callback_function)
            
    def insert(self, insert_node: 'BinarySearchTreeNode') -> None:
        insert_value = insert_node.get_value()
        if insert_value == self._value:
            return
        if insert_value < self._value:
            left_child = self.get_left_child()
            if left_child is None:
                self.set_left_child(insert_node)
                return
            left_child.insert(insert_node)
        if insert_value > self._value:
            right_child = self.get_right_child()
            if right_child is None:
                self.set_right_child(insert_node)
                return
            right_child.insert(insert_node)
    
    def __repr__(self) -> str:
        return 'BinarySearchTreeNode()'
    
    def __str__(self) -> str:
        left_value: str = ''
        if self._left_child is not None:
            left_value = str(self._left_child.get_value())
        right_value: str = ''
        if self._right_child is not None:
            right_value = str(self._right_child.get_value())
        return str(f'node: "{self.get_value()}" ( left: "{left_value}" , '
                   f'right: "{right_value}" )')

class BinarySearchTree:
    
    def __init__(self):
        self._root_node = None
        
    def is_empty(self) -> bool:
        if self._root_node is None:
            return True
        return False
    
    def insert(self, value: int) -> bool:
        insert_node = BinarySearchTreeNode(value)
        if self.is_empty():
            self._root_node = insert_node
            return
        self._root_node.insert(insert_node)

    def traverse(self, callback_function: Callable):
        if self.is_empty():
            return
        self._root_node.traverse(callback_function)
