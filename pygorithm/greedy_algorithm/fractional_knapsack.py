"""
Author: SHARAD BHAT
Created On: 22nd August 2017
"""
import inspect
# TODO: Explain how this works / Explain what a knapsack is


def knapsack(w, item_values, item_weights):
    """
    :param w: maximum weight capacity
    :param item_values: a list of values of items in the knapsack
    :param item_weights: a list of weights of items in the knapsack
    """

    if type(item_values) is not list:
        raise TypeError("fractional knapsack only accepts lists, not {}".format(str(type(item_values))))
    if type(item_weights) is not list:
        raise TypeError("fractional knapsack only accepts lists, not {}".format(str(type(item_weights))))

    if len(item_values) != len(item_weights):
        raise ValueError("length of both lists must be same")

    n = len(item_values)

    fractional_weights = []
    for i in range(0, n):
        fractional_weights.append(item_values[i] / item_weights[i])

    # Sorting items based on maximum fractional profit
    for i in range(0, n):
        maximum = i
        for j in range(i, n):
            if fractional_weights[maximum] < fractional_weights[j]:
                maximum = j

        fractional_weights[i], fractional_weights[maximum] = fractional_weights[maximum], fractional_weights[i]
        item_values[i], item_values[maximum] = item_values[maximum], item_values[i]
        item_weights[i], item_weights[maximum] = item_weights[maximum], item_weights[i]

    # Placing items in knapsack
    remaining_space = w
    profit = 0
    for i in range(0, n):
        if remaining_space > item_weights[i]:
            profit += item_values[i]
            remaining_space -= item_weights[i]
        else:
            profit += fractional_weights[i] * remaining_space
            break

    return profit


def get_code():
    """
    returns the code for the knapsack function
    """
    return inspect.getsource(knapsack)
