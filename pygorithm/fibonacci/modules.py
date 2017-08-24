"""
Find all modules in Fibonacci logic.
"""

import pkgutil

import pygorithm.fibonacci


def modules():
    """
    Find all functions in `pygorithm.fibonacci`.
    """
    package = pygorithm.fibonacci

    modules = sorted([
        modname for _, modname, __ in pkgutil.iter_modules(package.__path__) if modname != 'modules'
    ])

    return modules
