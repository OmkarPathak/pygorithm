def inplace_insertion_sort(arr, start_ind, end_ind):
    """
    Performs an in-place insertion sort over a continuous slice of an
    array. A natural way to avoid this would be to use numpy arrays,
    where slicing does not copy.

    This is in-place and has no result.

    :param arr: the array to sort
    :param start_ind: the index to begin sorting at
    :param end_ind: the index to end sorting at. This index is excluded
        from the sort (i.e., len(arr) is ok)
    """
    for i in range(start_ind + 1, end_ind):
        current_number = arr[i]

        for j in range(i - 1, start_ind - 1, -1):
            if arr[j] > current_number:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                arr[j + 1] = current_number
                break


# iterative Timsort function to sort the
# array[0...n-1] (similar to merge sort)
def tim_sort(arr, run=32):
    """
    Tim sort algorithm. See https://en.wikipedia.org/wiki/Timsort.
    This is performed in-place.

    :param arr: list of values to sort
    :param run: the largest array that is sorted with an insertion sort.
    :return: the sorted array
    """

    # Sort individual subarrays of size run

    for i in range(0, len(arr), run):
        inplace_insertion_sort(arr, i, min(i + run, len(arr)))

    # start merging from size RUN (or 32). It will merge
    # to form size 64, then 128, 256 and so on ....
    size = run
    while size < len(arr):
        # pick starting point of left sub array. We
        # are going to merge arr[left..left+size-1]
        # and arr[left+size, left+2*size-1]
        # After every merge, we increase left by 2*size
        for left in range(0, len(arr), 2 * size):
            # find ending point of left sub array
            # mid+1 is starting point of right sub array
            mid = left + size
            right = min(left + (2 * size), len(arr))

            # merge sub array arr[left.....mid] &
            # arr[mid+1....right]
            merge(arr, left, mid, right)

        size = 2 * size
    return arr

def merge(arr, left, mid, right):
    """
    Merge of two sections of array, both of which are individually
    sorted. The result is that the entire chunk is sorted. Note that right
    edges are exclusive (like slicing).

    This modifies the passed array, but requires a complete copy of the array.

    .. code:: python

        merge([0, -1, 1, 3, 2, 4], 2, 4, 6) # [0, -1, 1, 2, 3, 4]

    :param arr: the array which should have a portion sorted in-place
    :param left: the left-most index which is included in the merge
    :param mid: the first index that belongs to the second section
    :param right: the right-edge in the merge, which is not included in the sort.
    """
    # original array is broken in two parts
    # left and right array
    left_arr = arr[left:mid]
    right_arr = arr[mid:right]

    left_pos = 0
    right_pos = 0
    arr_ind = left
    # after comparing, we merge those two array
    # in larger sub array
    while left_pos < len(left_arr) and right_pos < len(right_arr):
        if left_arr[left_pos] <= right_arr[right_pos]:
            arr[arr_ind] = left_arr[left_pos]
            left_pos += 1
        else:
            arr[arr_ind] = right_arr[right_pos]
            right_pos += 1

        arr_ind += 1

    # copy remaining elements of left, if any
    for i in range(left_pos, len(left_arr)):
        arr[arr_ind] = left_arr[i]
        arr_ind += 1

    # copy remaining element of right, if any
    for i in range(right_pos, len(right_arr)):
        arr[arr_ind] = right_arr[i]
        arr_ind += 1
