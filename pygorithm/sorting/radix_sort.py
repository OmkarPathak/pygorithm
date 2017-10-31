"""
Author: Ian Doarn
Date: 31st Oct 2017

Reference:
 https://stackoverflow.com/questions/35419229/python-radix-sort
"""


def sort(_list, base=10):
    """
    Radix Sort
    
    :param _list: array to sort
    :param base: base radix number
    :return: sorted list
    """
    # TODO: comment this

    result_list = []
    power = 0
    while _list:
        bs = [[] for _ in range(base)]
        for x in _list:
            bs[x // base ** power % base].append(x)
        _list = []
        for b in bs:
            for x in b:
                if x < base ** (power + 1):
                    result_list.append(x)
                else:
                    _list.append(x)
        power += 1
    return result_list


if __name__ == '__main__':
    print(sort([170, 45, 75, 90, 802, 24, 2, 66]))
