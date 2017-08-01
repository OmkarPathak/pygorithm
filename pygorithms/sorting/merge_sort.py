# Author: OMKAR PATHAK
# Created On: 31st July 2017

# Best = Average = Worst = O(nlog(n))

# merge function to merge the separated lists
def merge(a,b):
    """ Function to merge two arrays """
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c

# Code for merge sort
def sort(x):
    """ Function to sort an array using merge sort algorithm """
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = len(x)//2
        a = sort(x[:middle])
        b = sort(x[middle:])
        return merge(a,b)

# time complexities
def bestcase_complexity():
    return 'O(nlogn)'

def averagecase_complexity():
    return 'O(nlogn)'

def worstcase_complexity():
    return 'O(nlogn)'

# easily retrieve the source code of the sort function
def get_code():
    import inspect
    return inspect.getsource(sort), inspect.getsource(merge)
