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


def selection_sort(sorting_list: List) -> List:
    for i in range(len(sorting_list)):
        min_index = i
        key = sorting_list[i]
        for j in range(i + 1, len(sorting_list)):
            if sorting_list[j] < sorting_list[min_index]:
                min_index = j
        sorting_list[i] = sorting_list[min_index]
        sorting_list[min_index] = key
    return sorting_list
