"""
Collection of special math functions
"""
import pkgutil

def modules():
    """
    Find all functions in pygorithm.math
    """
    from pygorithm import math
    package = math
    modules_list = []
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        modules_list.append(modname)
    modules_list.remove('modules')
    modules_list.sort()
    return modules_list

modules_list = modules()

__all__ = modules_list
