"""
Base2 to Base10

Convert binary numbers to decimal numbers

Author: Ian Doarn
"""


def convert_base2_to_base10(n, visualize=False):
    """
    Convert given number to a list
    for every number do the following formula

    x * 2 + number

    repeat for each result! Example:

    binary number = 100110

    0 x 2 + 1 = 1
    1 x 2 + 0 = 2
    2 x 2 + 0 = 4
    4 x 2 + 1 = 9
    9 x 2 + 1 = 19
    19 x 2 + 0 = 38

    :param n: binary number
    :param visualize: Show process
    :return: decimal number
    """
    if type(n) is str:
        raise ValueError('value must be int not type {}'.format(str(type(n))))

    x = 0
    _list = [int(i) for i in str(n)]

    for number in _list:
        if visualize:
            print("{} x 2 + {} = {}".format(str(x), str(number), str(x * 2 + number)))
        x = x * 2 + number

    return x
