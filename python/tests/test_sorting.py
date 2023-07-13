#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List
import random
import os
import sys
from pprint import pprint


sys.path.append(f"{os.path.dirname(os.path.abspath(__file__))}{os.sep}..")
from dsa.sorting import (insertion_sort,
                         selection_sort,
                         bubble_sort)
from utils.printing import print_heading


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
    pprint(to_be_sorted_list)
    return to_be_sorted_list


def test_sort(some_list: List) -> None:
    for index in range(len(some_list) - 1):
        assert some_list[index] <= some_list[index + 1]
        print(f"{some_list[index]} <= {some_list[index + 1]}")


if __name__ == '__main__':
    to_be_sorted = prepare()
    algorithms = [
        'insertion',
        'selection',
        'bubble',
        # 'merge',
        # 'heap',
        # 'quick',
        # 'counting',
        # 'radix',
        # 'bucket'
    ]
    for algo in algorithms:
        function_name = f'{algo}_sort'
        print_heading(function_name, 1)
        test_sort(globals()[function_name](list(to_be_sorted), SIZE))
