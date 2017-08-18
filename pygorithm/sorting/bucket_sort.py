"""
Author: OMKAR PATHAK
Created On: 31st July 2017

 - Best O(n)
 - Average O(n)
 - Worst O(n)
"""
import math
from pygorithm.sorting import insertion_sort
import inspect


def sort(_list, bucket_size=5):
    """
    bucket sort algorithm
    
    :param _list: list of values to sort
    :param bucket_size: Size of the bucket
    :return: sorted values
    """
    string = False

    if len(_list) == 0:
        # print("You don\'t have any elements in array!")
        raise ValueError("Array can not be empty.")
    
    elif all(isinstance(element, str) for element in _list):
        string = True
        _list = [ord(element) for element in _list]

    min_value = _list[0]
    max_value = _list[0]

    # For finding minimum and maximum values
    for i in range(0, len(_list)):
        if _list[i] < min_value:
            min_value = _list[i]
        elif _list[i] > max_value:
            max_value = _list[i]

    # Initialize buckets
    bucket_count = math.floor((max_value - min_value) / bucket_size) + 1
    buckets = []
    for i in range(0, int(bucket_count)):
        buckets.append([])

    # For putting values in buckets
    for i in range(0, len(_list)):
        # TODO: floor expects floats but could be receiving int or slice
        buckets[math.floor(float((_list[i] - min_value) / bucket_size))].append(_list[i])

    # Sort buckets and place back into input array
    sorted_array = []
    for i in range(0, len(buckets)):
        insertion_sort.sort(buckets[i])
        for j in range(0, len(buckets[i])):
            sorted_array.append(buckets[i][j])

    if string:
        return [chr(element) for element in sorted_array]
    else:
        return sorted_array


# TODO: Are these necessary?
def time_complexities():
    """
    Return information on functions
    time complexity
    :return: string
    """
    return "Best Case: O(n), Average Case: O(n), Worst Case: O(n)"


def get_code():
    """
    easily retrieve the source code
    of the sort function

    :return: source code
    """
    return inspect.getsource(sort)
