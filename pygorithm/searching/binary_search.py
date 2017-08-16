# Author: OMKAR PATHAK
# Created On: 1st August 2017

# Best O(1); Average O(logn); Worst O(logn)

def search(List, target):
    '''This function performs a binary search on a sorted list and returns the position if successful else returns -1'''
    left = 0                # First position of the list
    right = len(List) - 1   # Last position of the list

    try:
        found = False
        while left <= right:    # you can also write while True condition
            mid = (left + right) // 2
            if target == List[mid]:
                found = True
                return mid
            elif target < List[mid]:
                right =  mid - 1
            else:
                left = mid + 1
        if found == False:
            return -1
    except TypeError:
        return -1


# time complexities
def time_complexities():
    return '''Best Case: O(1), Average Case: O(logn), Worst Case: O(logn)'''

# easily retrieve the source code of the search function
def get_code():
    import inspect
    return inspect.getsource(search)
