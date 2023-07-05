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


def test_traverse():
    bst = BinarySearchTree()
    print("Empty BST:")
    bst.traverse(print)
    test_insertion(bst)
    print("\nNot empty BST:")
    bst.traverse(print)

if __name__ == '__main__':
    test_creation_and_initialization()
    test_traverse()