#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import Tuple
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


def print_h2_delimiter() -> None:
    print(get_comment_prefix() + "-" * 70)


def format_h1_text(text: str) -> str:
    return f"{get_comment_prefix()}{text.upper()}"


def print_h1(text: str) -> None:
    print()
    print_h1_delimiter()
    print(format_h1_text(text))
    print_h1_delimiter()
    print()


def format_h2(text: str) -> str:
    return f" :: {text.capitalize()}"


def print_h2(text: str, h1_text: str) -> None:
    print_h2_delimiter()
    print(f"{format_h1_text(h1_text)}{format_h2(text)}")
    print_h2_delimiter()
    print()


def print_h3_delimiter() -> None:
    print("*" * 50)


def print_h3(text: str, h1_text: str, h2_text: str) -> None:
    print_h3_delimiter()
    print(f"* {h1_text} :: {h2_text} :: {text} ")
    print_h3_delimiter()
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


def get_values_to_be_deleted(
        included_list: list[int]
    ) -> None:
    print("Included_list:")
    print(str(included_list) + "\n")
    positions_to_be_removed = get_positions_to_be_removed()
    print("Positions to be removed:")
    print(f"{positions_to_be_removed}\n")
    return ([included_list[x] for x in range(len(included_list))
             if x in positions_to_be_removed])


def get_keeped_values(included_list: list[int],
                      deletion_list: list[int]) -> list[int]:
    return ([included_list[x]
             for x in range(len(included_list))
             if included_list[x] not in deletion_list])


def test_insertion_wrapper() -> tuple[BinarySearchTree, list[int], list[int]]:
    bst = BinarySearchTree()
    print_h1('INSERTION TEST')
    insertion_list, excluded_list = get_inclusion_and_excluded_lists()
    test_insertion(bst=bst, insertion_list=insertion_list)
    print("Nodes inserted into the tree structure.\n")
    return bst, insertion_list, excluded_list


def test_traverse_wrapper(bst: BinarySearchTree) -> None:
    print_h1('TRAVERSAL TEST')
    print("Empty BST:")
    test_traverse(BinarySearchTree())
    print("\nNon empty BST:")
    test_traverse(bst)
    print("Tree traversed.\n")


def test_search_wrapper(bst: BinarySearchTree,
                        included_list: list[int],
                        excluded_list: list[int]) -> None:
    print_h1('SEARCH TEST')
    test_search(bst=bst,
                included_list=list(set(included_list)),
                excluded_list=excluded_list)
    print("Search (contains) test passed.\n")


def test_sort(bst: BinarySearchTree) -> None:
    sorted_list = bst.sort()
    for index in range(len(sorted_list) - 1):
        assert sorted_list[index] <= sorted_list[index + 1]
        print(f"{sorted_list[index]} <= {sorted_list[index + 1]}")


def test_sort_reverse(bst: BinarySearchTree) -> None:
    sorted_list = bst.sort(reverse=True)
    for index in range(len(sorted_list) - 1):
        assert sorted_list[index] >= sorted_list[index + 1]
        print(f"{sorted_list[index]} >= {sorted_list[index + 1]}")


def test_sort_wrapper(bst: BinarySearchTree) -> None:
    print_h1('SORT TEST')
    test_sort(bst=bst)
    print("Sort test passed.\n")
    test_sort_reverse(bst=bst)
    print("Reversed Sort test passed.\n")


def real_test_find_max(bst: BinarySearchTree,
                       included_list: List[int]) -> None:
    bst.traverse(print)
    print(included_list)
    assert bst.find_max() == max(included_list)


def test_find_max_wrapper(bst: BinarySearchTree,
                          included_list: List[int]) -> None:
    h1_text = 'find max'
    print_h1(f'{h1_text} test')
    real_test_find_max(bst, included_list)
    print(f"{h1_text} tests passed".capitalize())


def test_count(bst: BinarySearchTree, included_list: List[int]) -> None:
    bst_count = bst.count()
    # insertion_list may have duplicated values.
    assert bst_count == len(list(set(included_list)))
    print(f"BST count as expected: {bst_count}")


def test_count_wrapper(bst: BinarySearchTree, included_list: List[int]) -> None:
    print_h1('COUNT TEST')
    test_count(bst=bst, included_list=included_list)
    print("Count test passed.\n")


def real_test_deletion(bst: BinarySearchTree,
                       removal_list: List[int],
                       remaining_list: List[int],
                       removed_list: List[int],
                       msg: str = '') -> None:
    deletion_value = removal_list.pop(0)
    remaining_list.remove(deletion_value)
    removed_list.append(deletion_value)
    bst.delete(deletion_value)
    print(f"Selective tree after deleting {deletion_value}:")
    bst.traverse(print)
    assert bst.count() == len(remaining_list)
    for value in remaining_list:
        assert bst.contains(value)
    for value in removed_list:
        assert not bst.contains(value)
    test_sort(bst)
    print("Sort test passed")
    test_sort_reverse(bst)
    print("Reversed sort test passed")


