"""
Author: OMKAR PATHAK
Created On: 26th August 2017

 - Best O(1)
 - Average O(logn)
 - Worst O(logn)

 More info: https://en.wikipedia.org/wiki/Exponential_search
"""

from __future__ import division
import inspect

def binary_search(_list, left, right, target):
    if right >= left:
        mid = (left + right) // 2

        # if element is present at the mid itself
        if _list[mid] == target:
            return mid

        # If the element is smaller than mid, then it
        # can only be present in the left subarray
        if _list[mid] > target:
            return binary_search(_list, left, mid - 1, target)

        # Else the element can only be present in the right
        return binary_search(_list, mid + 1, right, target)

    return False

def search(_list, target):
    """
    This function performs a exponential search
    on a sorted list and returns the index
    of item if successful else returns False

    :param _list: list to search
    :param target: item to search for
    :return: index of item if successful else returns False
    """

    if type(_list) is not list:
        raise TypeError("Exponential search only excepts lists, not {}".format(str(type(_list))))

    # is target is at the first position itself
    if _list[0] == target:
        return 0

    # Find range for binary seaarch by repeated doubling
    i = 1
    while i < len(_list) and _list[i] <= target:
        i = i * 2

    return binary_search(_list, i//2, min(i, len(_list)), target)


def time_complexities():
    """
    Return information on functions
    time complexity
    :return: string
    """
    return "Best Case: O(1), Average Case: O(logn), Worst Case: O(logn)"


def get_code():
    """
    easily retrieve the source code
    of the function
    :return: source code
    """
    return inspect.getsource(search)
