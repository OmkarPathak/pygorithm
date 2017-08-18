"""
Author: DION MISIC
Created On: 11th August 2017
"""
import inspect


def search(array, n):
    """
    Recursively defined function for finding nth number in unsorted list

    :param array:
    :param n:
    :return:
    """
    return select(array, 0, len(array) - 1, n)


def select(array, left, right, n):
    """
    helper method for search function

    :param array:
    :param left:
    :param right:
    :param n:
    :return:
    """
    if left == right:
        return array[left]
    split = partition(array, left, right, n)
    length = split - left + 1
    if length == n:
        return array[split]
    elif n < length:
        return select(array, left, split - 1, n)
    else:
        return select(array, split + 1, right, n - length)


def partition(array, left, right, pivot):
    """
    helper method for select functions
    :param array:
    :param left:
    :param right:
    :param pivot:
    :return:
    """
    pivot_val = array[pivot]
    array[pivot], array[right] = array[right], array[pivot]
    store_index = left

    for i in range(left, right):
        if array[i] < pivot_val:
            array[store_index], array[i] = array[i], array[store_index]
            store_index += 1

    array[right], array[store_index] = array[store_index], array[right]
    return store_index


# TODO: Are these necessary?
def time_complexities():
    """
    Return information on functions
    time complexity
    :return: string
    """
    return "Best Case: O(n), Average Case: O(n), Worst Case: O(n^2)"


def get_code():
    """
    easily retrieve the source code
    of the function

    :return: source code
    """
    return inspect.getsource(search)
