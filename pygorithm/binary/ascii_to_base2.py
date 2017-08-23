"""
ASCII to Binary

Author: Ian Doarn
"""
from pygorithm.binary.base10_to_base2 import convert_base10_to_base2


def convert_ascii_to_base2(string, visualize=False, as_string=False):
    """
    Convert ascii string to binary

    :param string: Ascii string
    :param visualize: Show process
    :param as_string: join strings with a space as one large value
    :return: array of binary numbers, or entire string
    """
    _list = []
    for x in string:
        if visualize:
            print("{} -> {} -> {}".format(
                x, str(ord(x)),
                str(convert_base10_to_base2(ord(x)))
            ))
        _list.append(str(convert_base10_to_base2(ord(x))))

    if as_string:
        return ' '.join(_list)
    return _list
