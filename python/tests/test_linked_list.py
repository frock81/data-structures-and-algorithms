#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os


# DEPRECATED: using PYTHONPATH in .envrc
# sys.path.append(os.path.dirname(os.path.abspath(__file__)) + f'{os.sep}..')


from dsa.linked_list import LinkedList, OutOfBoundsException


def test_linked_list_insert_last():
    linked_list = LinkedList()
    linked_list.insert_last(1)
    linked_list.insert_last(1)
    linked_list.insert_last(3)
    linked_list.insert_last(5)
    linked_list.insert_last(8)
    linked_list.insert_last(13)
    linked_list.insert_last(21)


def test_linked_list_insert_first():
    linked_list = LinkedList()
    linked_list.insert_first(1)
    linked_list.insert_first(1)
    linked_list.insert_first(3)
    linked_list.insert_first(5)
    linked_list.insert_first(8)
    linked_list.insert_first(13)
    linked_list.insert_first(21)


def test_linked_list_insert_at():
    linked_list = LinkedList()
    try:
        linked_list.insert_at(1, 101)
    except OutOfBoundsException as e:
        pass
    linked_list.insert_at(0, 100)
    linked_list.insert_at(3, 103)
    linked_list.insert_at(5, 105)
    linked_list.insert_at(8, 108)

def test_linked_list_traverse():
    linked_list = LinkedList()
    linked_list.insert_last(1)
    linked_list.insert_last(1)
    linked_list.insert_last(3)
    linked_list.insert_last(5)
    linked_list.insert_last(8)
    linked_list.insert_last(13)
    linked_list.insert_last(21)
    linked_list.traverse(print)



if __name__ == '__main__':
    test_linked_list_insert_last()
    test_linked_list_insert_first()
    test_linked_list_insert_at()
    test_linked_list_traverse()
