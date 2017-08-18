"""
Author: OMKAR PATHAK
Created On: 1st August 2017

 - Best O(1)
 - Average O(n)
 - Worst O(n)
"""
import inspect


def search(_list, target, initial_position=0):
    """sequential search algorithm
    
    This function returns the position 
    of the target if found else returns -1
    
    :param _list: 
    :param target:
    :param initial_position: default @ 0
    :return: 
    """
    position = initial_position
    while position < len(_list):
        if target == _list[position]:
            return position
        position += 1
    return -1


# TODO: Are these necessary?
def time_complexities():
    """
    Return information on functions
    time complexity
    :return: string
    """
    return "Best Case: O(1), Average Case: O(n), Worst Case: O(n)"


def get_code():
    """
    easily retrieve the source code
    of the function

    :return: source code
    """
    return inspect.getsource(search)
