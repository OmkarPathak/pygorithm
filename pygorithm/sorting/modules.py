import pkgutil
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

