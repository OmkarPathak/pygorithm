# Author: OMKAR PATHAK
# Created On: 31st July 2017

# Best O(n); Average O(n); Worst O(n)

# bucket sort algorithm
def sort(myList, bucketSize = 5):
    from pygorithm.sorting import insertion_sort
    import math

    string = False

    if(len(myList) == 0):
        print('You don\'t have any elements in array!')
    elif all(isinstance(element, str) for element in myList):
        string = True
        myList = [ord(element) for element in myList]

    minValue = myList[0]
    maxValue = myList[0]

    # For finding minimum and maximum values
    for i in range(0, len(myList)):
        if myList[i] < minValue:
            minValue = myList[i]
        elif myList[i] > maxValue:
            maxValue = myList[i]

    # Initialize buckets
    bucketCount = math.floor((maxValue - minValue) / bucketSize) + 1
    buckets = []
    for i in range(0, bucketCount):
        buckets.append([])

    # For putting values in buckets
    for i in range(0, len(myList)):
        buckets[math.floor((myList[i] - minValue) / bucketSize)].append(myList[i])

    # Sort buckets and place back into input array
    sortedArray = []
    for i in range(0, len(buckets)):
        insertion_sort.sort(buckets[i])
        for j in range(0, len(buckets[i])):
            sortedArray.append(buckets[i][j])

    if string:
        return [chr(element) for element in sortedArray]
    else:
        return sortedArray

# time complexities
def time_complexities():
    return '''Best Case: O(n), Average Case: O(n), Worst Case: O(n)'''

# easily retrieve the source code of the sort function
def get_code():
    import inspect
    return inspect.getsource(sort)
