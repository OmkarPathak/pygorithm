"""
Author: MrDupin
Created At: 25th August 2017
"""
import inspect

#Path(i, j) = min(Path(i-1, j), Path(i, j-1) + Matrix(i, j)


def calculate_path(i, j, matrix, s):
    if(s[i][j] > 0):
        #We have already calculated solution for i,j; return it.
        return s[i][j]

    m1 = calculate_path(i-1, j, matrix, s) + matrix[i][j] #Optimal solution for i-1, j (top)
    m2 = calculate_path(i, j-1, matrix, s) + matrix[i][j] #Optimal solution for i, j-1 (left)

    #Store and return the optimal (minimum) solution
    if(m1 < m2):
        s[i][j] = m1
        return m1
    else:
        s[i][j] = m2
        return m2


def find_path(matrix):
    l = len(matrix);
    #Initialize solution array.
    #A node of i, j in solution has an equivalent node of i, j in matrix
    s = [[0 for i in range(l)] for j in range(l)];

    #Initialize first node as its matrix equivalent
    s[0][0] = matrix[0][0]

    #Initialize first column as the matrix equivalent + the above solution
    for i in range(1, l):
        s[i][0] = matrix[i][0] + s[i-1][0]

    #Initialize first row as the matrix equivalent + the left solution
    for j in range(1, l):
        s[0][j] = matrix[0][j] + s[0][j-1]

    return calculate_path(l-1, l-1, matrix, s)


def get_code():
    """
    returns the code for the min cost path function
    """
    return inspect.getsource(calculate_path)
