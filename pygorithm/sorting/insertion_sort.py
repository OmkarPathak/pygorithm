# Author: OMKAR PATHAK
# Created On: 31st July 2017

#  Best O(n); Average O(n^2); Worst O(n^2)

# insertion sort algorithm
def sort(List):
    for i in range(1, len(List)):
        currentNumber = List[i]
        for j in range(i - 1, -1, -1):
            if List[j] > currentNumber :
                List[j], List[j + 1] = List[j + 1], List[j]
            else:
                List[j + 1] = currentNumber
                break
    return List

# time complexities
def time_complexities():
    return '''Best Case: O(n), Average Case: O(n ^ 2), Worst Case: O(n ^ 2)'''

# easily retrieve the source code of the sort function
def get_code():
    import inspect
    return inspect.getsource(sort)
