#Author: OMKAR PATHAK
# Created On: 17th August 2017

def is_palindrome(string):
    '''This function checks the string for palindrome'''
    revString = string[::-1]
    if string == revString:
        return True
    else:
        return False

def get_code():
    """ returns the code for the current class """
    import inspect
    return inspect.getsource(palindrome)