def test_deletion_prepare(insertion_list) -> BinarySearchTree:
    bst = BinarySearchTree()
    for value in insertion_list:
        bst.insert(value)
    print("Selective tree after insertions (preorder):")
    bst.traverse(print)
    assert bst.count() == len(insertion_list)
    return bst


def test_deletion_no_children() -> None:
    '''
    |   1   | 1   | 1 | vazio |
    |  / \  |  \  |   |       |
    | 0   2 |   2 |   |       |
    '''
    insertion_list = [1, 0, 2]
    removal_list = [0, 2, 1]
    removed_list = []

    h2_text = "no children"
    print_h2(h1_text="deletion", text=h2_text)

    h3_text = "prepare/insertions"
    print_h3(h1_text="deletion",
             h2_text=h2_text,
             text=h3_text)
    bst = test_deletion_prepare(insertion_list)
    print(f"deletion, {h2_text}, {h3_text} assertions tests passed\n"
          .capitalize())

    h3_text = 'left'
    print_h3(h1_text="deletion",
             h2_text=h2_text,
             text=h3_text)
    real_test_deletion(bst,
                       remaining_list=insertion_list,
                       removal_list=removal_list,
                       removed_list=removed_list)
    print(f"deletion, {h2_text}, {h3_text} assertions tests passed\n"
          .capitalize())

    h3_text = 'right'
    real_test_deletion(bst,
                       remaining_list=insertion_list,
                       removal_list=removal_list,
                       removed_list=removed_list)
    print(f"deletion, {h2_text}, {h3_text} assertions tests passed\n"
          .capitalize())

    h3_text = "root"
    print_h3(h1_text="deletion",
             h2_text=h2_text,
             text=h3_text)
    real_test_deletion(bst,
                       remaining_list=insertion_list,
                       removal_list=removal_list,
                       removed_list=removed_list)
    print(f"deletion, {h2_text}, {h3_text} assertions tests passed\n"
          .capitalize())


def test_deletion_single_child_left() -> None:
    '''
    |     3 |   3 |   3 | 1 |
    |    /  |  /  |  /  |   |
    |   2   | 0   | 1   |   |
    |  /    |  \  |     |   |
    | 0     |   1 |     |   |
    |  \    |     |     |   |
    |   1   |     |     |   |
    '''
    insertion_list = [3, 2, 0, 1]
    removal_list = [2, 0, 3]
    removed_list = []

    h2_text = "single child left"
    print_h2(h1_text="deletion", text=h2_text)

    h3_text = "prepare/insertions"
    print_h3(h1_text="deletion",
             h2_text=h2_text,
             text=h3_text)
    bst = test_deletion_prepare(insertion_list)
    print(f"deletion, {h2_text}, {h3_text} assertions tests passed\n"
          .capitalize())

    h3_text = 'left'
    print_h3(h1_text="deletion",
             h2_text=h2_text,
             text=h3_text)
    real_test_deletion(bst,
                       remaining_list=insertion_list,
                       removal_list=removal_list,
                       removed_list=removed_list)
    print(f"deletion, {h2_text}, {h3_text} assertions tests passed\n"
          .capitalize())

    h3_text = 'right'
    real_test_deletion(bst,
                       remaining_list=insertion_list,
                       removal_list=removal_list,
                       removed_list=removed_list)
    print(f"deletion, {h2_text}, {h3_text} assertions tests passed\n"
          .capitalize())

    h3_text = "root"
    print_h3(h1_text="deletion",
             h2_text=h2_text,
             text=h3_text)
    real_test_deletion(bst,
                       remaining_list=insertion_list,
                       removal_list=removal_list,
                       removed_list=removed_list)
    print(f"deletion, {h2_text}, {h3_text} assertions tests passed\n"
          .capitalize())


