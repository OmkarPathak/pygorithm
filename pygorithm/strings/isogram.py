"""
Author: OMKAR PATHAK
Created On: 17th August 2017
"""
import inspect


def is_isogram(word):
    """
    An isogram (also known as a "nonpattern word")
    is a logological term for a word or phrase
    without a repeating letter

    :param word: word to check
    :return: bool
    """

    # Make an empty list to append unique letters
    letter_list = []
    for letter in word.lower():
        # If letter is an alphabet then only check
        if letter.isalpha():
            if letter in letter_list:
                return False
            letter_list.append(letter)
    return True


def get_code():
    """
    returns the code for the is_isogram function
    :return: source code
    """
    return inspect.getsource(is_isogram)
