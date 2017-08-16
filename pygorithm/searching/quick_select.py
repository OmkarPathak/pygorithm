# Author: DION MISIC
# Created On: 11th August 2017

def search(array, n):
    ''' Recursively defined function for finding nth number in unsorted list '''
    def select(array, left, right, n):
        if left == right:
            return array[left]
        split = partition(array, left, right, n)
        length = split - left + 1
        if length == n:
            return array[split]
        elif n < length:
            return select(array, left, split - 1, n)
        else:
            return select(array, split + 1, right, n - length)

    def partition(array, left, right, pivot):
        pivot_val = array[pivot]
        array[pivot], array[right] = array[right], array[pivot]
        store_index = left

        for i in range(left, right):
            if array[i] < pivot_val:
                array[store_index], array[i] = array[i], array[store_index]
                store_index += 1

        array[right], array[store_index] = array[store_index], array[right]
        return store_index

    ans = select(array, 0, len(array) - 1, n)
    return ans

def time_complexities():
    ''' Time Complexity '''
    return '''Best Case: O(n), Average Case: O(n), Worst Case: O(n^2)'''

def get_code():
    ''' Standard code inspection '''
    import inspect
    return inspect.getsource(search)
