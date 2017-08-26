"""
Author: OMKAR PATHAK
Created at: 16th August 2017
"""
from functools import reduce
import inspect


def lcm(_list):
    """LCM
    function to find LCM for given list of elements
    :param _list: _list of which LCM is to be found out
    """

    def __lcm(a, b):
        """
        helper function for finding LCM

        :param a:
        :param b:
        :return: lcm
        """
        if a > b:
            greater = a
        else:
            greater = b

        while True:
            if greater % a == 0 and greater % b == 0:
                lcm_ = greater
                break
            greater += 1
        return lcm_

    return reduce(lambda x, y: __lcm(x, y), _list)


def get_code():
    """
    returns the code for the lcm function
    """
    return inspect.getsource(lcm)
