'''
Created by: Pratik Narola (https://github.com/Pratiknarola)
last modified: 14-10-2019
'''


def cocktail_sort(arr):
    '''
    Cocktail Sort is a variation of Bubble sort.
    The Bubble sort algorithm always traverses elements from left
    and moves the largest element to its correct position in first iteration
    and second largest in second iteration and so on.
    Cocktail Sort traverses through a given array in both directions alternatively.

    This is an in-place sort.

    :param arr: the array to sort
    :return: the sorted array, which is the same reference as arr
    '''
    swapped = True
    start = 0
    end = len(arr) - 1
    while swapped:
        # reset the swapped flag on entering the loop,
        # because it might be true from a previous
        # iteration.
        swapped = False

        # loop from left to right same as the bubble
        # sort
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # if nothing moved, then array is sorted.
        if not swapped:
            break

        # otherwise, reset the swapped flag so that it
        # can be used in the next stage
        swapped = False

        # move the end point back by one, because
        # item at the end is in its rightful spot
        end -= 1

        # from right to left, doing the same
        # comparison as in the previous stage
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # increase the starting point, because
        # the last stage would have moved the next
        # smallest number to its rightful spot.
        start = start + 1

    return arr
