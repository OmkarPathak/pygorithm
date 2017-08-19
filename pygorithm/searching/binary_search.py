"""
Author: OMKAR PATHAK
Created On: 1st August 2017

 - Best O(1)
 - Average O(logn)
 - Worst O(logn)
"""
from __future__ import division
import inspect


def search(_list, target):
    """
    This function performs a binary search
    on a sorted list and returns the index
    of item if successful else returns False

    :param _list: list to search
    :param target: item to search for
    :return: index of item if successful else returns False
    """

    if type(_list) is not list:
        raise TypeError("binary search only excepts lists, not {}".format(str(type(_list))))

    # First position of the list
    left = 0
    # Last position of the list
    right = len(_list) - 1

    try:
        # you can also write while True condition
        while left <= right:
            mid = (left + right) // 2
            if target == _list[mid]:
                return mid
            elif target < _list[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False
    except TypeError:
        return False


# TODO: Are these necessary?
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
