'''
    Author: OMKAR PATHAK
    Created at: 01st September 2017

    Implementing various Matrix operations such as matrix addition, subtraction, multiplication.
'''

class Matrix(object):
    '''
        Matrix class for performing various transformations

        Matrix operations can be performed on two matrices with any number of dimensions
    '''

    def __init__(self, matrix_one = None, matrix_two=None):
        '''
            :param matrix_one: matrix with nxn dimensions
            :param matrix_two: matrix with nxn dimensions

            .. code-block:: python:

                matrix_one = [[1, 2], [1, 3], [1, 4]] (a 3x2 matrix)
        '''
        self.matrix_one = matrix_one
        self.matrix_two = matrix_two


    def add(self):
        '''
            function for adding the two matrices

            .. note::

                Matrix addition requires both the matrices to be of same size.
                That is both the matrices should be of nxn dimensional.
        '''

        # check if both the matrices are of same shape
        if not (len(self.matrix_one) == len(self.matrix_two)) or not (len(self.matrix_one[0]) == len(self.matrix_two[0])):
            raise Exception('Both Matrices should be of same dimensions')

        added_matrix = [[0 for i in range(len(self.matrix_one))] for j in range(len(self.matrix_two))]

        # iterate through rows
        for row in range(len(self.matrix_one)):
            # iterate through columns
            for column in range(len(self.matrix_one[0])):
                added_matrix[row][column] = self.matrix_one[row][column] + self.matrix_two[row][column]

        return added_matrix

    def subtract(self):
        '''
            function for subtracting the two matrices

            .. note::

                Matrix subtraction requires both the matrices to be of same size.
                That is both the matrices should be of nxn dimensional.
        '''

        # check if both the matrices are of same shape
        if not (len(self.matrix_one) == len(self.matrix_two)) or not (len(self.matrix_one[0]) == len(self.matrix_two[0])):
            raise Exception('Both Matrices should be of same dimensions')

        subtracted_matrix = [[0 for i in range(len(self.matrix_one))] for j in range(len(self.matrix_two))]

        # iterate through rows
        for row in range(len(self.matrix_one)):
            # iterate through columns
            for column in range(len(self.matrix_one[0])):
                subtracted_matrix[row][column] = self.matrix_one[row][column] - self.matrix_two[row][column]

        return subtracted_matrix


    def multiply(self):
        '''
            function for multiplying the two matrices

            .. note::

                Matrix multiplication can be carried out even on matrices with different dimensions.
        '''

        multiplied_matrix = [[0 for i in range(len(self.matrix_two[0]))] for j in range(len(self.matrix_one))]

        # iterate through rows
        for row_one in range(len(self.matrix_one)):
            # iterate through columns matrix_two
            for column in range(len(self.matrix_two[0])):
                # iterate through rows of matrix_two
                for row_two in range(len(self.matrix_two)):
                    multiplied_matrix[row_one][column] += self.matrix_one[row_one][row_two] * self.matrix_two[row_two][column]

        return multiplied_matrix


    def transpose(self):
        '''
            The transpose of a matrix is a new matrix whose rows are the columns of the original.
            (This makes the columns of the new matrix the rows of the original)
        '''
        transpose_matrix = [[0 for i in range(len(self.matrix_one))] for j in range(len(self.matrix_one[0]))]

        # iterate through rows
        for row in range(len(self.matrix_one)):
           # iterate through columns
           for column in range(len(self.matrix_one[0])):
               transpose_matrix[column][row] = self.matrix_one[row][column]

        return transpose_matrix


    def rotate(self):
        '''
            Given a matrix, clockwise rotate elements in it.

            .. code-block:: python:

                **Examples:**

                Input
                1    2    3
                4    5    6
                7    8    9

                Output:
                4    1    2
                7    5    3
                8    9    6

            For detailed information visit: https://github.com/keon/algorithms/blob/master/matrix/matrix_rotation.txt
        '''

        top = 0
        bottom = len(self.matrix_one) - 1
        left = 0
        right = len(self.matrix_one[0]) - 1

        while left < right and top < bottom:
            # Store the first element of next row, this element will replace first element of
            # current row
            prev = self.matrix_one[top + 1][left]

            # Move elements of top row one step right
            for i in range(left, right + 1):
                curr = self.matrix_one[top][i]
                self.matrix_one[top][i] = prev
                prev = curr

            top += 1

            # Move elements of rightmost column one step downwards
            for i in range(top, bottom+1):
                curr = self.matrix_one[i][right]
                self.matrix_one[i][right] = prev
                prev = curr

            right -= 1

            # Move elements of bottom row one step left
            for i in range(right, left-1, -1):
                curr = self.matrix_one[bottom][i]
                self.matrix_one[bottom][i] = prev
                prev = curr

            bottom -= 1

            # Move elements of leftmost column one step upwards
            for i in range(bottom, top-1, -1):
                curr = self.matrix_one[i][left]
                self.matrix_one[i][left] = prev
                prev = curr

            left += 1

        return self.matrix_one


    def count_unique_paths(self, m, n):
        '''
            Count the number of unique paths from a[0][0] to a[m-1][n-1]
            We are allowed to move either right or down from a cell in the matrix.
            Approaches-
            (i) Recursion - Recurse starting from a[m-1][n-1], upwards and leftwards,
                           add the path count of both recursions and return count.
            (ii) Dynamic Programming- Start from a[0][0].Store the count in a count
                           matrix. Return count[m-1][n-1]
            Time Complexity = O(mn), Space Complexity = O(mn)

            :param m: number of rows
            :param n: number of columns
        '''
        if m < 1 or n < 1:
            return

        count = [[None for j in range(n)] for i in range(m)]

        # Taking care of the edge cases- matrix of size 1xn or mx1
        for i in range(n):
            count[0][i] = 1
        for j in range(m):
            count[j][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                count[i][j] = count[i-1][j] + count[i][j-1]

        return count[m-1][n-1]
