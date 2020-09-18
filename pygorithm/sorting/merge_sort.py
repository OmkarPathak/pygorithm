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
        return list(_list)
    else:
        middle = len(_list)//2
        a = sort(_list[:middle])
        b = sort(_list[middle:])
        return merge(a, b)

from itertools import zip_longest
def sorti(_list, verbose=True):
    """
    Function to sort an array
    using merge sort algorithm, iteratively

    :param _list: list of values to sort
    :return: sorted
    """
    # breakdown every element into its own list
    series = [[i] for i in _list]
    while len(series) > 1:
        if verbose: print(series)
        # iterator to handle two at a time in the zip_longest below
        isl = iter(series)
        series = [
            merge(a, b) if b else a
            for a, b in zip_longest(isl, isl)
        ]
    return series[0]

# TODO: Are these necessary?
def time_complexities():
    """
    Return information on functions
    time complexity
    :return: string
    """
    return "Best Case: O(nlogn), Average Case: O(nlogn), Worst Case: O(nlogn)"


def get_code(iter=False):
    """
    easily retrieve the source code
    of the sort function

    :return: source code
    """
    if iter: 
        return inspect.getsource(sorti) + "\n"
    return inspect.getsource(sort) + "\n" + inspect.getsource(merge)
