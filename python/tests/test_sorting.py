#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pprint import pprint
from typing import List
from utils.printing import print_heading
import dsa.sorting
import random


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
        'merge',
        # 'heap',
        # 'quick',
        # 'counting',
        # 'radix',
        # 'bucket'
    ]
    for algo in algorithms:
        function_name = f'{algo}_sort'
        print_heading(function_name, 1)
        sorting_module = getattr(dsa.sorting, function_name)
        test_sort(sorting_module(list(to_be_sorted), SIZE))
