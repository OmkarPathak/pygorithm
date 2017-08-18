"""
Author: OMKAR PATHAK
Created On: 17th August 2017
"""
from collections import Counter
import inspect


def is_anagram(word, _list):
    """ANAGRAM
    An anagram is direct word switch or word play,
    the result of rearranging the letters of a word
    or phrase to produce a new word or phrase, using
    all the original letters exactly once we are taking
    a word and a list. We return the anagrams of that
    word from the given list and return the list of
    anagrams else return empty list.

    :param word: word
    :param _list: list of words
    :return: anagrams
    """
    word = word.lower()
    anagrams = []
    for words in _list:
        if word != words.lower():
            if Counter(word) == Counter(words.lower()):
                anagrams.append(words)
    return anagrams


def get_code():
    """
    returns the code for the is_anagram function
    :return: source code
    """
    return inspect.getsource(is_anagram)
