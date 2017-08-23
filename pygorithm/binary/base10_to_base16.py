"""
Convert decimal numbers to hexadecimal numbers

Author: Ian Doarn
"""


hex_values = {
    0: '0', 1: '1', 2: '2',
    3: '3', 4: '4', 5: '5',
    6: '6', 7: '7', 8: '8',
    9: '9', 10: 'A', 11: 'B',
    12: 'C', 13: 'D', 14: 'E',
    15: 'F'
}


def convert_base10_to_base16(n, visualize=False):
    """
    Convert decimal number to hexadecimal

    Divide the number by 16 and add the remainder
    to a list, round down the value after division
    and repeat till our value is 0

    Reverse the results list, get each values respective
    hex value using hex_values map

    :param n: decimal number
    :param visualize: Show process
    :return: hexadecimal number
    """
    _list = []
    while n != 0:
        if visualize:
            print("{} % 16 = {} -> hex = {}".format(
                str(n), str(n % 16), hex_values[n % 16]
            ))
            _list.append(hex_values[n % 16])
        n = int(n / 16)

    if visualize:
        print(_list)
        print("reversed = " + str(_list[::-1]))

    return ''.join(_list[::-1])
