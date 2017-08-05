# Author: OMKAR PATHAK
# Created On: 31st July 2017

# Best O(n^2); Average O(n^2); Worst O(n^2)

# Bubble Sorting algorithm
def sort(List):
    for i in range(len(List)):
        for j in range(len(List) - 1, i, -1):
            if List[j] < List[j - 1]:
                List[j], List[j - 1] = List[j - 1], List[j]
    return List

# time complexities
def time_complexities():
    return '''Best Case: O(n ^ 2), Average Case: O(n ^ 2), Worst Case: O(n ^ 2)'''

# easily retrieve the source code of the sort function
def get_code():
    import inspect
    return inspect.getsource(sort)
