"""
Helper methods for binary package
Author: Ian Doarn
"""


def pad(value, return_type=str):
    '''
        Pad binary value with zeros
        :param value: string
        :param return_type: string
    '''
    if type(value) is not str:
        raise TypeError("pad only accepts str, not {}".format(str(type(value))))
    if len(value) % 4 != 0:
        pad_amount = 4 - (len(value) % 4)
        return return_type(('0' * pad_amount) + value)
    else:
        return return_type(value)


def to_string(binary_array, delimiter=' '):
    """
        Convert binary array to string
    """
    if type(binary_array) is not list:
        raise TypeError("to_string only accepts lists, not {}".format(str(type(value))))
    return delimiter.join(binary_array)
