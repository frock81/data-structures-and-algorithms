#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List, Optional


def insertion_sort(sorting_list: List[int], size: int) -> List:
    for i in range(1, size):
        key = sorting_list[i]
        j = i-1
        while j>=0 and sorting_list[j] > key:
            sorting_list[j+1] = sorting_list[j]
            j = j - 1
        sorting_list[j+1] = key
    return sorting_list


def selection_sort(sorting_list: List[int], size: int) -> List:
    for i in range(size):
        min_index = i
        for j in range(i+1, size):
            if sorting_list[j] < sorting_list[min_index]:
                min_index = j
        key = sorting_list[i]
        sorting_list[i] = sorting_list[min_index]
        sorting_list[min_index] = key
    return sorting_list


def bubble_sort(sorting_list: List[int],
                size: int,
                variant: str = 'left') -> List:
    return globals()[f'bubble_sort_{variant}'](
        sorting_list=sorting_list, size=size)


def bubble_sort_right(sorting_list: List[int], size: int) -> List:
    temp = None
    for i in range(size-1, 0, -1):
        j = i
        # Invariante do laço interno: o valor à direita de j é sempre
        # maior ou Nil.
        for j in range(size-1, 0, -1):
            if sorting_list[j-1] > sorting_list[j]:
                temp = sorting_list[j]
                sorting_list[j] = sorting_list[j-1]
                sorting_list[j-1] = temp
    return sorting_list


def bubble_sort_left(sorting_list: List[int], size: int) -> List:
    temp = None
    for i in range(size-1):
        j = i
        # Invariante do loop interno: o valor à esquerda de j é sempre
        # menor ou Nil
        for j in range(size-1):
            if sorting_list[j] > sorting_list[j+1]:
                temp = sorting_list[j]
                sorting_list[j] = sorting_list[j+1]
                sorting_list[j+1] = temp
    return sorting_list


def merge_sort(sorting_list: Optional[List[int]],
               size: int) -> List:
    if sorting_list is None:
        return []
    if size == 1:
        return sorting_list
    half = size // 2
    left_size = half
    right_size = size - half
    left = sorting_list[:half]
    right = sorting_list[half:]
    left = merge_sort(sorting_list=left, size=left_size)
    right = merge_sort(sorting_list=right, size=right_size)
    return merge(left, left_size, right, right_size)


def merge(left: List[int],
          left_size: int,
          right: List[int],
          right_size: int) -> List[int]:
    merged = []
    merged_size = 0
    while left_size > 0 and right_size > 0:
        # <= for stability (i guess)
        if left[0] <= right[0]:
            merged.append(left.pop(0))
            merged_size += 1
            left_size -= 1
            continue
        merged.append(right.pop(0))
        merged_size += 1
        right_size -= 1
    while left_size > 0:
        merged.append(left.pop(0))
        merged_size += 1
        left_size -= 1
    while right_size > 0:
        merged.append(right.pop(0))
        merged_size += 1
        right_size -= 1
    return merged
