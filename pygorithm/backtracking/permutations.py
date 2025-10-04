"""
Author: ADWAITA JADHAV
Created On: 4th October 2025

Permutations Generator using Backtracking
Time Complexity: O(n! * n) where n is the length of the input
Space Complexity: O(n! * n)

Generate all possible permutations of a given list using backtracking.
"""
import inspect


def generate_permutations(arr):
    """
    Generate all permutations of the given array using backtracking
    
    :param arr: list of elements to permute
    :return: list of all permutations
    """
    if not arr:
        return [[]]
    
    result = []
    
    def backtrack(current_perm, remaining):
        """Recursively generate permutations"""
        if not remaining:
            result.append(current_perm[:])
            return
        
        for i in range(len(remaining)):
            # Choose
            current_perm.append(remaining[i])
            new_remaining = remaining[:i] + remaining[i+1:]
            
            # Explore
            backtrack(current_perm, new_remaining)
            
            # Unchoose (backtrack)
            current_perm.pop()
    
    backtrack([], arr)
    return result


def generate_permutations_iterative(arr):
    """
    Generate all permutations using iterative approach with swapping
    
    :param arr: list of elements to permute
    :return: list of all permutations
    """
    if not arr:
        return [[]]
    
    result = []
    arr_copy = arr[:]
    
    def generate(n):
        if n == 1:
            result.append(arr_copy[:])
            return
        
        for i in range(n):
            generate(n - 1)
            
            # If n is odd, swap first and last element
            if n % 2 == 1:
                arr_copy[0], arr_copy[n-1] = arr_copy[n-1], arr_copy[0]
            # If n is even, swap ith and last element
            else:
                arr_copy[i], arr_copy[n-1] = arr_copy[n-1], arr_copy[i]
    
    generate(len(arr))
    return result


def generate_unique_permutations(arr):
    """
    Generate all unique permutations of an array that may contain duplicates
    
    :param arr: list of elements to permute (may contain duplicates)
    :return: list of unique permutations
    """
    if not arr:
        return [[]]
    
    result = []
    arr_sorted = sorted(arr)
    used = [False] * len(arr_sorted)
    
    def backtrack(current_perm):
        if len(current_perm) == len(arr_sorted):
            result.append(current_perm[:])
            return
        
        for i in range(len(arr_sorted)):
            # Skip used elements
            if used[i]:
                continue
            
            # Skip duplicates: if current element is same as previous
            # and previous is not used, skip current
            if i > 0 and arr_sorted[i] == arr_sorted[i-1] and not used[i-1]:
                continue
            
            # Choose
            used[i] = True
            current_perm.append(arr_sorted[i])
            
            # Explore
            backtrack(current_perm)
            
            # Unchoose
            current_perm.pop()
            used[i] = False
    
    backtrack([])
    return result


def generate_k_permutations(arr, k):
    """
    Generate all k-length permutations of the given array
    
    :param arr: list of elements
    :param k: length of each permutation
    :return: list of k-length permutations
    """
    if k > len(arr) or k < 0:
        return []
    
    if k == 0:
        return [[]]
    
    result = []
    
    def backtrack(current_perm, remaining):
        if len(current_perm) == k:
            result.append(current_perm[:])
            return
        
        for i in range(len(remaining)):
            # Choose
            current_perm.append(remaining[i])
            new_remaining = remaining[:i] + remaining[i+1:]
            
            # Explore
            backtrack(current_perm, new_remaining)
            
            # Unchoose
            current_perm.pop()
    
    backtrack([], arr)
    return result


def count_permutations(n, r=None):
    """
    Count the number of permutations of n items taken r at a time
    
    :param n: total number of items
    :param r: number of items to choose (defaults to n)
    :return: number of permutations
    """
    if r is None:
        r = n
    
    if r > n or r < 0:
        return 0
    
    if r == 0:
        return 1
    
    result = 1
    for i in range(n, n - r, -1):
        result *= i
    
    return result


def is_permutation(arr1, arr2):
    """
    Check if arr2 is a permutation of arr1
    
    :param arr1: first array
    :param arr2: second array
    :return: True if arr2 is a permutation of arr1, False otherwise
    """
    if len(arr1) != len(arr2):
        return False
    
    # Count frequency of each element
    freq1 = {}
    freq2 = {}
    
    for item in arr1:
        freq1[item] = freq1.get(item, 0) + 1
    
    for item in arr2:
        freq2[item] = freq2.get(item, 0) + 1
    
    return freq1 == freq2


def next_permutation(arr):
    """
    Generate the next lexicographically greater permutation
    
    :param arr: current permutation
    :return: next permutation or None if current is the last
    """
    if not arr or len(arr) <= 1:
        return None
    
    arr_copy = arr[:]
    
    # Find the largest index i such that arr[i] < arr[i + 1]
    i = len(arr_copy) - 2
    while i >= 0 and arr_copy[i] >= arr_copy[i + 1]:
        i -= 1
    
    # If no such index exists, this is the last permutation
    if i == -1:
        return None
    
    # Find the largest index j such that arr[i] < arr[j]
    j = len(arr_copy) - 1
    while arr_copy[j] <= arr_copy[i]:
        j -= 1
    
    # Swap arr[i] and arr[j]
    arr_copy[i], arr_copy[j] = arr_copy[j], arr_copy[i]
    
    # Reverse the suffix starting at arr[i + 1]
    arr_copy[i + 1:] = reversed(arr_copy[i + 1:])
    
    return arr_copy


def time_complexities():
    """
    Return information on time complexity
    :return: string
    """
    return "Best Case: O(n! * n), Average Case: O(n! * n), Worst Case: O(n! * n)"


def get_code():
    """
    Easily retrieve the source code of the generate_permutations function
    :return: source code
    """
    return inspect.getsource(generate_permutations)