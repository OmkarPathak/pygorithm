# Author: OMKAR PATHAK
# Created On: 31st July 2017

#  Best = Average = O(nlog(n)), Worst = O(n ^ 2)

# quick_sort algorithm
def sort(List):
    if len(List) <= 1:
        return List
    pivot = List[len(List) // 2]
    left = [x for x in List if x < pivot]
    middle = [x for x in List if x == pivot]
    right = [x for x in List if x > pivot]
    return sort(left) + middle + sort(right)

# time complexities
def time_complexities():
    return '''Best Case: O(nlogn), Average Case: O(nlogn), Worst Case: O(n ^ 2)'''

# easily retrieve the source code of the sort function
def get_code():
    import inspect
    return inspect.getsource(sort)
