#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BinarySearchTreeNode:
    
    def __init__(self,
                 value: int,
                 left_value: int = None,
                 right_value: int = None) -> None:
        self._value = value
        self.left_child: 'BinarySearchTreeNode' = None
        self.right_child: 'BinarySearchTreeNode' = None
        if left_value is not None:
            self.left_child = BinarySearchTreeNode(value=left_value)
        if right_value is not None:
            self.right_child = BinarySearchTreeNode(value=right_value)
        
    def get_value(self) -> int:
        return self._value
    
    def set_left_child(self, value: int) -> None:
        self.left_child = BinarySearchTreeNode(value=value)
    
    def set_right_child(self, value: int) -> None:
        self.right_child = BinarySearchTreeNode(value=value)
    
    def __repr__(self) -> str:
        return 'BinarySearchTreeNode()'
    
    def __str__(self) -> str:
        return str(self.get_value())

class BinarySearchTree:
    
    def __init__(self):
        self._root_node = None
        
    def is_empty(self) -> bool:
        if self._root_node is None:
            return True
        return False
