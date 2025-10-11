"""
Author: ADWAITA JADHAV
Created On: 4th October 2025

Edit Distance (Levenshtein Distance) Algorithm
Time Complexity: O(m * n) where m and n are lengths of the two strings
Space Complexity: O(m * n) or O(min(m, n)) with space optimization

The edit distance between two strings is the minimum number of single-character
edits (insertions, deletions, or substitutions) required to change one string
into another.
"""
import inspect


def edit_distance(str1, str2):
    """
    Calculate the edit distance between two strings using dynamic programming
    
    :param str1: first string
    :param str2: second string
    :return: minimum edit distance
    """
    m, n = len(str1), len(str2)
    
    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i  # Delete all characters from str1
    
    for j in range(n + 1):
        dp[0][j] = j  # Insert all characters to get str2
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # Delete
                    dp[i][j - 1],      # Insert
                    dp[i - 1][j - 1]   # Replace
                )
    
    return dp[m][n]


def edit_distance_optimized(str1, str2):
    """
    Calculate edit distance with space optimization (O(min(m, n)) space)
    
    :param str1: first string
    :param str2: second string
    :return: minimum edit distance
    """
    # Make str1 the shorter string for space optimization
    if len(str1) > len(str2):
        str1, str2 = str2, str1
    
    m, n = len(str1), len(str2)
    
    # Use only two rows instead of full matrix
    prev = list(range(m + 1))
    curr = [0] * (m + 1)
    
    for j in range(1, n + 1):
        curr[0] = j
        for i in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                curr[i] = prev[i - 1]
            else:
                curr[i] = 1 + min(prev[i], curr[i - 1], prev[i - 1])
        
        prev, curr = curr, prev
    
    return prev[m]


def edit_distance_with_operations(str1, str2):
    """
    Calculate edit distance and return the sequence of operations
    
    :param str1: first string
    :param str2: second string
    :return: tuple (distance, operations) where operations is list of (operation, char, position)
    """
    m, n = len(str1), len(str2)
    
    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i
    
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # Delete
                    dp[i][j - 1],      # Insert
                    dp[i - 1][j - 1]   # Replace
                )
    
    # Backtrack to find operations
    operations = []
    i, j = m, n
    
    while i > 0 or j > 0:
        if i > 0 and j > 0 and str1[i - 1] == str2[j - 1]:
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + 1:
            operations.append(('replace', str2[j - 1], i - 1))
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            operations.append(('delete', str1[i - 1], i - 1))
            i -= 1
        elif j > 0 and dp[i][j] == dp[i][j - 1] + 1:
            operations.append(('insert', str2[j - 1], i))
            j -= 1
    
    operations.reverse()
    return dp[m][n], operations


def similarity_ratio(str1, str2):
    """
    Calculate similarity ratio between two strings (0.0 to 1.0)
    
    :param str1: first string
    :param str2: second string
    :return: similarity ratio (1.0 means identical, 0.0 means completely different)
    """
    if not str1 and not str2:
        return 1.0
    
    max_len = max(len(str1), len(str2))
    if max_len == 0:
        return 1.0
    
    distance = edit_distance(str1, str2)
    return 1.0 - (distance / max_len)


def is_one_edit_away(str1, str2):
    """
    Check if two strings are one edit away from each other
    
    :param str1: first string
    :param str2: second string
    :return: True if one edit away, False otherwise
    """
    m, n = len(str1), len(str2)
    
    # If length difference is more than 1, they can't be one edit away
    if abs(m - n) > 1:
        return False
    
    # Make str1 the shorter or equal length string
    if m > n:
        str1, str2 = str2, str1
        m, n = n, m
    
    i = j = 0
    found_difference = False
    
    while i < m and j < n:
        if str1[i] != str2[j]:
            if found_difference:
                return False
            
            found_difference = True
            
            if m == n:
                i += 1  # Replace operation
            # For insertion, only increment j
        else:
            i += 1
        
        j += 1
    
    return True


def longest_common_subsequence_length(str1, str2):
    """
    Calculate the length of longest common subsequence
    
    :param str1: first string
    :param str2: second string
    :return: length of LCS
    """
    m, n = len(str1), len(str2)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]


def apply_operations(str1, operations):
    """
    Apply a sequence of edit operations to transform str1
    
    :param str1: original string
    :param operations: list of operations from edit_distance_with_operations
    :return: transformed string
    """
    result = list(str1)
    
    for operation, char, pos in operations:
        if operation == 'insert':
            result.insert(pos, char)
        elif operation == 'delete':
            if pos < len(result):
                result.pop(pos)
        elif operation == 'replace':
            if pos < len(result):
                result[pos] = char
    
    return ''.join(result)


def hamming_distance(str1, str2):
    """
    Calculate Hamming distance between two strings of equal length
    
    :param str1: first string
    :param str2: second string
    :return: Hamming distance or -1 if strings have different lengths
    """
    if len(str1) != len(str2):
        return -1
    
    return sum(c1 != c2 for c1, c2 in zip(str1, str2))


def find_closest_strings(target, candidates, max_distance=None):
    """
    Find strings from candidates that are closest to target
    
    :param target: target string
    :param candidates: list of candidate strings
    :param max_distance: maximum allowed edit distance (None for no limit)
    :return: list of (string, distance) tuples sorted by distance
    """
    if not candidates:
        return []
    
    distances = []
    for candidate in candidates:
        distance = edit_distance(target, candidate)
        if max_distance is None or distance <= max_distance:
            distances.append((candidate, distance))
    
    return sorted(distances, key=lambda x: x[1])


def time_complexities():
    """
    Return information on time complexity
    :return: string
    """
    return "Best Case: O(m * n), Average Case: O(m * n), Worst Case: O(m * n)"


def get_code():
    """
    Easily retrieve the source code of the edit_distance function
    :return: source code
    """
    return inspect.getsource(edit_distance)