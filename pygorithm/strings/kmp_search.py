"""
Author: ADWAITA JADHAV
Created On: 4th October 2025

Knuth-Morris-Pratt (KMP) String Matching Algorithm
Time Complexity: O(n + m) where n is text length and m is pattern length
Space Complexity: O(m)

The KMP algorithm efficiently finds occurrences of a pattern within a text
by using a failure function to avoid unnecessary character comparisons.
"""
import inspect


def kmp_search(text, pattern):
    """
    Find all occurrences of pattern in text using KMP algorithm
    
    :param text: string to search in
    :param pattern: string pattern to search for
    :return: list of starting indices where pattern is found
    """
    if not text or not pattern:
        return []
    
    if len(pattern) > len(text):
        return []
    
    # Build failure function (LPS array)
    lps = build_lps_array(pattern)
    
    matches = []
    i = 0  # index for text
    j = 0  # index for pattern
    
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        if j == len(pattern):
            matches.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return matches


def build_lps_array(pattern):
    """
    Build the Longest Proper Prefix which is also Suffix (LPS) array
    
    :param pattern: pattern string
    :return: LPS array
    """
    m = len(pattern)
    lps = [0] * m
    length = 0  # length of previous longest prefix suffix
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    
    return lps


def kmp_search_first(text, pattern):
    """
    Find the first occurrence of pattern in text using KMP algorithm
    
    :param text: string to search in
    :param pattern: string pattern to search for
    :return: index of first occurrence or -1 if not found
    """
    if not text or not pattern:
        return -1
    
    if len(pattern) > len(text):
        return -1
    
    lps = build_lps_array(pattern)
    
    i = 0  # index for text
    j = 0  # index for pattern
    
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        if j == len(pattern):
            return i - j
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return -1


def kmp_count_occurrences(text, pattern):
    """
    Count the number of occurrences of pattern in text
    
    :param text: string to search in
    :param pattern: string pattern to search for
    :return: number of occurrences
    """
    return len(kmp_search(text, pattern))


def kmp_search_overlapping(text, pattern):
    """
    Find all occurrences including overlapping ones
    
    :param text: string to search in
    :param pattern: string pattern to search for
    :return: list of starting indices where pattern is found
    """
    if not text or not pattern:
        return []
    
    if len(pattern) > len(text):
        return []
    
    lps = build_lps_array(pattern)
    matches = []
    i = 0  # index for text
    j = 0  # index for pattern
    
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        if j == len(pattern):
            matches.append(i - j)
            # For overlapping matches, use LPS to find next possible match
            j = lps[j - 1]
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return matches


def print_lps_array(pattern):
    """
    Print the LPS array for a given pattern
    
    :param pattern: pattern string
    :return: string representation of LPS array
    """
    if not pattern:
        return "Empty pattern"
    
    lps = build_lps_array(pattern)
    result = f"Pattern: {pattern}\n"
    result += f"LPS:     {lps}\n"
    result += "Index:   " + " ".join(str(i) for i in range(len(pattern)))
    
    return result


def kmp_replace(text, pattern, replacement):
    """
    Replace all occurrences of pattern with replacement string
    
    :param text: original text
    :param pattern: pattern to replace
    :param replacement: replacement string
    :return: text with replacements made
    """
    if not text or not pattern:
        return text
    
    matches = kmp_search(text, pattern)
    if not matches:
        return text
    
    # Replace from right to left to maintain indices
    result = text
    for match_index in reversed(matches):
        result = result[:match_index] + replacement + result[match_index + len(pattern):]
    
    return result


def validate_pattern(pattern):
    """
    Validate if a pattern is suitable for KMP search
    
    :param pattern: pattern to validate
    :return: True if valid, False otherwise
    """
    if not pattern:
        return False
    
    if not isinstance(pattern, str):
        return False
    
    return True


def compare_with_naive(text, pattern):
    """
    Compare KMP results with naive string search
    
    :param text: text to search in
    :param pattern: pattern to search for
    :return: tuple (kmp_matches, naive_matches, are_equal)
    """
    kmp_matches = kmp_search(text, pattern)
    
    # Naive search
    naive_matches = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            naive_matches.append(i)
    
    return kmp_matches, naive_matches, kmp_matches == naive_matches


def time_complexities():
    """
    Return information on time complexity
    :return: string
    """
    return "Best Case: O(n + m), Average Case: O(n + m), Worst Case: O(n + m)"


def get_code():
    """
    Easily retrieve the source code of the kmp_search function
    :return: source code
    """
    return inspect.getsource(kmp_search)