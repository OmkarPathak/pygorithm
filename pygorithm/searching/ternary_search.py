'''
Author: OMKAR PATHAK
Created at: 26th August 2017

Time complexity: O(logn)

More Info: https://en.wikipedia.org/wiki/Ternary_search
'''
from __future__ import division
import inspect

def search(_list, left, right, target):
    if right >= left:
        mid1 = (left + right) // 3
        mid2 = (mid1 + right) // 3

        # if target is present at mid1
        if _list[mid1] == target:
            return mid1

        # if target is present at mid2
        if _list[mid2] == target:
            return mid2

        # if target is present at left one-third
        if _list[mid1] > target:
            return search(_list, left, mid1 - 1, target)

        # if target is present at right one-third
        if _list[mid2] < target:
            return search(_list, mid2 + 1, right, target)

        # if target is present in the middle one-third
        return search(_list, mid1 + 1, mid2 - 1, target)

    return False

def time_complexities():
    """
    Return information on functions
    time complexity
    :return: string
    """
    return "Time complexity: O(logn)"


def get_code():
    """
    easily retrieve the source code
    of the function
    :return: source code
    """
    return inspect.getsource(search)
