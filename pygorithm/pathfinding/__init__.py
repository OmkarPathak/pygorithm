"""
Collection of pathfinding examples
"""
import pkgutil

def modules():
    """
    Find all functions in pygorithm.pathfinding
    """
    from pygorithm import pathfinding
    package = pathfinding
    modules_list = []
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        modules_list.append(modname)
    modules_list.remove('modules')
    modules_list.sort()
    return modules_list

modules_list = modules()

__all__ = modules_list
