"""
Author: OMKAR PATHAK
Created On: 31st July 2017

 - Best = Average = Worst = O(n log(n))
 
"""
import inspect


def merge(a, b):
    """
    Function to merge 
    two arrays / separated lists
    
    :param a: Array 1
    :param b: Array 2
    :return: merged arrays
    """
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c


def sort(_list):
    """
    Function to sort an array 
    using merge sort algorithm 
    
    :param _list: list of values to sort
    :return: sorted
    """
    if len(_list) == 0 or len(_list) == 1:
        return _list
    else:
        middle = len(_list)//2
        a = sort(_list[:middle])
        b = sort(_list[middle:])
        return merge(a, b)


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
    return inspect.getsource(sort) + "\n" + inspect.getsource(merge)
