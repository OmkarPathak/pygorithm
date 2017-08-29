"""
Author: OMKAR PATHAK
Created On: 26th August 2017
"""
import inspect


def activity_selection(start_times, finish_times):
    """
    The activity selection problem is a combinatorial optimization problem concerning the selection of
    non-conflicting activities to perform within a given time frame, given a set of activities each marked
    by a start time (si) and finish time (fi). The problem is to select the maximum number of activities
    that can be performed by a single person or machine, assuming that a person can only work on a single
    activity at a time.

    :param start_times: An array that contains start time of all activities
    :param finish_times: An array that conatins finish time of all activities
    """

    if type(start_times) is not list:
        raise TypeError("Activity selection problem only accepts lists, not {}".format(str(type(start_times))))

    if type(finish_times) is not list:
        raise TypeError("Activity selection problem only accepts lists, not {}".format(str(type(finish_times))))

    if len(start_times) != len(finish_times):
        raise ValueError('Length of start_times list and finish_times list must be same')

    n = len(start_times)
    activity = []

    # first activity is also selected
    i = 0
    activity.append(i)

    for j in range(n):
        # If this activity has start time greater than
        # or equal to the finish time of previously
        # selected activity, then select it
        if start_times[j] >= finish_times[i]:
            activity.append(j)
            i = j

    return activity


def get_code():
    """
    returns the code for the activity_selection function
    """
    return inspect.getsource(activity_selection)
