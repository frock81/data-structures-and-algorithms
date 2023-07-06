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
DELETION_RATE = 0.5


def get_inclusion_and_excluded_lists() -> None:
    random.seed(SEED)
    insertion_list = []
    all_set = set()
    for i in range(SAMPLES):
        # Allow duplicates
        insertion_list.append(random.randint(0,SAMPLES))
        all_set.add(i)
    excluded_list = list(all_set - set(insertion_list))
    return insertion_list, excluded_list


def get_comment_prefix():
    return '# '


def print_h1_delimiter() -> None:
    print(get_comment_prefix() + "=" * 70)


def print_h1(text: str) -> None:
    print("\n")
    print_h1_delimiter()
    print(f"{get_comment_prefix()}{text.upper()}")
    print_h1_delimiter()
    print()


def test_creation_and_initialization() -> None:
    bst = BinarySearchTree()
    bstNode = BinarySearchTreeNode(0)
    bstNode = BinarySearchTreeNode(0,1)
    bstNode = BinarySearchTreeNode(0,1,2)


def test_search(bst: BinarySearchTree,
                included_list: list[int],
                excluded_list: list[int]) -> None:
    for included in included_list:
        assert bst.contains(included)
        print(f'Tree contains {included}')
    print('All contains assertions passed.')
    for excluded in excluded_list:
        assert not bst.contains(excluded)
        print(f'Tree does not contain {excluded}')
    print('All not contains assertions passed.')
    print("Search (contains) test passed!")


def test_insertion(bst: BinarySearchTree, insertion_list: list[int]) -> None:
    for i in insertion_list:
        bst.insert(i)


def test_traverse(bst: BinarySearchTree) -> None:
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


def calculate_the_amount_to_remove() -> int:
    """Calculate the amount to remove

    Calculate the amount of entries to remove from the included list
    based on samples size and deletion rate.
    """
    return round(SAMPLES * DELETION_RATE) - 1


def get_positions_to_be_removed() -> list[int]:
    """Return a list of positions to be removed

    Return a list of positions to be removed from the list of included
    values in the list. The positions are chosen randomly from 0 to the
    size of the amount to remove minus one. As we are not being strict,
    the random values can repeat.
    """
    amount_to_remove = calculate_the_amount_to_remove()
    positions = set()
    for _ in range(amount_to_remove):
        positions.add(random.randint(0, amount_to_remove))
    return list(positions)

def get_values_from_included_to_be_deleted(
        included_list: list[int]
    ) -> None:
    print("Included_list:")
    print(str(included_list) + "\n")
    positions_to_be_removed = get_positions_to_be_removed()
    print("Positions to be removed:")
    print(f"{positions_to_be_removed}\n")
    return ([included_list[x] for x in range(len(included_list))
             if x in positions_to_be_removed])

def test_deletion(bst: BinarySearchTree, included_list: list[int]) -> None:
    for_deletion_values = get_values_from_included_to_be_deleted(
        included_list)
    print("Valores a serem excluídos da árvore")
    print(for_deletion_values)


def test_operations() -> None:
    bst = BinarySearchTree()
    print_h1('INSERTION TEST')
    insertion_list, excluded_list = get_inclusion_and_excluded_lists()
    test_insertion(bst=bst, insertion_list=insertion_list)
    print_h1('TRAVERSAL TEST')
    print("Empty BST:")
    test_traverse(BinarySearchTree())
    print("\nNot empty BST:")
    test_traverse(bst)
    print_h1('SEARCH TEST')
    test_search(bst=bst,
                included_list=list(set(insertion_list)),
                excluded_list=excluded_list)
    print_h1('DELETION TEST')
    test_deletion(bst=bst, included_list=insertion_list)


if __name__ == '__main__':
    test_creation_and_initialization()
    test_operations()
