import pkgutil


def modules():
    """
    Find all functions in pygorithm.pathfinding
    """
    import pygorithm.pathfinding
    package = pygorithm.pathfinding
    modules = []
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        modules.append(modname)
    modules.remove('modules')
    modules.sort()
    return modules
