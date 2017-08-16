# Author: OMKAR PATHAK
# Created On: 31st July 2017

# Best O(n); Average O(n); Worst O(n)

# bucket sort algorithm
def sort(List, bucketSize = 5):
    from pygorithm.sorting import insertion_sort
    import math

    string = False

    if(len(List) == 0):
        print('You don\'t have any elements in array!')
    elif all(isinstance(element, str) for element in List):
        string = True
        List = [ord(element) for element in List]

    minValue = List[0]
    maxValue = List[0]

    # For finding minimum and maximum values
    for i in range(0, len(List)):
        if List[i] < minValue:
            minValue = List[i]
        elif List[i] > maxValue:
            maxValue = List[i]

    # Initialize buckets
    bucketCount = math.floor((maxValue - minValue) / bucketSize) + 1
    buckets = []
    for i in range(0, bucketCount):
        buckets.append([])

    # For putting values in buckets
    for i in range(0, len(List)):
        buckets[math.floor((List[i] - minValue) / bucketSize)].append(List[i])

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
