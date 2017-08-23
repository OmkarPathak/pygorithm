"""
Base10 to Base2

Convert decimal numbers to binary numbers

Author: Ian Doarn
"""


def convert_base10_to_base2(n, visualize=False):
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
