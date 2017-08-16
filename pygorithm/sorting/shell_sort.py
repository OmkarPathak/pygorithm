# Author: OMKAR PATHAK
# Created On: 31st July 2017

# Best Case O(n logn); Average Case O(depends on gap sequence); Worst Case O(n^2)

# shell sort algorithm
def sort(List):
    gap = len(List) // 2
    while gap > 0:
        for i in range(gap, len(List)):
            currentItem = List[i]
            j = i
            while j >= gap and List[j - gap] > currentItem:
                List[j] = List[j - gap]
                j -= gap
            List[j] = currentItem
        gap //= 2

    return List

# time complexities
def time_complexities():
    return '''Best Case: O(nlogn), Average Case: O(depends on gap sequence), Worst Case: O(n ^ 2)'''

# easily retrieve the source code of the sort function
def get_code():
    import inspect
    return inspect.getsource(sort)
