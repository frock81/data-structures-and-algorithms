#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List
import random
import os
import sys
from pprint import pprint


sys.path.append(os.path.dirname(os.path.abspath(__file__)) + f'{os.sep}..')


# from dsa.sorting import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, heap_sort
from dsa.sorting import insertion_sort


SEED = 12
SIZE = 25
FROM = 0
TO = 100


def print_heading(text, level):
    if level == 1:
        formatted_text = (
            f"\n{'#' + '=' * 72}"
            f"\n#  {text.upper()}\n"
            f"{'#' + '=' * 72}\n")
    elif level == 2:
        formatted_text = f"\n--- {text.capitalize()} ---"
    elif level == 3:
        formatted_text = f"\n> {text.title()} <"
    else:
        formatted_text = text
    print(formatted_text)


def prepare() -> List:
    """Return a random list to be sorted"""
    print_heading('prepare', 1)
    random.seed(SEED)
    to_be_sorted_list = []
    for i in range(SIZE):
        to_be_sorted_list.append(random.randint(FROM, TO))
    print('List to be sorted')
    pprint(to_be_sorted_list)
    return to_be_sorted_list


def test_sort(some_list: List) -> None:
    for index in range(len(some_list) - 1):
        assert some_list[index] <= some_list[index + 1]
        print(f"{some_list[index]} <= {some_list[index + 1]}")


def test_insertion_sort(to_be_sorted_list: List):
    print_heading('insertion sort', 1)
    sorted_list = insertion_sort(to_be_sorted_list)
    test_sort(sorted_list)


if __name__ == '__main__':
    to_be_sorted = prepare()
    # Test bubble sort
    # Test selection sort
    # Test insertion sort
    test_insertion_sort(to_be_sorted)
    # Test merge sort
    # Test quick sort
    # Test heap
    # Test radix