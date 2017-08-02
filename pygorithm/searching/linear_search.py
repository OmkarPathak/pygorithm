# Author: OMKAR PATHAK
# Created On: 1st August 2017

# Best O(1); Average O(n); Worst O(n)

# sequential search algorithm
def search(List, target):
    '''This function returns the position of the target if found else returns -1'''
    position = 0
    while position < len(List):
        if target == List[position]:
            return position
        position += 1
    return -1

# time complexities
def bestcase_complexity():
    return 'O(1)'

def averagecase_complexity():
    return 'O(n)'

def worstcase_complexity():
    return 'O(n)'

# easily retrieve the source code of the sort function
def get_code():
    import inspect
    return inspect.getsource(search)
