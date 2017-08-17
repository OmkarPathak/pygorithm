"""
Author: OMKAR PATHAK
Created On: 31st July 2017

 - Best O(n^2)
 - Average O(n^2) 
 - Worst O(n^2)
"""
import inspect


def sort(_list):
    """
    selection sort algorithm
    
    :param _list: list of integers to sort
    :return: sorted list
    """

    # For iterating n - 1 times
    for i in range(len(_list) - 1):
        minimum = i

        # Compare i and i + 1 element
        for j in range(i + 1, len(_list)):
            if _list[j] < _list[minimum]:
                minimum = j
        if minimum != i:
            _list[i], _list[minimum] = _list[minimum], _list[i]
    return _list


# TODO: Are these necessary?
def time_complexities():
    """
    Return information on functions
    time complexity
    :return: string
    """
    return "Best Case: O(n ^ 2), Average Case: O(n ^ 2), Worst Case: O(n ^ 2)"


def get_code():
    """
    easily retrieve the source code
    of the sort function

    :return: source code
    """
    return inspect.getsource(sort)
