"""
Author: OMKAR PATHAK
Created On: 17th August 2017
"""
from string import ascii_lowercase
import inspect


def is_pangram(sentence):
    """
    A sentence containing every letter of the alphabet.

    :param sentence: Sentence to check
    :return: bool
    """

    f_string = ''.join(c for c in sentence if c.isalpha()).lower()
    return set(ascii_lowercase) == set(f_string)


def get_code():
    """
    returns the code for the is_pangram function
    :return: source code
    """
    return inspect.getsource(is_pangram)
