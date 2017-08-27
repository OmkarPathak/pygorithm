'''
Author: OMKAR PATHAK
Created at: 27th August 2017
'''


def manacher(string):
    """
    Computes length of the longest palindromic substring centered on each char
    in the given string. The idea behind this algorithm is to reuse previously
    computed values whenever possible (palindromes are symmetric).

    Example (interleaved string):
    i    0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22
    s    #  a  #  b  #  c  #  q  #  q  #  q  #  q  #  q  #  q  #  x  #  y  #
    P    0  1  0  1  0  1  0  1  2  3  4  5  6  5  4  ?
                                    ^        ^        ^        ^
                                  mirror   center   current  right

    We're at index 15 wondering shall we compute (costly) or reuse. The mirror
    value for 15 is 9 (center is in 12). P[mirror] = 3 which means a palindrome
    of length 3 is centered at this index. A palindrome of same length would be
    placed in index 15, if 15 + 3 <= 18 (right border of large parlindrome
    centered in 12). This condition is satisfied, so we can reuse value from
    index 9 and avoid costly computation.
    """
    if type(string) is not str:
        raise TypeError("Manacher Algorithm only excepts strings, not {}".format(str(type(string))))

    # Get the interleaved version of a given string. 'aaa' --> '^#a#a#a#$'.
    # Thanks to this we don't have to deal with even/odd palindrome
    # length problem.
    string_with_bounds = '#'.join('^{}$'.format(string))
    length = len(string_with_bounds)
    P = [0] * length
    center = right = 0

    for i in range(1, length - 1):
        P[i] = (right > i) and min(right - i, P[2 * center - i])

        # Attempt to expand palindrome centered at i
        while string_with_bounds[i + 1 + P[i]] == string_with_bounds[i - 1 - P[i]]:
            P[i] += 1

        # If palindrome centered at i expand past R,
        # adjust center based on expanded palindrome.
        if i + P[i] > right:
            center, right = i, i + P[i]

    # Find the maximum element in P and return the string
    maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
    return string[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]

def get_code():
    """
    returns the code for the manacher's algorithm
    :return: source code
    """
    return inspect.getsource(manacher)
