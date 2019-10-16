def brick_sort(arr):
    """Performs an odd-even in-place sort, which is a variation of a bubble
    sort.

    https://www.geeksforgeeks.org/odd-even-sort-brick-sort/

    :param arr: the array of values to sort
    :return: the sorted array
    """
    # Initially array is unsorted
    is_sorted = False
    while not is_sorted:
        is_sorted = True

        for i in range(1, len(arr) - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

        for i in range(0, len(arr) - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

    return arr
