"""
Hexadecimal to ASCII

Author: Ian Doarn
"""
from pygorithm.binary.base16_to_base2 import convert_base16_to_base2
from pygorithm.binary.base2_to_ascii import convert_base2_to_ascii


def convert_base16_to_ascii(h_array, visualize=False):
    """
    Convert base16 array to ASCII string

    Input must be a list of strings:
    Example::

    array = [
        '74', '68', '65',
        '20', '71', '75',
        '69', '63', '6B',
        '20', '62', '72',
        '6F', '77', '6E',
        '20', '66', '6F',
        '78', '20', '6A',
        '75', '6D', '70',
        '73', '20', '6F',
        '76', '65', '72',
        '20', '74', '68',
        '65', '20', '6C',
        '61', '7A', '79',
        '20', '64', '6F',
        '67'
    ]

    result -> the quick brown fox jumps over the lazy dog

    :param h_array: hex value array
    :param visualize: Show process
    :return: ASCII string
    """
    string = ''

    for h_value in h_array:
        if visualize:
            print("{} -> {} -> {}".format(
                h_value,
                convert_base16_to_base2(h_value),
                convert_base2_to_ascii(str(convert_base16_to_base2(h_value)))
            ))

        string += convert_base2_to_ascii(str(convert_base16_to_base2(h_value)))

    return string
