"""
Hexadecimal to Decimal

Author: Ian Doarn
"""
from math import pow

hex_letter_values = {
    '0': 0, '1': 1, '2': 2,
    '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8,
    '9': 9, 'A': 10, 'B': 11,
    'C': 12, 'D': 13, 'E': 14,
    'F': 15
}


def convert_base16_to_base10(h, visualize=False):
    """
    Convert hexadecimal number to decimal number
    
    Send hex to a list and reverse. Evaluate each hex value
    via hex_letter_values map. Enumerate the list,
    
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
                v, str(hex_letter_values[v]),
                str(hex_letter_values[v]),
                str(i),
                str(hex_letter_values[v] * (pow(16, i)))
            ))

        value += hex_letter_values[v] * (pow(16, i))

    return int(value)
