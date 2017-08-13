# Author: OMKAR PATHAK
# Created On: 31st July 2017

# Best O(nlog(n)); Average O(nlog(n)); Worst O(nlog(n))

# heap sort algorithm
def sort(List):
    heapify(List)              # create the heap
    end = len(List) - 1
    while end > 0:
        List[end], List[0] = List[0], List[end]
        shiftDown(List, 0, end - 1)
        end -= 1
    return List

def heapify(List):
    ''' This function helps to maintain the heap property '''
    # start = (len(List) - 2) // 2         (faster execution)
    start = len(List) // 2
    while start >= 0:
        shiftDown(List, start, len(List) - 1)
        start -= 1

def shiftDown(List, start, end):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        # right child exists and is greater than left child
        if child + 1 <= end and List[child] < List[child + 1]:
            child += 1
        # if child is greater than root(parent), then swap their positions
        if child <= end and List[root] < List[child]:
            List[root], List[child] = List[child], List[root]
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
