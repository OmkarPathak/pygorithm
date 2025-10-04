"""
Author: ADWAITA JADHAV
Created On: 4th October 2025

Bingo Sort Algorithm
Time Complexity: O(n + k) where k is the range of input, O(n^2) worst case
Space Complexity: O(1)

Bingo Sort is a variation of selection sort that is particularly efficient
when there are many duplicate elements in the array. It processes all
elements with the same value in a single pass.
"""
import inspect


def sort(_list):
    """
    Sort a list using Bingo Sort algorithm
    
    :param _list: list of values to sort
    :return: sorted list
    """
    if not _list or len(_list) <= 1:
        return _list[:]
    
    # Make a copy to avoid modifying the original list
    arr = _list[:]
    n = len(arr)
    
    # Find the minimum and maximum values
    min_val = max_val = arr[0]
    for i in range(1, n):
        if arr[i] < min_val:
            min_val = arr[i]
        if arr[i] > max_val:
            max_val = arr[i]
    
    # If all elements are the same, return the array
    if min_val == max_val:
        return arr
    
    # Bingo sort main algorithm
    bingo = min_val
    next_pos = 0
    
    while next_pos < n:
        # Find next bingo value
        next_bingo = max_val
        for i in range(next_pos, n):
            if arr[i] > bingo and arr[i] < next_bingo:
                next_bingo = arr[i]
        
        # Place all instances of current bingo value at correct positions
        for i in range(next_pos, n):
            if arr[i] == bingo:
                arr[i], arr[next_pos] = arr[next_pos], arr[i]
                next_pos += 1
        
        bingo = next_bingo
        
        # If no next bingo found, we're done
        if next_bingo == max_val:
            break
    
    return arr


def bingo_sort_optimized(_list):
    """
    Optimized version of Bingo Sort
    
    :param _list: list of values to sort
    :return: sorted list
    """
    if not _list or len(_list) <= 1:
        return _list[:]
    
    arr = _list[:]
    n = len(arr)
    
    # Find min and max
    min_val = max_val = arr[0]
    for val in arr:
        if val < min_val:
            min_val = val
        if val > max_val:
            max_val = val
    
    if min_val == max_val:
        return arr
    
    # Bingo sort main algorithm
    bingo = min_val
    next_bingo = max_val
    largest_pos = n - 1
    next_pos = 0
    
    while bingo < next_bingo:
        # Find next bingo value and place current bingo values
        start_pos = next_pos
        
        for i in range(start_pos, largest_pos + 1):
            if arr[i] == bingo:
                arr[i], arr[next_pos] = arr[next_pos], arr[i]
                next_pos += 1
            elif arr[i] < next_bingo:
                next_bingo = arr[i]
        
        bingo = next_bingo
        next_bingo = max_val
    
    return arr


def bingo_sort_with_duplicates(_list):
    """
    Bingo sort that efficiently handles many duplicates
    
    :param _list: list of values to sort
    :return: sorted list
    """
    if not _list or len(_list) <= 1:
        return _list[:]
    
    arr = _list[:]
    n = len(arr)
    
    # Count duplicates while finding min/max
    value_count = {}
    min_val = max_val = arr[0]
    
    for val in arr:
        value_count[val] = value_count.get(val, 0) + 1
        if val < min_val:
            min_val = val
        if val > max_val:
            max_val = val
    
    # If only one unique value
    if min_val == max_val:
        return arr
    
    # Reconstruct array using counts
    result = []
    current_val = min_val
    
    while current_val <= max_val:
        if current_val in value_count:
            result.extend([current_val] * value_count[current_val])
        
        # Find next value
        next_val = max_val + 1
        for val in value_count:
            if val > current_val and val < next_val:
                next_val = val
        
        current_val = next_val
    
    return result


def is_suitable_for_bingo_sort(_list):
    """
    Check if the list is suitable for bingo sort (has many duplicates)
    
    :param _list: list to check
    :return: True if suitable, False otherwise
    """
    if not _list or len(_list) <= 1:
        return False
    
    unique_count = len(set(_list))
    total_count = len(_list)
    
    # If less than 50% unique elements, bingo sort is beneficial
    return unique_count / total_count < 0.5


def count_duplicates(_list):
    """
    Count the number of duplicate elements in the list
    
    :param _list: list to analyze
    :return: dictionary with element counts
    """
    if not _list:
        return {}
    
    counts = {}
    for item in _list:
        counts[item] = counts.get(item, 0) + 1
    
    return counts


def bingo_sort_stable(_list):
    """
    Stable version of bingo sort (maintains relative order of equal elements)
    
    :param _list: list of values to sort
    :return: sorted list maintaining stability
    """
    if not _list or len(_list) <= 1:
        return _list[:]
    
    # Create list of (value, original_index) pairs
    indexed_list = [(val, i) for i, val in enumerate(_list)]
    
    # Sort by value, then by original index for stability
    indexed_list.sort(key=lambda x: (x[0], x[1]))
    
    # Extract just the values
    return [val for val, _ in indexed_list]


def analyze_efficiency(_list):
    """
    Analyze if bingo sort would be more efficient than other sorting algorithms
    
    :param _list: list to analyze
    :return: dictionary with analysis results
    """
    if not _list:
        return {"suitable": False, "reason": "Empty list"}
    
    n = len(_list)
    unique_count = len(set(_list))
    duplicate_ratio = 1 - (unique_count / n)
    
    analysis = {
        "total_elements": n,
        "unique_elements": unique_count,
        "duplicate_ratio": duplicate_ratio,
        "suitable": duplicate_ratio > 0.3,
        "efficiency_gain": max(0, duplicate_ratio * 100)
    }
    
    if duplicate_ratio > 0.5:
        analysis["recommendation"] = "Highly recommended - many duplicates"
    elif duplicate_ratio > 0.3:
        analysis["recommendation"] = "Recommended - moderate duplicates"
    else:
        analysis["recommendation"] = "Not recommended - few duplicates"
    
    return analysis


def compare_with_other_sorts(_list):
    """
    Compare bingo sort performance characteristics with other algorithms
    
    :param _list: list to analyze
    :return: performance comparison
    """
    analysis = analyze_efficiency(_list)
    n = len(_list) if _list else 0
    
    comparison = {
        "bingo_sort": {
            "best_case": "O(n + k)" if analysis.get("suitable", False) else "O(n^2)",
            "average_case": "O(n + k)" if analysis.get("suitable", False) else "O(n^2)",
            "worst_case": "O(n^2)",
            "space": "O(1)",
            "stable": "No (unless using stable variant)"
        },
        "quick_sort": {
            "best_case": "O(n log n)",
            "average_case": "O(n log n)",
            "worst_case": "O(n^2)",
            "space": "O(log n)",
            "stable": "No"
        },
        "merge_sort": {
            "best_case": "O(n log n)",
            "average_case": "O(n log n)",
            "worst_case": "O(n log n)",
            "space": "O(n)",
            "stable": "Yes"
        }
    }
    
    return comparison


def time_complexities():
    """
    Return information on time complexity
    :return: string
    """
    return ("Best Case: O(n + k) where k is range of input, "
            "Average Case: O(n + k) with many duplicates or O(n^2), "
            "Worst Case: O(n^2)")


def get_code():
    """
    Easily retrieve the source code of the sort function
    :return: source code
    """
    return inspect.getsource(sort)