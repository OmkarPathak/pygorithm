# Author: OMKAR PATHAK
# Created On: 31st July 2017

#  Best = Average = Worst =  O(n + k)

# counting sort algorithm
def sort(List):
    try:
        maxValue = 0
        for i in range(len(List)):
            if List[i] > maxValue:
                maxValue = List[i]

        buckets = [0] * (maxValue + 1)

        for i in List:
            buckets[i] += 1

        i = 0
        for j in range(maxValue + 1):
             for a in range(buckets[j]):
                 List[i] = j
                 i += 1

        return List

    except TypeError:
        print('Counting Sort can only be applied to integers')

# time complexities
def time_complexities():
    return '''Best Case: O(n + k), Average Case: O(n + k), Worst Case: O(n + k)'''

# easily retrieve the source code of the sort function
def get_code():
    import inspect
    return inspect.getsource(sort)
