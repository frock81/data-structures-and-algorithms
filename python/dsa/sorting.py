#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def insertion_sort(sorting_list: List) -> List:
    for i in range(1, len(sorting_list)):
        key = sorting_list[i]
        j = i - 1
        while j>=0 and sorting_list[j] > key:
            sorting_list[j+1] = sorting_list[j]
            j = j - 1
        sorting_list[j+1] = key
    return sorting_list
