# Author: OMKAR PATHAK
# Created On: 31st July 2017

# Best O(nlog(n)); Average O(nlog(n)); Worst O(nlog(n))

# heap sort algorithm
def sort(alist):
    heapify(alist)              # create the heap
    end = len(alist) - 1
    while end > 0:
        alist[end], alist[0] = alist[0], alist[end]
        shiftDown(alist, 0, end - 1)
        end -= 1
    return alist

def heapify(alist):
    ''' This function helps to maintain the heap property '''
    # start = (len(alist) - 2) // 2         (faster execution)
    start = len(alist) // 2
    while start >= 0:
        shiftDown(alist, start, len(alist) - 1)
        start -= 1

def shiftDown(alist, start, end):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        # right child exists and is greater than left child
        if child + 1 <= end and alist[child] < alist[child + 1]:
            child += 1
        # if child is greater than root(parent), then swap their positions
        if child <= end and alist[root] < alist[child]:
            alist[root], alist[child] = alist[child], alist[root]
            root = child
        else:
            return

# time complexities
def time_complexities():
    return '''Best Case: O(nlogn), Average Case: O(nlogn), Worst Case: O(nlogn)'''

# easily retrieve the source code of the sort function
def get_code():
    import inspect
    return inspect.getsource(sort)
