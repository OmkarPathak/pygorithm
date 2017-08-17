"""
Author: OMKAR PATHAK
Created On: 31st July 2017

 - Best = Average = O(n log(n))
 - Worst = O(n ^ 2)
"""
import inspect



def sort(_list):
    """
    quick_sort algorithm
    :param _list: list of integers to sort
    :return: sorted list
    """
    if len(_list) <= 1:
        return _list
    pivot = _list[len(_list) // 2]
    left = [x for x in _list if x < pivot]
    middle = [x for x in _list if x == pivot]
    right = [x for x in _list if x > pivot]
    return sort(left) + middle + sort(right)


# TODO: Are these necessary?
def time_complexities():
    """
    Return information on functions
    time complexity
    :return: string
    """
    return '''Best Case: O(nlogn), Average Case: O(nlogn), Worst Case: O(n ^ 2)'''


def get_code():
    """
    easily retrieve the source code
    of the sort function

    :return: source code
    """
    return inspect.getsource(sort)
