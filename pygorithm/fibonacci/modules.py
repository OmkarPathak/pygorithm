import pkgutil
def modules():
    """
    Find all functions in pygorithm.data_structures
    """
    import pygorithm.fibonacci
    package = pygorithm.fibonacci
    modules = []
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        modules.append(modname)
    modules.remove('modules')
    modules.sort()
    return modules
