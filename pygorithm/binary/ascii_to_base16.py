"""
ASCII to Hexadecimal

Author: Ian Doarn
"""
from pygorithm.binary.ascii_to_base2 import convert_ascii_to_base2
from pygorithm.binary.base2_to_base16 import convert_base2_to_base16
from pygorithm.binary.base2_to_ascii import convert_base2_to_ascii


def convert_ascii_to_base16(string, visualize=False):
    """
    Convert ascii to hexadecimal

    :param string: string to convert
    :param visualize: Show process
    :param as_string: return value as string not array
    :return: hex representation of given string
    """
    hex_array = []

    for b_value in convert_ascii_to_base2(string):
        if visualize:
            print("{} -> {}".format(
                convert_base2_to_ascii(b_value), convert_base2_to_base16(b_value)
            ))
        hex_array.append(convert_base2_to_base16(b_value))

    return hex_array
