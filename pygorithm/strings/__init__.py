"""
Collection of string methods and functions
"""
from . import anagram
from . import pangram
from . import isogram
from . import palindrome
from . import manacher_algorithm
from . import kmp_search
from . import edit_distance

__all__ = [
    'anagram',
    'pangram',
    'isogram',
    'manacher_algorithm',
    'palindrome',
    'kmp_search',
    'edit_distance'
]
