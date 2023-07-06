#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random
import os
import sys


sys.path.append(os.path.dirname(os.path.abspath(__file__)) + f'{os.sep}..')

from dsa.binary_search_tree import BinarySearchTree, BinarySearchTreeNode
from typing import List

SEED = 10
SAMPLES = 25


def get_inclusion_and_excluded_lists():
    random.seed(SEED)
    insertion_list = []
    all_set = set()
    for i in range(SAMPLES):
        # Allow duplicates
        insertion_list.append(random.randint(0,SAMPLES))
        all_set.add(i)
    excluded_list = list(all_set - set(insertion_list))
    return insertion_list, excluded_list
        


def test_creation_and_initialization():
    bst = BinarySearchTree()
    bstNode = BinarySearchTreeNode(0)
    bstNode = BinarySearchTreeNode(0,1)
    bstNode = BinarySearchTreeNode(0,1,2)
    
def test_search(bst: BinarySearchTree,
                included_list: list[int],
                excluded_list: list[int]):
    for included in included_list:
        assert bst.contains(included)
    for excluded in excluded_list:
        assert not bst.contains(excluded)
    print("Search test passed!")

def test_insertion(bst: BinarySearchTree, insertion_list: list[int]):
    for i in insertion_list:
        bst.insert(i)
    
def test_traverse(bst: BinarySearchTree):
    print("Preorder traversal...")
    bst.traverse(callback_function=print, order_prefix='pre')
    print("\nInorder traversal...")
    bst.traverse(callback_function=print, order_prefix='in')
    print("\nPostorder traversal...")
    bst.traverse(callback_function=print, order_prefix='post')
    print("\nPreorder reverse traversal...")
    bst.traverse(callback_function=print, order_prefix='pre', reverse=True)
    print("\nInorder reverse traversal...")
    bst.traverse(callback_function=print, order_prefix='in', reverse=True)
    print("\nPostorder reverse traversal...")
    bst.traverse(callback_function=print, order_prefix='post', reverse=True)
    

def test_operations():
    bst = BinarySearchTree()
    print("Empty BST:")
    test_traverse(bst)
    insertion_list, excluded_list = get_inclusion_and_excluded_lists()
    test_insertion(bst=bst, insertion_list=insertion_list)
    print("\nNot empty BST:")
    test_traverse(bst)
    test_search(bst=bst,
                included_list=list(set(insertion_list)),
                excluded_list=excluded_list)

if __name__ == '__main__':
    test_creation_and_initialization()
    test_operations()