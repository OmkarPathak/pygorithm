# Author: OMKAR PATHAK
# Created On: 31st July 2017

#  Best = Average = Worst =  O(n + k)

# counting sort algorithm
def sort(myList):
    try:
        maxValue = 0
        for i in range(len(myList)):
            if myList[i] > maxValue:
                maxValue = myList[i]

        buckets = [0] * (maxValue + 1)

        for i in myList:
            buckets[i] += 1

        i = 0
        for j in range(maxValue + 1):
             for a in range(buckets[j]):
                 myList[i] = j
                 i += 1

        return myList

    except TypeError:
        print('Counting Sort can only be applied to integers')

# time complexities
def bestcase_complexity():
    return 'O(n + k)'

def averagecase_complexity():
    return 'O(n + k)'

def worstcase_complexity():
    return 'O(n + k)'

# easily retrieve the source code of the sort function
def get_code():
    import inspect
    return inspect.getsource(sort)
