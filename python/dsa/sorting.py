#!/usr/bin/env python
# -*- coding: utf-8 -*-


from utils.printing import print_heading
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
    print_heading(f'Até aqui', 3)
    print(f'sorting_list: {sorting_list}')
    print(f'size: {size}')
    sorted_left = None
    sorted_right = None
    if sorting_list is None:
        return [], 0
    if size == 1:
        return sorting_list, 1
    half = size // 2
    print(f'half: {half}')
    left = sorting_list[0:half]
    print(f'left: {left}')
    right = sorting_list[half:size]
    print(f'right: {right}')
    sorted_left, sorted_left_size = merge_sort(sorting_list=left, size=half)
    print(f"sorted left: {sorted_left}")
    sorted_right, sorted_right_size = merge_sort(sorting_list=right, size=size - half)
    print(f"sorted right: {sorted_right}")
    merged = []
    merged_size = 0
    while True:
        if sorted_left_size == 0 and sorted_right_size == 0:
            break
        if sorted_left_size == 0 and sorted_right_size != 0:
            merged.append(sorted_right.pop(0))
            merged_size = merged_size + 1
            sorted_right_size = sorted_right_size - 1
            if sorted_right_size == 0:
                break
            continue
        if sorted_left_size != 0 and sorted_right_size == 0:
            merged.append(sorted_left.pop(0))
            merged_size = merged_size + 1
            sorted_left_size = sorted_left_size - 1
            if sorted_left_size == 0:
                break
            continue
        # <= for stability?
        if sorted_left[0] <= sorted_right[0]:
            merged.append(sorted_left[0])
            merged_size = merged_size + 1
            sorted_left.pop(0)
            sorted_left_size = sorted_left_size - 1
            continue
        merged.append(sorted_right[0])
        merged_size = merged_size + 1
        sorted_right.pop(0)
        sorted_right_size = sorted_right_size - 1
    return list(merged), merged_size
