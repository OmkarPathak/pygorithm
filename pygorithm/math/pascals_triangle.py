'''
Author: OMKAR PATHAK
Created at: 26th August 2017
'''

def pascals_triangle(n):
    '''
    :param n: total number of lines in pascal triangle

    Pascal’s triangle is a triangular array of the binomial coefficients.
    Following are the first 6 rows of Pascal’s Triangle (when n = 6)
    1
    1 1
    1 2 1
    1 3 3 1
    1 4 6 4 1
    1 5 10 10 5 1
    '''

    for line in range(1, n + 1):
        C = 1
        for i in range(1, line + 1):
            print(C, end = ' ')
            C = C * (line - i) // i
        print()
