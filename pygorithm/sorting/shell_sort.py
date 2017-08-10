# Author: OMKAR PATHAK
# Created On: 31st July 2017

# Best Case O(n logn); Average Case O(depends on gap sequence); Worst Case O(n^2)

# shell sort algorithm
def sort(myList):
    gap = len(myList) // 2
    while gap > 0:
        for i in range(gap, len(myList)):
            currentItem = myList[i]
            j = i
            while j >= gap and myList[j - gap] > currentItem:
                myList[j] = myList[j - gap]
                j -= gap
            myList[j] = currentItem
        gap //= 2

    return myList

# time complexities
def time_complexities():
    return '''Best Case: O(nlogn), Average Case: O(depends on gap sequence), Worst Case: O(n)'''

# easily retrieve the source code of the sort function
def get_code():
    import inspect
    return inspect.getsource(sort)
