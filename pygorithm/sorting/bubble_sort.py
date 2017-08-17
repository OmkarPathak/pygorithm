"""
Author: OMKAR PATHAK
Contributors: Mohamed Kiouaz
Created On: 31st July 2017

Best O(n); Average O(n*(n-1)/4); Worst O(n^2)
"""
import inspect


def sort(_list):
    """
    Bubble Sorting algorithm

    :param _list: list of values to sort
    :return: sorted values
    """
    for i in range(len(_list)):
        for j in range(len(_list) - 1, i, -1):
            if _list[j] < _list[j - 1]:
                _list[j], _list[j - 1] = _list[j - 1], _list[j]
    return _list


def improved_sort(_list):
    """
    Improved Bubble Sorting algorithm

    :param _list: list of values to sort
    :return: sorted values
    """
    for i in range(len(_list)):
        stop = True
        for j in range(len(_list) - 1, i, -1):
            if _list[j] < _list[j - 1]:
                stop = False
                _list[j], _list[j - 1] = _list[j - 1], _list[j]
        if stop:
            return _list
    return _list


# TODO: Are these necessary?
def time_complexities():
    """
    Return information on functions
    time complexity
    :return: string
    """
    return "Best Case: O(n), " \
           "Average Case: O(n ^ 2), " \
           "Worst Case: O(n ^ 2).\n\n" \
           "For Improved Bubble Sort:\nBest Case: O(n); Average Case: O(n * (n - 1) / 4); Worst Case: O(n ^ 2)"


def get_code():
    """
    easily retrieve the source code
    of the sort function

    :return: source code
    """
    return inspect.getsource(sort)
