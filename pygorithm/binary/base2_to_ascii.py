"""
Base2 to ASCII

Author: Ian Doarn
"""
from pygorithm.binary.base2_to_base10 import convert_base2_to_base10


def convert_base2_to_ascii(b, visualize=False):
    """
    Convert binary to ASCII

    :param b: binary number or array
    :param visualize: Show process
    :return: ASCII String
    """
    binary = b
    # Make sure give binary is a str array
    if type(b) is str:
        binary = b.split(' ')
    elif type(b) is list:
        binary = b

    string = ''

    for b_value in binary:
        if visualize:
            print("{} -> {} -> {}".format(
                b_value, convert_base2_to_base10(int(b_value)),
                chr(convert_base2_to_base10(int(b_value)))
            ))
        value = convert_base2_to_base10(int(b_value))
        string += chr(value)
    return string
