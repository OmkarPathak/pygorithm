'''
Created by: Pratik Narola (https://github.com/Pratiknarola)
last modified: 14-10-2019
'''





# A function to sort the given list using Gnome sort
def gnome_sort(arr):
    '''
    Gnome Sort also called Stupid sort is based on the concept of a Garden Gnome sorting his flower pots.
    A garden gnome sorts the flower pots by the following method-

    He looks at the flower pot next to him and the previous one;
    if they are in the right order he steps one pot forward, otherwise he swaps them and steps one pot backwards.
    If there is no previous pot (he is at the starting of the pot line), he steps forwards;
    if there is no pot next to him (he is at the end of the pot line), he is done.

    This is an in-place sort.

    :param arr: the array of values to sort
    :return: the sorted array, which is the same reference as arr
    '''
    index = 0
    while index < len(arr):
        if index == 0:
            index = index + 1
        elif arr[index] >= arr[index - 1]:
            index = index + 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index = index - 1

    return arr
