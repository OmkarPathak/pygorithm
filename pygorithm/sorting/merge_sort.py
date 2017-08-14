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
def sort(List):
    """ Function to sort an array using merge sort algorithm """
    if len(List) == 0 or len(List) == 1:
        return List
    else:
        middle = len(List)//2
        a = sort(List[:middle])
        b = sort(List[middle:])
        return merge(a,b)

# time complexities
def time_complexities():
    return '''Best Case: O(nlogn), Average Case: O(nlogn), Worst Case: O(nlogn)'''

# easily retrieve the source code of the sort function
def get_code():
    import inspect
    return inspect.getsource(sort), inspect.getsource(merge)
