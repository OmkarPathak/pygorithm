# Author: OMKAR PATHAK
# Created On: 31st July 2017

#  Best = Average = O(nlog(n)), Worst = O(n ^ 2)

# quick_sort algorithm
def sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return sort(left) + middle + sort(right)

# time complexities
def time_complexities():
    return '''Best Case: O(nlogn), Average Case: O(nlogn), Worst Case: O(n ^ 2)'''

# easily retrieve the source code of the sort function
def get_code():
    import inspect
    return inspect.getsource(sort)
