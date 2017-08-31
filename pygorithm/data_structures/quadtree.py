"""
Author: Timothy Moore
Created On: 31th August 2017

Defines a two-dimensional quadtree of arbitrary
depth and bucket size.
"""
import inspect

from pygorithm.geometry import (vector2, polygon2, rect2)

class QuadTree(object):
    """
    A quadtree is a sorting tool for two-dimensional space, most
    commonly used to reduce the number of required collision 
    calculations in a two-dimensional scene. In this context, 
    the scene is stepped without collision detection, then a 
    quadtree is constructed from all of the boundaries
    """
    @staticmethod
    def get_code():
        """
        Get the code for the QuadTree class
        
        :returns: code for QuadTree
        :rtype: string
        """
        return inspect.getsource(QuadTree)