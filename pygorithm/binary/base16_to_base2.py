"""
Hexadecimal to Binary

Author: Ian Doarn
"""

hex_binary_values = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}


def convert_base16_to_base2(h, visualize=False):
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
                value, hex_binary_values[value]
            ))
        _list.append(hex_binary_values[value])

    return int(''.join(_list))
