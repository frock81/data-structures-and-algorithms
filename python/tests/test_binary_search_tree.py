#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random
import os
import sys


sys.path.append(os.path.dirname(os.path.abspath(__file__)) + f'{os.sep}..')

from dsa.binary_search_tree import BinarySearchTree, BinarySearchTreeNode


def test_creation_and_initialization():
    bst = BinarySearchTree()
    bstNode = BinarySearchTreeNode(0)
    bstNode = BinarySearchTreeNode(0,1)
    bstNode = BinarySearchTreeNode(0,1,2)
    
def test_search(bst: BinarySearchTree):
    assert bst.contains(0)
    assert bst.contains(1)
    assert bst.contains(2)
    assert bst.contains(3)
    assert bst.contains(5)
    assert bst.contains(6)
    assert bst.contains(8)
    assert bst.contains(10)
    assert bst.contains(13)
    assert bst.contains(14)
    assert bst.contains(15)
    assert bst.contains(16)
    assert bst.contains(18)
    assert bst.contains(20)
    assert not bst.contains(4)
    assert not bst.contains(7)
    assert not bst.contains(9)
    assert not bst.contains(11)
    assert not bst.contains(12)
    assert not bst.contains(17)
    assert not bst.contains(19)
    assert not bst.contains(500)
    print("Search test passed!")

def test_insertion(bst: BinarySearchTree):
    print('Insert 2')
    bst.insert(2)
    print('Insert 1')
    bst.insert(1)
    print('Insert 3')
    bst.insert(3)
    random.seed(10)
    for _ in range(17):
        random_value = random.randint(0,20)
        print(f'Insert {random_value}')
        bst.insert(random_value)

def test_operations():
    bst = BinarySearchTree()
    print("Empty BST:")
    bst.traverse(print)
    test_insertion(bst)
    test_search(bst)
    print("\nNot empty BST:")
    bst.traverse(print)

if __name__ == '__main__':
    test_creation_and_initialization()
    test_operations()