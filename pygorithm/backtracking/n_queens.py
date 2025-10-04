"""
Author: ADWAITA JADHAV
Created On: 4th October 2025

N-Queens Problem using Backtracking
Time Complexity: O(N!)
Space Complexity: O(N)

The N-Queens problem is to place N chess queens on an N×N chessboard 
so that no two queens attack each other.
"""
import inspect


def solve_n_queens(n):
    """
    Solve the N-Queens problem using backtracking
    
    :param n: size of the chessboard (n x n)
    :return: list of all possible solutions, each solution is a list of column positions
    """
    if n <= 0:
        return []
    
    solutions = []
    board = [-1] * n  # board[i] represents the column position of queen in row i
    
    def is_safe(row, col):
        """Check if placing a queen at (row, col) is safe"""
        for i in range(row):
            # Check if queens are in same column or diagonal
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True
    
    def backtrack(row):
        """Recursively place queens using backtracking"""
        if row == n:
            solutions.append(board[:])  # Found a solution
            return
        
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # Backtrack
    
    backtrack(0)
    return solutions


def solve_n_queens_first_solution(n):
    """
    Find the first solution to N-Queens problem
    
    :param n: size of the chessboard (n x n)
    :return: first solution found or None if no solution exists
    """
    if n <= 0:
        return None
    
    board = [-1] * n
    
    def is_safe(row, col):
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True
    
    def backtrack(row):
        if row == n:
            return True
        
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                if backtrack(row + 1):
                    return True
                board[row] = -1
        return False
    
    if backtrack(0):
        return board[:]
    return None


def print_board(solution):
    """
    Print the chessboard with queens placed
    
    :param solution: list representing queen positions
    :return: string representation of the board
    """
    if not solution:
        return "No solution found"
    
    n = len(solution)
    board_str = ""
    
    for i in range(n):
        row = ""
        for j in range(n):
            if solution[i] == j:
                row += "Q "
            else:
                row += ". "
        board_str += row.strip() + "\n"
    
    return board_str.strip()


def count_solutions(n):
    """
    Count the total number of solutions for N-Queens problem
    
    :param n: size of the chessboard
    :return: number of solutions
    """
    return len(solve_n_queens(n))


def time_complexities():
    """
    Return information on time complexity
    :return: string
    """
    return "Best Case: O(N!), Average Case: O(N!), Worst Case: O(N!)"


def get_code():
    """
    Easily retrieve the source code of the solve_n_queens function
    :return: source code
    """
    return inspect.getsource(solve_n_queens)