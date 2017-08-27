"""
ASCII

Conversions from ASCII to:
  - base2
  - base16

Author: Ian Doarn
"""
from pygorithm.binary.binary_utils import pad
from pygorithm.binary.base10 import to_base2 as b10_to_b2
from pygorithm.binary.base2 import to_base16 as b2_to_b16, \
    to_ascii as b2_to_ascii


def to_base16(string, visualize=False):
    """
    Convert ascii to hexadecimal
    :param string: string to convert
    :param visualize: Show process
    :param as_string: return value as string not array
    :return: hex representation of given string
    """
    hex_array = []

    for b_value in to_base2(string):
        if visualize:
            print("{} -> {}".format(
                b2_to_ascii(b_value), b2_to_b16(b_value)
            ))
        hex_array.append(b2_to_b16(b_value))

    return hex_array


def to_base2(string, visualize=False, as_string=False):
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
                str(b10_to_b2(ord(x)))
            ))
        value = pad(str(b10_to_b2(ord(x))))
        _list.append(value)

    if as_string:
        return ' '.join(_list)
    return _list
