#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os


sys.path.append(os.path.dirname(os.path.abspath(__file__)) + f'{os.sep}..')

from dsa.binary_search_tree import BinarySearchTree, BinarySearchTreeNode


def test_creation_and_initialization():
    bst = BinarySearchTree()
    bstNode = BinarySearchTreeNode(0)
    bstNode = BinarySearchTreeNode(0,1)
    bstNode = BinarySearchTreeNode(0,1,2)

if __name__ == '__main__':
    pass