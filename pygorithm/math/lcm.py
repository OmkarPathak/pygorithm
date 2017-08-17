# Author    : OMKAR PATHAK
# Created at: 16th August 2017

from functools import reduce    # need this line if you're using Python3.x

def lcm(List):
    ''' function to find LCM for given list of elements

        :param List: List of which LCM is to be found out
     '''
    def _lcm(a, b):
        ''' helper function for finding LCM '''
        if a > b:
            greater = a
        else:
            greater = b

        while True:
            if greater % a == 0 and greater % b == 0:
                lcm = greater
                break
            greater += 1

        return lcm

    return reduce(lambda x, y: _lcm(x, y), List)

def get_code():
    """ returns the code for the current class """
    import inspect
    return inspect.getsource(lcm)
