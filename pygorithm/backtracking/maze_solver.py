"""
Author: ADWAITA JADHAV
Created On: 4th October 2025

Maze Solver using Backtracking
Time Complexity: O(4^(n*m)) where n and m are dimensions of the maze
Space Complexity: O(n*m)

A maze solver that finds a path from start to end using backtracking.
The maze is represented as a 2D grid where 0 represents a path and 1 represents a wall.
"""
import inspect


def solve_maze(maze, start=None, end=None):
    """
    Solve a maze using backtracking to find a path from start to end
    
    :param maze: 2D list representing the maze (0 = path, 1 = wall)
    :param start: tuple (row, col) for start position, defaults to (0, 0)
    :param end: tuple (row, col) for end position, defaults to bottom-right
    :return: list of tuples representing the path, or None if no path exists
    """
    if not maze or not maze[0]:
        return None
    
    rows, cols = len(maze), len(maze[0])
    
    # Set default start and end positions
    if start is None:
        start = (0, 0)
    if end is None:
        end = (rows - 1, cols - 1)
    
    # Check if start and end positions are valid
    if (start[0] < 0 or start[0] >= rows or start[1] < 0 or start[1] >= cols or
        end[0] < 0 or end[0] >= rows or end[1] < 0 or end[1] >= cols or
        maze[start[0]][start[1]] == 1 or maze[end[0]][end[1]] == 1):
        return None
    
    # Create visited matrix
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    path = []
    
    def is_safe(row, col):
        """Check if the cell is safe to visit"""
        return (0 <= row < rows and 0 <= col < cols and 
                maze[row][col] == 0 and not visited[row][col])
    
    def backtrack(row, col):
        """Recursively find path using backtracking"""
        # Mark current cell as visited and add to path
        visited[row][col] = True
        path.append((row, col))
        
        # Check if we reached the destination
        if (row, col) == end:
            return True
        
        # Try all four directions: up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if is_safe(new_row, new_col):
                if backtrack(new_row, new_col):
                    return True
        
        # Backtrack: remove current cell from path and mark as unvisited
        path.pop()
        visited[row][col] = False
        return False
    
    # Start backtracking from the start position
    if backtrack(start[0], start[1]):
        return path[:]
    return None


def solve_maze_all_paths(maze, start=None, end=None):
    """
    Find all possible paths from start to end in a maze
    
    :param maze: 2D list representing the maze (0 = path, 1 = wall)
    :param start: tuple (row, col) for start position
    :param end: tuple (row, col) for end position
    :return: list of all possible paths
    """
    if not maze or not maze[0]:
        return []
    
    rows, cols = len(maze), len(maze[0])
    
    if start is None:
        start = (0, 0)
    if end is None:
        end = (rows - 1, cols - 1)
    
    if (start[0] < 0 or start[0] >= rows or start[1] < 0 or start[1] >= cols or
        end[0] < 0 or end[0] >= rows or end[1] < 0 or end[1] >= cols or
        maze[start[0]][start[1]] == 1 or maze[end[0]][end[1]] == 1):
        return []
    
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    all_paths = []
    current_path = []
    
    def is_safe(row, col):
        return (0 <= row < rows and 0 <= col < cols and 
                maze[row][col] == 0 and not visited[row][col])
    
    def backtrack(row, col):
        visited[row][col] = True
        current_path.append((row, col))
        
        if (row, col) == end:
            all_paths.append(current_path[:])
        else:
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if is_safe(new_row, new_col):
                    backtrack(new_row, new_col)
        
        current_path.pop()
        visited[row][col] = False
    
    backtrack(start[0], start[1])
    return all_paths


def print_maze_with_path(maze, path=None):
    """
    Print the maze with the solution path marked
    
    :param maze: 2D list representing the maze
    :param path: list of tuples representing the solution path
    :return: string representation of the maze with path
    """
    if not maze:
        return "Invalid maze"
    
    rows, cols = len(maze), len(maze[0])
    result = [[' ' for _ in range(cols)] for _ in range(rows)]
    
    # Fill the result with maze structure
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 1:
                result[i][j] = '█'  # Wall
            else:
                result[i][j] = '.'  # Path
    
    # Mark the solution path
    if path:
        for i, (row, col) in enumerate(path):
            if i == 0:
                result[row][col] = 'S'  # Start
            elif i == len(path) - 1:
                result[row][col] = 'E'  # End
            else:
                result[row][col] = '*'  # Path
    
    # Convert to string
    maze_str = ""
    for row in result:
        maze_str += ''.join(row) + '\n'
    
    return maze_str.strip()


def create_sample_maze():
    """
    Create a sample maze for testing
    
    :return: 2D list representing a sample maze
    """
    return [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]


def is_valid_maze(maze):
    """
    Check if a maze is valid (rectangular and contains only 0s and 1s)
    
    :param maze: 2D list to validate
    :return: True if valid, False otherwise
    """
    if not maze or not maze[0]:
        return False
    
    cols = len(maze[0])
    for row in maze:
        if len(row) != cols:
            return False
        for cell in row:
            if cell not in [0, 1]:
                return False
    
    return True


def time_complexities():
    """
    Return information on time complexity
    :return: string
    """
    return "Best Case: O(n*m), Average Case: O(4^(n*m)), Worst Case: O(4^(n*m))"


def get_code():
    """
    Easily retrieve the source code of the solve_maze function
    :return: source code
    """
    return inspect.getsource(solve_maze)