# Author: OMKAR PATHAK
# Created On: 31st July 2017

# Best O(n^2); Average O(n^2); Worst O(n^2)

# selection sort algorithm
def sort(List):
    for i in range(len(List) - 1): #For iterating n - 1 times
        minimum = i
        for j in range( i + 1, len(List)): # Compare i and i + 1 element
            if(List[j] < List[minimum]):
                minimum = j
        if(minimum != i):
            List[i], List[minimum] = List[minimum], List[i]
    return List

# time complexities
def bestcase_complexity():
    return 'O(n ^ 2)'

def averagecase_complexity():
    return 'O(n ^ 2)'

def worstcase_complexity():
    return 'O(n ^ 2)'

# easily retrieve the source code of the sort function
def get_code():
    import inspect
    return inspect.getsource(sort)
