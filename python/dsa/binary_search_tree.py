#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import Callable, Literal, Optional, Union


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

    def set_value(self, value: int) -> None:
        self._value = value

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

    def get_child(self,
                  child_position: Literal['left', 'right']
                 ) -> 'BinarySearchTreeNode':
        attribute_name = f"_{child_position}_child"
        child = getattr(self, attribute_name)
        return child

    def set_child(self,
                  child_position: Literal['left', 'right'],
                  child: Optional['BinarySearchTreeNode']
                 ) -> Optional['BinarySearchTreeNode']:
        attribute_name = f"_{child_position}_child"
        setattr(self, attribute_name, child)

    def find_max(self):
        if self._right_child is not None:
            return self._right_child.find_max()
        return self._value

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

    def traverse_preorder(self, callback_function: Callable):
        callback_function(self)
        if self._left_child is not None:
            self._left_child.traverse_preorder(callback_function)
        if self._right_child is not None:
            self._right_child.traverse_preorder(callback_function)

    def traverse_inorder(self, callback_function: Callable):
        if self._left_child is not None:
            self._left_child.traverse_inorder(callback_function)
        callback_function(self)
        if self._right_child is not None:
            self._right_child.traverse_inorder(callback_function)

    def traverse_postorder(self, callback_function: Callable):
        if self._left_child is not None:
            self._left_child.traverse_postorder(callback_function)
        if self._right_child is not None:
            self._right_child.traverse_postorder(callback_function)
        callback_function(self)

    def traverse_preorder_reverse(self, callback_function: Callable):
        callback_function(self)
        if self._right_child is not None:
            self._right_child.traverse_preorder_reverse(callback_function)
        if self._left_child is not None:
            self._left_child.traverse_preorder_reverse(callback_function)

    def traverse_inorder_reverse(self, callback_function: Callable):
        if self._right_child is not None:
            self._right_child.traverse_inorder_reverse(callback_function)
        callback_function(self)
        if self._left_child is not None:
            self._left_child.traverse_inorder_reverse(callback_function)

    def traverse_postorder_reverse(self, callback_function: Callable):
        if self._right_child is not None:
            self._right_child.traverse_postorder_reverse(callback_function)
        if self._left_child is not None:
            self._left_child.traverse_postorder_reverse(callback_function)
        callback_function(self)

    def contains(self, search_value: int) -> bool:
        if self._value == search_value:
            return True
        if self._left_child is not None and search_value < self._value:
            return self._left_child.contains(search_value)
        if self._right_child is not None and search_value > self._value:
            return self._right_child.contains(search_value)
        return False

    def get_children_count(self) -> int:
        children_count = 0
        if self._left_child is not None:
            children_count = 1
        if self._right_child is not None:
            children_count= children_count + 1
        return children_count

    def get_single_child(self) -> 'BinarySearchTreeNode':
        if self._left_child is None:
            return self._right_child
        return self._left_child

    def search_children_for_removal(self, deletion_value: int) -> None:
        if self._value < deletion_value and self._right_child is not None:
            self._check_child_for_removal(deletion_value=deletion_value,
                                         child_position='right')
            return
        # By design we chose the max descendent from the left branch to replace
        # a node marked for removal. This would be different otherwise.
        self._check_child_for_removal(deletion_value=deletion_value,
                                      child_position='left')

    def _check_child_for_removal(self,
                                 deletion_value: int,
                                 child_position: Literal['left', 'right']
                                ) -> None:
        self_child = self.get_child(child_position)
        if self_child.get_value() == deletion_value:
            self._remove_child(child_position)
        else:
            self_child.search_children_for_removal(deletion_value)
    def _remove_child_with_no_children(self,
                                       child_position: Literal['left', 'right']
                                      ) -> None:
        self.set_child(child_position, None)

    def _remove_child_with_single_children(
        self,
        child_position: Literal['left', 'right']
    ) -> None:
        old_child = self.get_child(child_position)
        new_child = old_child.get_left_child()
        if new_child is None:
            new_child = old_child.get_right_child()
        self.set_child(child_position=child_position, child=new_child)

    def _remove_child(self, child_position: Literal['left', 'right']) -> None:
        children_count = self._get_self_child_children_count(child_position)
        if children_count == 0:
            self._remove_child_with_no_children(child_position)
        elif children_count == 1:
            self._remove_child_with_single_children(child_position)
        elif children_count == 2:
            left_max = (self.get_child(child_position).get_left_child()
                        .find_max())
            self.get_child(child_position).set_value(left_max)
            self.get_child(child_position).search_children_for_removal(left_max)

    def _get_self_child_children_count(self,
                                       child_position: Literal['left', 'right']
                                      ) -> int:
        self_child_children_count = 0
        self_child = self.get_child(child_position)
        if self_child.get_left_child() is not None:
            self_child_children_count = self_child_children_count + 1
        if self_child.get_right_child() is not None:
            self_child_children_count = self_child_children_count + 1
        return self_child_children_count

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

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, BinarySearchTreeNode):
            return False
        return self._value == __value.get_value()

class BinarySearchTree:

    def __init__(self):
        self._root_node: BinarySearchTreeNode = None

    def is_empty(self) -> bool:
        if self._root_node is None:
            return True
        return False

    def insert(self, value: int) -> bool:
        insert_node = BinarySearchTreeNode(value)
        if self._root_node is None:
            self._root_node = insert_node
            return
        self._root_node.insert(insert_node)

    def traverse(self,
                 callback_function: Callable,
                 order_prefix: str='pre',
                 reverse: bool = False):
        if self._root_node is None:
            return
        method_name = (f"traverse_{order_prefix}order"
                       f"{'_reverse' if reverse else ''}")
        traversal_method = self._root_node.__getattribute__(method_name)
        traversal_method(callback_function)

    def contains(self, value: int) -> bool:
        if self._root_node is None:
            return False
        return self._root_node.contains(value)

    def delete(self, value: int) -> None:
        if self._root_node is None:
            return
        if self._root_node.get_value() == value:
            self._delete_root_node()
        else:
            self._root_node.search_children_for_removal(value)

    def sort(self, reverse: bool = False) -> list[int]:
        values: list[int] = []
        def cb_append_values(node: BinarySearchTreeNode):
            values.append(node.get_value())
        if reverse:
            self.traverse(cb_append_values, order_prefix='in', reverse=True)
            return values
        self.traverse(cb_append_values, order_prefix='in')
        return values

    def count(self) -> int:
        if self.is_empty():
            return 0
        return len(self.sort())

    def find_max(self) -> Optional[int]:
        if self._root_node is None:
            return None
        return self._root_node.find_max()

    def _delete_root_node(self) -> None:
        children_count = self._root_node.get_children_count()
        if children_count == 0:
            self._root_node = None
            return
        if children_count == 1:
            self._root_node = self._root_node.get_single_child()
            return
        if children_count == 2:
            raise NotImplementedError()
        raise Exception("This point should never be reached: a root node with "
                        "more than two children")
