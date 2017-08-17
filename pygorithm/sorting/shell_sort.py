"""
Author: OMKAR PATHAK
Created On: 31st July 2017

 - Best Case O(n log n)
 - Average Case O(depends on gap sequence)
 - Worst Case O(n^2)
"""
import inspect


def sort(_list):
    """
    Shell sort algorithm

    :param _list: list of integers to sort
    :return: sorted list
    """
    gap = len(_list) // 2
    while gap > 0:
        for i in range(gap, len(_list)):
            current_item = _list[i]
            j = i
            while j >= gap and _list[j - gap] > current_item:
                _list[j] = _list[j - gap]
                j -= gap
            _list[j] = current_item
        gap //= 2

    return _list


# TODO: Are these necessary?
def time_complexities():
    """
    Return information on functions
    time complexity
    :return: string
    """
    return "Best Case: O(nlogn), Average Case: O(depends on gap sequence), Worst Case: O(n ^ 2)"


def get_code():
    """
    easily retrieve the source code 
    of the sort function
    
    :return: source code
    """
    return inspect.getsource(sort)
