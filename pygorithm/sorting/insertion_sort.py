"""
Author: OMKAR PATHAK
Created On: 31st July 2017

 - Best O(n)
 - Average O(n^2)
 - Worst O(n^2)
"""
import inspect


def sort(_list):
    """
    Insertion sort algorithm

    :param _list: list or values to sort
    :return: sort values
    """
    for i in range(1, len(_list)):
        current_number = _list[i]
        for j in range(i - 1, -1, -1):
            if _list[j] > current_number:
                _list[j], _list[j + 1] = _list[j + 1], _list[j]
            else:
                _list[j + 1] = current_number
                break
    return _list


# TODO: Are these necessary?
def time_complexities():
    """
    Return information on functions
    time complexity
    :return: string
    """
    return "Best Case: O(n), Average Case: O(n ^ 2), Worst Case: O(n ^ 2)"


def get_code():
    """
    easily retrieve the source code
    of the sort function

    :return: source code
    """
    return inspect.getsource(sort)
