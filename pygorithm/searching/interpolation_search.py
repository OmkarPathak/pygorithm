"""
Author: SHARAD BHAT
Created On: 22nd August 2017

 - Best O(1)
 - Average O(log(logn))
 - Worst O(n)
"""

import inspect

def search(_list, target):
    """
    This function performs an interpolation search
    on a sorted list and returns the index
    of item if successful else returns False

    :param _list: list to search
    :param target: item to search for
    :return: index of item if successful else returns False
    """

    if type(_list) is not list:
        raise TypeError("interpolation search only accepts lists, not {}".format(str(type(_list))))

    # First element
    low = 0
    # Last element
    high = len(_list) - 1

    # List is assumed to be sorted
    while low <= high and target >= _list[low] and target <= _list[high]:
        position = low + int(((float(high - low) / (_list[high] - _list[low])) * (target - _list[low])))

        if _list[position] == target:
            return position

        # If target is greater, search in right half
        if _list[position] < target:
            low = position + 1

        # If target is smaller, search in left half
        else:
            high = position - 1

    return False



def time_complexities():
    """
    Return information on functions
    time complexity
    :return: string
    """
    return "Best Case: O(1), Average Case: O(log(logn)), Worst Case: O(logn)"


def get_code():
    """
    easily retrieve the source code
    of the function
    :return: source code
    """
    return inspect.getsource(search)
