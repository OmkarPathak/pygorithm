# Author: OMKAR PATHAK
# Created On: 17th August 2017

def is_pangram(sentence):
    '''
        PANGRAM: A sentence containing every letter of the alphabet.
    '''
    alphabet = list(map(chr, range(97, 123)))
    formattedString = ''.join(c for c in sentence if c.isalpha()).lower()
    return set(alphabet) == set(formattedString)

def get_code():
    """ returns the code for the current class """
    import inspect
    return inspect.getsource(is_pangram)