def test_deletion_single_child_right() -> None:
    '''
    | 0     | 0     | 0   | 2 |
    |  \    |  \    |  \  |   |
    |   1   |   1   |   2 |   |
    |    \  |    \  |     |   |
    |     3 |     2 |     |   |
    |     / |       |     |   |
    |    2  |       |     |   |
    '''
    insertion_list = [0, 1, 3, 2]
    removal_list = [3, 1, 0]
    removed_list = []
    h2_text = "single child right"
    print_h2(h1_text="deletion", text=h2_text)

    h3_text = "prepare/insertions"
    print_h3(h1_text="deletion",
             h2_text=h2_text,
             text=h3_text)
    bst = test_deletion_prepare(insertion_list)
    print(f"deletion, {h2_text}, {h3_text} assertions tests passed\n"
          .capitalize())

    h3_text = 'left'
    print_h3(h1_text="deletion",
             h2_text=h2_text,
             text=h3_text)
    real_test_deletion(bst,
                       remaining_list=insertion_list,
                       removal_list=removal_list,
                       removed_list=removed_list)
    print(f"deletion, {h2_text}, {h3_text} assertions tests passed\n"
          .capitalize())

    h3_text = 'right'
    real_test_deletion(bst,
                       remaining_list=insertion_list,
                       removal_list=removal_list,
                       removed_list=removed_list)
    print(f"deletion, {h2_text}, {h3_text} assertions tests passed\n"
          .capitalize())

    h3_text = "root"
    print_h3(h1_text="deletion",
             h2_text=h2_text,
             text=h3_text)
    real_test_deletion(bst,
                       remaining_list=insertion_list,
                       removal_list=removal_list,
                       removed_list=removed_list)
    print(f"deletion, {h2_text}, {h3_text} assertions tests passed\n"
          .capitalize())

def test_deletion_single_child() -> None:
    test_deletion_single_child_left()
    test_deletion_single_child_right()


def test_deletion_couple_children() -> None:
    '''
          5       |     5       |     5       |     4       |
         / \      |    / \      |    / \      |    / \      |
        4   6     |   4   6     |   4   6     |   1   6     |
       /     \    |  /     \    |  /     \    |    \   \    |
      2       8   | 1       8   | 1       7   |     3   7   |
     / \     / \  |  \     / \  |  \       \  |          \  |
    1   3   7   9 |   3   7   9 |   3       9 |           9 |
    '''
    insertion_list = [5, 4, 2, 1, 3, 6, 8, 7, 9]
    removal_list = [2, 8, 5]
    removed_list = []
    h2_text = "couple"
    print_h2(h1_text="deletion", text=h2_text)

    h3_text = "prepare/insertions"
    print_h3(h1_text="deletion",
             h2_text=h2_text,
             text=h3_text)
    bst = test_deletion_prepare(insertion_list)
    print(f"deletion, {h2_text}, {h3_text} assertions tests passed\n"
          .capitalize())

    h3_text = 'left'
    print_h3(h1_text="deletion",
             h2_text=h2_text,
             text=h3_text)
    real_test_deletion(bst,
                       remaining_list=insertion_list,
                       removal_list=removal_list,
                       removed_list=removed_list)
    print(f"deletion, {h2_text}, {h3_text} assertions tests passed\n"
          .capitalize())

    raise NotImplementedError()


def test_selected_deletion() -> None:
    test_deletion_no_children()
    test_deletion_single_child()
    test_deletion_couple_children()


def test_random_deletion(bst: BinarySearchTree, included_list: list[int]) -> None:
    print("Tree before deletion:")
    bst.traverse(print)
    print()
    for_deletion_values = get_values_to_be_deleted(
        included_list)
    print("Valores a serem excluídos da árvore")
    print(f"{for_deletion_values}\n")
    for value_to_be_deleted in for_deletion_values:
        print(f"Deleting value {value_to_be_deleted}")
        bst.delete(value=value_to_be_deleted)
        assert not bst.contains(value_to_be_deleted)
    print("\nTree after deletion:")
    bst.traverse(print)
    print()
    keeped_values = get_keeped_values(included_list=included_list,
                                      deletion_list=for_deletion_values)
    for keeped_value in keeped_values:
        assert bst.contains(keeped_value)
    print("All delete assertions passed.")


def test_deletion(bst: BinarySearchTree, included_list: List[int]) -> None:
    test_selected_deletion()
    test_random_deletion(bst, included_list)


def test_deletion_wrapper(bst, included_list) -> None:
    print_h1('DELETION TEST')
    test_deletion(bst=bst, included_list=included_list)


def test_operations() -> None:
    bst: BinarySearchTree
    insertion_list: list[int]
    excluded_list: list[int]
    bst, insertion_list, excluded_list = test_insertion_wrapper()
    test_traverse_wrapper(bst=bst)
    test_sort_wrapper(bst=bst)
    test_find_max_wrapper(bst=bst, included_list=insertion_list)
    test_count_wrapper(bst=bst, included_list=insertion_list)
    test_search_wrapper(bst=bst,
                        included_list=insertion_list,
                        excluded_list=excluded_list)
    test_deletion_wrapper(bst=bst, included_list=insertion_list)


if __name__ == '__main__':
    test_creation_and_initialization()
    test_operations()
