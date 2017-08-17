"""
Author: OMKAR PATHAK
Created On: 31st July 2017

 - Best O(nlog(n))
 - Average O(nlog(n))
 - Worst O(nlog(n))

"""
import inspect


def sort(_list):
    """
    heap sort algorithm

    :param _list: list of values to sort
    :return: sorted values
    """
    # TODO: Add description of how this works!
    
    # create the heap
    heapify(_list)              
    end = len(_list) - 1
    while end > 0:
        _list[end], _list[0] = _list[0], _list[end]
        shift_down(_list, 0, end - 1)
        end -= 1
    return _list


def heapify(_list):
    """
    function helps to maintain the heap property
    
    :param _list: list of values to sort
    :return: sorted values
    """

    start = len(_list) // 2
    while start >= 0:
        shift_down(_list, start, len(_list) - 1)
        start -= 1


def shift_down(_list, start, end):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        # right child exists and is greater than left child
        if child + 1 <= end and _list[child] < _list[child + 1]:
            child += 1
        # if child is greater than root(parent), then swap their positions
        if child <= end and _list[root] < _list[child]:
            _list[root], _list[child] = _list[child], _list[root]
            root = child
        else:
            return


# TODO: Are these necessary?
def time_complexities():
    """
    Return information on functions
    time complexity
    :return: string
    """
    return "Best Case: O(nlogn), Average Case: O(nlogn), Worst Case: O(nlogn)"


def get_code():
    """
    easily retrieve the source code 
    of the sort function

    :return: source code
    """
    return inspect.getsource(sort)
