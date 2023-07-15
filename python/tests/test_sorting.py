#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pprint import pprint
from typing import List
from utils.printing import print_heading
import dsa.sorting
import random
import sys


SEED = 12
SIZE = 25
FROM = 0
TO = 100


def prepare() -> List:
    """Return a random list to be sorted"""
    print_heading('prepare', 1)
    random.seed(SEED)
    to_be_sorted_list = []
    for i in range(SIZE):
        to_be_sorted_list.append(random.randint(FROM, TO))
    print('List to be sorted')
    print(to_be_sorted_list)
    return to_be_sorted_list


def test_sort(some_list: List) -> None:
    for index in range(len(some_list) - 1):
        assert some_list[index] <= some_list[index + 1]
        print(f"{some_list[index]} <= {some_list[index + 1]}")


def call_test(sort_algorithm: str, to_be_sorted: List) -> None:
    print_heading(sort_algorithm, 1)
    sorting_module = getattr(dsa.sorting, f'{sort_algorithm}_sort')
    sorted = sorting_module(list(to_be_sorted), SIZE)
    print_heading('Sorted list', 3)
    print(sorted)
    test_sort(sorted)


if __name__ == '__main__':
    implemented_algorithms = [
        'insertion',
        'selection',
        'bubble',
        'merge',
        # 'heap',
        # 'quick',
        # 'counting',
        # 'radix',
        # 'bucket'
    ]
    sort_algorithm = None
    if len(sys.argv) > 1:
        sort_algorithm = sys.argv[1]
        if sort_algorithm not in implemented_algorithms:
            print(f'Invalid algorithm: {sort_algorithm}. Saindo...')
            exit()
    to_be_sorted = prepare()
    if sort_algorithm:
        call_test(sort_algorithm, to_be_sorted)
        exit()
    for sort_algorithm in implemented_algorithms:
        call_test(sort_algorithm, to_be_sorted)
