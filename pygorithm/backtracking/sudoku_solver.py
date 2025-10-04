"""
Author: ADWAITA JADHAV
Created On: 4th October 2025

Sudoku Solver using Backtracking
Time Complexity: O(9^(n*n)) where n is the size of the grid
Space Complexity: O(n*n)

Sudoku is a logic-based number-placement puzzle. The objective is to fill 
a 9×9 grid with digits so that each column, each row, and each of the nine 
3×3 subgrids contains all of the digits from 1 to 9.
"""
import inspect


def solve_sudoku(board):
    """
    Solve a Sudoku puzzle using backtracking
    
    :param board: 9x9 2D list representing the Sudoku board (0 for empty cells)
    :return: True if solved, False if no solution exists
    """
    if not board or len(board) != 9 or len(board[0]) != 9:
        return False
    
    def find_empty():
        """Find an empty cell in the board"""
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None
    
    def is_valid(num, pos):
        """Check if placing num at pos is valid"""
        row, col = pos
        
        # Check row
        for j in range(9):
            if board[row][j] == num:
                return False
        
        # Check column
        for i in range(9):
            if board[i][col] == num:
                return False
        
        # Check 3x3 box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] == num:
                    return False
        
        return True
    
    # Find empty cell
    empty = find_empty()
    if not empty:
        return True  # Board is complete
    
    row, col = empty
    
    # Try numbers 1-9
    for num in range(1, 10):
        if is_valid(num, (row, col)):
            board[row][col] = num
            
            if solve_sudoku(board):
                return True
            
            # Backtrack
            board[row][col] = 0
    
    return False


def is_valid_sudoku(board):
    """
    Check if a Sudoku board is valid (not necessarily complete)
    
    :param board: 9x9 2D list representing the Sudoku board
    :return: True if valid, False otherwise
    """
    if not board or len(board) != 9:
        return False
    
    def is_valid_unit(unit):
        """Check if a unit (row, column, or box) is valid"""
        unit = [num for num in unit if num != 0]
        return len(unit) == len(set(unit))
    
    # Check rows
    for row in board:
        if len(row) != 9 or not is_valid_unit(row):
            return False
    
    # Check columns
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid_unit(column):
            return False
    
    # Check 3x3 boxes
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = []
            for i in range(box_row, box_row + 3):
                for j in range(box_col, box_col + 3):
                    box.append(board[i][j])
            if not is_valid_unit(box):
                return False
    
    return True


def print_board(board):
    """
    Print the Sudoku board in a readable format
    
    :param board: 9x9 2D list representing the Sudoku board
    :return: string representation of the board
    """
    if not board:
        return "Invalid board"
    
    board_str = ""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            board_str += "------+-------+------\n"
        
        row_str = ""
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row_str += "| "
            
            if board[i][j] == 0:
                row_str += ". "
            else:
                row_str += str(board[i][j]) + " "
        
        board_str += row_str.strip() + "\n"
    
    return board_str.strip()


def create_empty_board():
    """
    Create an empty 9x9 Sudoku board
    
    :return: 9x9 2D list filled with zeros
    """
    return [[0 for _ in range(9)] for _ in range(9)]


def count_empty_cells(board):
    """
    Count the number of empty cells in the board
    
    :param board: 9x9 2D list representing the Sudoku board
    :return: number of empty cells
    """
    if not board:
        return 0
    
    count = 0
    for row in board:
        for cell in row:
            if cell == 0:
                count += 1
    return count


def time_complexities():
    """
    Return information on time complexity
    :return: string
    """
    return "Best Case: O(1) (if already solved), Average Case: O(9^(n*n)), Worst Case: O(9^(n*n))"


def get_code():
    """
    Easily retrieve the source code of the solve_sudoku function
    :return: source code
    """
    return inspect.getsource(solve_sudoku)