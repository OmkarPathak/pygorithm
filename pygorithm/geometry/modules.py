"""
List all modules
"""
import pkgutil

def modules():
    import pygorithm.geometry
    package = pygorithm.geometry
    modules = []
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        modules.append(modname)
    modules.remove('modules')
    modules.sort()
    return modules