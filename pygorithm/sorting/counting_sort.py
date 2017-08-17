"""
Author: OMKAR PATHAK
Created On: 31st July 2017

 - Best = Average = Worst =  O(n + k)
"""
import inspect


# counting sort algorithm
def sort(_list):
    """
    counting sort algorithm
    
    :param _list: list of values to sort
    :return: sorted values
    """
    try:
        max_value = 0
        for i in range(len(_list)):
            if _list[i] > max_value:
                max_value = _list[i]

        buckets = [0] * (max_value + 1)

        for i in _list:
            buckets[i] += 1
        i = 0

        for j in range(max_value + 1):
            for a in range(buckets[j]):
                _list[i] = j
                i += 1

        return _list

    except TypeError as error:
        print('Counting Sort can only be applied to integers. {}'.format(error))


# TODO: Are these necessary?
def time_complexities():
    """
    Return information on functions
    time complexity
    :return: string
    """
    return "Best Case: O(n + k), Average Case: O(n + k), Worst Case: O(n + k)"


def get_code():
    """
    easily retrieve the source code
    of the sort function

    :return: source code
    """
    return inspect.getsource(sort)
