"""
Helper methods for binary package
Author: Ian Doarn
"""


def pad(value: str, return_type=str) -> """Pad binary value with zeros""":
    if len(value) % 4 != 0:
        pad_amount = 4 - (len(value) % 4)
        return return_type(('0' * pad_amount) + value)
    else:
        return return_type(value)


def to_string(binary_array: list, delimiter=' ') -> """Convert binary array to string""":
    return delimiter.join(binary_array)