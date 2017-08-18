"""
List all modules
"""
import pkgutil

# TODO: This can be moved to the __init__.py file in the __all__
# TODO: See the __init__.py file

def modules():
    """
    Find all functions in pygorithm.sorting
    """
    import pygorithm.sorting
    package = pygorithm.sorting
    modules = []
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        modules.append(modname)
    modules.remove('modules')
    modules.sort()
    return modules

