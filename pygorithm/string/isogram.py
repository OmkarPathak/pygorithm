# Author: OMKAR PATHAK
# Created On: 17th August 2017

def is_isogram(word):
    '''
        An isogram (also known as a "nonpattern word") is a logological term for a word
        or phrase without a repeating letter
    '''
    # Convert the word or sentence in lower case letters.
    clean_word = word.lower()
    # Make ann empty list to append unique letters
    letter_list = []
    for letter in clean_word:
        # If letter is an alphabet then only check
        if letter.isalpha():
            if letter in letter_list:
                return False
            letter_list.append(letter)

    return True

def get_code():
    """ returns the code for the current class """
    import inspect
    return inspect.getsource(is_isogram)
