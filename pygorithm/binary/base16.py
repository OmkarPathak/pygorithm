"""
Binary: Base16

Conversions from base16 to:
  - base2
  - base10
  - ASCII

Author: Ian Doarn
"""
from pygorithm.binary.base2 import to_ascii as b2_to_ascii
from pygorithm.binary.binary_utils import pad
from math import pow

HEX_BINARY_VALUES = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}

HEX_LETTER_VALUES = {
    '0': 0, '1': 1, '2': 2,
    '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8,
    '9': 9, 'A': 10, 'B': 11,
    'C': 12, 'D': 13, 'E': 14,
    'F': 15
}


def to_base2(h, visualize=False):
    """
    Convert hexadecimal to binary number

    :param h: hexadecimal number
    :param visualize: Show process
    :return: binary number
    """

    hex_char_list = list(h)
    _list = []

    for value in hex_char_list:
        if visualize:
            print("{} -> {}".format(
                value, HEX_BINARY_VALUES[value]
            ))
        _list.append(pad(HEX_BINARY_VALUES[value]))

    return int(''.join(_list))


def to_base10(h, visualize=False):
    """
    Convert hexadecimal number to decimal number

    Send hex to a list and reverse. Evaluate each hex value
    via HEX_LETTER_VALUES map. Enumerate the list,

    using the equation: value * 16 ^ index

    value is the hex char value: F -> 15
    index is its position in the list: ['1', 'A', 'F'] F's index = 2

    Continue this for each hex letter until we reach the end of the list,
    summing all evaluated values.

    :param h: hexadecimal number
    :param visualize: Show process
    :return: decimal number
    """

    # Check to see if '0x' is at the beginning and remove it
    if h[0:2] == '0x':
        hex_char_list = list(h[2:])[::-1]
    else:
        hex_char_list = list(h)[::-1]

    value = 0

    for i, v in enumerate(hex_char_list):
        if visualize:
            print("{} -> {} || {} * (16 ^ {}) = {}".format(
                v, str(HEX_LETTER_VALUES[v]),
                str(HEX_LETTER_VALUES[v]),
                str(i),
                str(HEX_LETTER_VALUES[v] * (pow(16, i)))
            ))

        value += HEX_LETTER_VALUES[v] * (pow(16, i))

    return int(value)


def to_ascii(h_array, visualize=False):
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
                to_base2(h_value),
                b2_to_ascii(str(to_base2(h_value)))
            ))

        string += b2_to_ascii(str(to_base2(h_value)))

    return string
