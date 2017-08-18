# Author: OMKAR PATHAK
# Created On: 17th August 2017

from collections import Counter

def is_anagram(word, List):
    '''
        ANAGRAM: An anagram is direct word switch or word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once
        We are taking a word and a list. We return the anagrams of that word from the given list and return the list of anagrams else return empty list
    '''
    word = word.lower()
    anagrams = []
    for words in List:
    	if word != words.lower():
    		if Counter(word) == Counter(words.lower()):
    			anagrams.append(words)
    return anagrams

def get_code():
    """ returns the code for the current class """
    import inspect
    return inspect.getsource(is_anagram)
