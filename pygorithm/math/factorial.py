"""
Author: OMKAR PATHAK
Created On: 22 August 2017
"""

def factorial(number):
    ''' This function calculates the factorial of a number '''
    if not isinstance(number, int):
        raise Exception('Enter an integer number to find the factorial')
    if number == 1 or number == 0:
        return 1
    else:
        return number * factorial(number - 1)

def get_code():
    """
    returns the code for the factorial function
    """
    return inspect.getsource(factorial)
