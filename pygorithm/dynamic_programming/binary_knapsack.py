"""
Author: Omkar Pathak
Created At: 25th August 2017
"""
import inspect


def knapsack(w, value, weight):
    """
    The knapsack problem or rucksack problem is a problem in combinatorial optimization: Given a set of
    items, each with a weight and a value, determine the number of each item to include in a collection
    so that the total weight is less than or equal to a given limit and the total value is as large as
    possible. It derives its name from the problem faced by someone who is constrained by a fixed-size
    knapsack and must fill it with the most valuable items.

    :param w: maximum weight capacity
    :param value: an array of values of items in the knapsack
    :param weight: an array of weights of items in the knapsack
    """
    if type(value) is not list:
        raise TypeError("binary knapsack only accepts lists, not {}".format(str(type(value))))
    if type(weight) is not list:
        raise TypeError("binary knapsack only accepts lists, not {}".format(str(type(weight))))

    if len(value) != len(weight):
        raise ValueError("both the lists must be of same length")

    # n = number of items
    n = len(value)

    knap_sack = [[0 for _ in range(w+1)] for _ in range(n+1)]

    for j in range(w + 1):
        knap_sack[0][j] = 0

    for i in range(n + 1):
        for w in range(w + 1):
            if weight[i - 1] <= w:
                knap_sack[i][w] = max(value[i - 1] + knap_sack[i - 1][w - weight[i - 1]], knap_sack[i - 1][w])
            else:
                knap_sack[i][w] = knap_sack[i - 1][w]

    return knap_sack[n][w]


def get_code():
    """
    returns the code for the knapsack function
    """
    return inspect.getsource(knapsack)
