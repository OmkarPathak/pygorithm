"""
Author: Omkar Pathak
Created At: 25th August 2017
"""
import inspect

def longest_increasing_subsequence(_list):
    """
    The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a
    given sequence such that all elements of the subsequence are sorted in increasing order. For example,
    the length of LIS for [10, 22, 9, 33, 21, 50, 41, 60, 80] is 6 and LIS is [10, 22, 33, 50, 60, 80].

    :param _list: an array of elements
    :return: returns a tuple of maximum length of lis and an array of the elements of lis
    """
    # Initialize list with some value
    lis = [1] * len(_list)
    # list for storing the elements in an lis
    elements = [0] * len(_list)

    # Compute optimized LIS values in bottom up manner
    for i in range(1, len(_list)):
        for j in range(0, i):
            if _list[i] > _list[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j]+1
                elements[i] = j

    # find the maximum of the whole list and get its index in idx
    maximum = max(lis)
    idx = lis.index(maximum)

    # for printing the elements later
    seq = [_list[idx]]
    while idx != elements[idx]:
        idx = elements[idx]
        seq.append(_list[idx])

    return (maximum, seq[::-1])


def get_code():
    """
    returns the code for the longest_increasing_subsequence function
    """
    return inspect.getsource(longest_increasing_subsequence)
