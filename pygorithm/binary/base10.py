"""
Binary: Base10

Conversions from base10 to:
  - base2
  - base16

Author: Ian Doarn
"""
HEX_VALUES = {
    0: '0', 1: '1', 2: '2',
    3: '3', 4: '4', 5: '5',
    6: '6', 7: '7', 8: '8',
    9: '9', 10: 'A', 11: 'B',
    12: 'C', 13: 'D', 14: 'E',
    15: 'F'
}


def to_base2(n, visualize=False):
    """
    Divide each number by 2 using
    the % operator.

    Reverse the resulting list of numbers
    and return the result

    :param n: decimal number
    :param visualize: Show process
    :return: binary number
    """
    _list = []
    while n > 0.5:
        if visualize:
            print("{} / 2 = {} || {} % 2 = {}".format(str(n), str(n / 2), str(n), str(n % 2)))
        _list.append(n % 2)
        n = int(n / 2)

    # Reverse the list, turn each number to a string,
    # join the string, and convert it back to an integer
    return int(''.join([str(i) for i in _list[::-1]]))


def to_base16(n, visualize=False):
    """
    Convert decimal number to hexadecimal

    Divide the number by 16 and add the remainder
    to a list, round down the value after division
    and repeat till our value is 0

    Reverse the results list, get each values respective
    hex value using HEX_VALUES map

    :param n: decimal number
    :param visualize: Show process
    :return: hexadecimal number
    """
    _list = []
    while n != 0:
        if visualize:
            print("{} % 16 = {} -> hex = {}".format(
                str(n), str(n % 16), HEX_VALUES[n % 16]
            ))
        _list.append(HEX_VALUES[n % 16])
        n = int(n / 16)

    if visualize:
        print(_list)
        print("reversed = " + str(_list[::-1]))

    return ''.join(_list[::-1])
