"""
Author: OMKAR PATHAK
Created On: 17th August 2017
"""
import inspect


def is_palindrome(string):
    """
    Checks the string for palindrome

    :param string: string to check
    :return: true if string is a palindrome false if not
    """
    if string == string[::-1]:
        return True
    return False


def get_code():
    """
    returns the code for the is_palindrome function
    :return: source code
    """
    return inspect.getsource(is_palindrome)
