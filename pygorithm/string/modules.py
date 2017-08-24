import pkgutil


def modules():
    """
    Find all functions in pygorithm.string
    """
    import pygorithm.string
    package = pygorithm.string
    modules = []
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        modules.append(modname)
    modules.remove('modules')
    modules.sort()
    return modules
