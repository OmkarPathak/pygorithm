import unittest

from pygorithm.strings import (
    anagram,
    isogram,
    pangram,
    manacher_algorithm,
    palindrome)

class TestAnagram(unittest.TestCase):
    def test_anagram(self):
        self.assertEqual(anagram.is_anagram('ant', ['tan', 'stand', 'at']), ['tan'])

class TestPangram(unittest.TestCase):
    def test_pangram(self):
        self.assertTrue(pangram.is_pangram('the quick brown fox jumps over the lazy dog'))
        self.assertFalse(pangram.is_pangram('omkar'))

class TestIsogram(unittest.TestCase):
    def test_isogram(self):
        self.assertTrue(isogram.is_isogram('isogram'))
        self.assertFalse(isogram.is_isogram('eleven'))

class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(palindrome.is_palindrome('madam'))
        self.assertFalse(palindrome.is_palindrome('eleven'))

class TestManacherAlgorithm(unittest.TestCase):
    def test_manacher_algorithm(self):
        self.assertEqual(manacher_algorithm.manacher('babcbabcbaccba'), 'abcbabcba')

if __name__ == '__main__':
    unittest.main()
