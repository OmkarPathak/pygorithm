"""
vector2

Author: Timothy Moore

Defines a simple two-dimensional, mutable vector.
"""

import math

class Vector2(object):
    """
    Define a simple two-dimensional, mutable vector.
    
    .. important::

        Equality is not overriden on vectors, because it is expected that 
        vectors will be used mutably by directly modifying x and y. However, all 
        functions on vectors are immutable (they return a copy) 
    
    :ivar x: The first component of this vector.
    :vartype x: :class:`numbers.Number`
    :ivar y: The second component of this vector.
    :vartype y: :class:`numbers.Number`
    """
    
    def __init__(self, *args, **kwargs):
        """
        Create a new Vector2 from the two components.
        
        Accepts a pair of unnamed parameters, a pair of named x, y parameters, 
        another Vector2, or a tuple with 2 numerics. Examples of each: 
        
        .. code-block:: python

            from pygorithm.geometry import vector2
            
            # A pair of unnamed parameters
            vec1 = vector2.Vector2(0, 5)
            
            # A pair of named parameters
            vec2 = vector2.Vector2(x = 0, y = 5)
            
            # Another vector2
            vec3 = vector2.Vector2(vec2)
            
            # A tuple with two numerics
            vec4 = vector2.Vector2( (0, 5) )
        
        :param args: unnamed arguments (purpose guessed by order)
        :param kwargs: named arguments (purpose known by name)
        """
        
        if len(args) == 2:
            self.x = args[0]
            self.y = args[1]
        elif len(args) == 1:
            if type(args[0]) == tuple:
                self.x = args[0][0]
                self.y = args[0][1]
            else:
                self.x = args[0].x
                self.y = args[0].y
        else:
            assert(len(args) == 0)
            
            self.x = kwargs['x']
            self.y = kwargs['y']
    
    def __add__(self, other):
        """
        Adds the two vectors component wise. 
        
        Example:

        .. code-block:: python

            from pygorithm.geometry import vector2
            
            vec1 = vector2.Vector2(0, 3)
            vec2 = vector2.Vector2(2, 4)
            
            vec3 = vec1 + vec2
            
            # prints <2, 7>
            print(vec3) 
        
        :param other: the vector to add to this one
        :type other: :class:`pygorithm.geometry.vector2.Vector2`
        :returns: a new vector that is the sum of self and other
        :rtype: :class:`pygorithm.geometry.vector2.Vector2`
        """
        
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """
        Subtract the two vectors component wise. 
        
        Example:

        .. code-block:: python

            from pygorithm.geometry import vector2
            
            vec1 = vector2.Vector2(5, 5)
            vec2 = vector2.Vector2(2, 3)
            
            vec3 = vec1 - vec2
            vec4 = vec2 - vec1
            
            # prints <3, 2>
            print(vec3)
            
            # prints <2, 3>
            print(vec4)
        
        :param other: the vector to subtract from this one
        :type other: :class:`pygorithm.geometry.vector2.Vector2`
        :returns: a new vector two that is the difference of self and other
        :rtype: :class:`pygorithm.geometry.vector2.Vector2`
        """
        
        return Vector2(self.x - other.x, self.y - other.y)
        
    def __mul__(self, scale_factor):
        """
        Scale the vector by the specified factor.
        
        .. caution::
        
            This will never perform a dot product. If scale_factor is a Vector2, an
            exception is thrown.
            
        Example:
        
        .. code-block:: python

            from pygorithm.geometry import vector2
            
            vec1 = vector2.Vector2(4, 8)
            
            vec2 = vec1 * 0.5
            
            # prints <2, 4>
            print(vec2)
        
        :param: scale_factor the amount to scale this vector by
        :type scale_factor: :class:`numbers.Number`
        :returns: a new vector that is self scaled by scale_factor
        :rtype: :class:`pygorithm.geometry.vector2.Vector2`
        :raises TypeError: if scale_factor is a Vector2
        """
        
        if type(scale_factor) == Vector2:
            raise TypeError('scale_factor cannot be a Vector2 (use dot!)')
        
        return Vector2(self.x * scale_factor, self.y * scale_factor)
    
    def __rmul__(self, scale_factor):
        """
        Scale the vector by the specified factor.
        
        .. caution::
        
            This will never perform a dot product. If scale_factor is a Vector2, an
            exception is thrown.
        
        Example:
        
        .. code-block:: python

            from pygorithm.geometry import vector2
            
            vec1 = vector2.Vector2(4, 8)
            
            vec2 = 2 * vec1
            
            # prints <8, 16>
            print(vec2)
        
        :param: scale_factor the amount to scale this vector by
        :type scale_factor: :class:`numbers.Number`
        :returns: a new vector that is self scaled by scale_factor
        :rtype: :class:`pygorithm.geometry.vector2.Vector2`
        :raises TypeError: if scale_factor is a Vector2
        """
        
        if type(scale_factor) == Vector2:
            raise TypeError('scale_factor cannot be a Vector2 (use dot!)')
        
        return Vector2(self.x * scale_factor, self.y * scale_factor)
    
    def __repr__(self):
        """
        Create an unambiguous representation of this vector
        
        Example:
        
        .. code-block:: python

            from pygorithm.geometry import vector2
            
            vec = vector2.Vector2(3, 5)
            
            # prints vector2(x=3, y=5)
            print(repr(vec)) 
            
        :returns: an unambiguous representation of this vector
        :rtype: string
        """
        
        return "vector2(x={}, y={})".format(self.x, self.y)
    
    def __str__(self):
        """
        Create a human-readable representation of this vector.
        
        Rounds to 3 decimal places if there are more.
        
        Example:
        
        .. code-block:: python

            from pygorithm.geometry import vector2
            
            vec = vector2.Vector2(7, 11)
            
            # prints <7, 11>
            print(str(vec))
            
            # also prints <7, 11>
            print(vec)
        
        :returns: a human-readable representation of this vector
        :rtype: string
        """
        
        pretty_x = round(self.x * 1000) / 1000
        if pretty_x == math.floor(pretty_x):
            pretty_x = math.floor(pretty_x)
            
        pretty_y = round(self.y * 1000) / 1000
        if pretty_y == math.floor(pretty_y):
            pretty_y = math.floor(pretty_y)
        
        return "<{}, {}>".format(pretty_x, pretty_y)
    
    def dot(self, other):
        """
        Calculate the dot product between this vector and other.
        
        The dot product of two vectors is calculated as so::

            Let v1 be a vector such that v1 = <v1_x, v1_y>
            Let v2 be a vector such that v2 = <v2_x, v2_y>
            
            v1 . v2 = v1_x * v2_x + v1_y * v2_y
        
        Example:

        .. code-block:: python

            from pygorithm.geometry import vector2
            
            vec1 = vector2.Vector2(3, 5)
            vec2 = vector2.Vector2(7, 11)
            
            dot_12 = vec1.dot(vec2)
            
            # prints 76
            print(dot_12) 
            
        :param other: the other vector
        :type other: :class:`pygorithm.geometry.vector2.Vector2`
        :returns: the dot product of self and other
        :rtype: :class:`numbers.Number`
        """
        
        return self.x * other.x + self.y * other.y
    
    def cross(self, other):
        """
        Calculate the z-component of the cross product between this vector and other.
        
        The cross product of two vectors is calculated as so::
        
            Let v1 be a vector such that v1 = <v1_x, v1_y>
            Let v2 be a vector such that v2 = <v2_x, v2_y>
            
            v1 x v2 = v1.x * v2.y - v1.y * v2.x
        
        .. caution::
        
            This is the special case of a cross product in 2 dimensions returning 1 
            value. This is really a vector in the z direction!
        """
        
        return self.x * other.y - self.y * other.x
    
    def rotate(self, *args, **kwargs):
        """
        The named argument "degrees" or "radians" may be passed in to rotate 
        this vector by the specified amount in degrees (or radians), 
        respectively. If both are omitted, the first unnamed argument is 
        assumed to be the amount to rotate in radians. 

        Additionally, the named argument "about" may be passed in to specify 
        about what the vector should be rotated. If omitted then the first 
        unconsumed unnamed argument is assumed to be the vector. If there are 
        no unconsumed unnamed arguments then the origin is assumed. 

        Examples:

        .. code-block:: python

            from pygorithm.geometry import vector2
            import math
            
            vec1 = vector2.Vector2(1, 0)
            
            vec2 = vec1.rotate(math.pi * 0.25)
            
            # prints <0.707, 0.707>
            print(vec2)
            
            vec3 = vec1.rotate(degrees = 45)
            
            # prints <0.707, 0.707>
            print(vec3)
            
            # The following operations are all identical
            
            vec4 = vec1.rotate(math.pi, vector2.Vector2(1, 1))
            vec5 = vec1.rotate(radians = math.pi, about = vector2.Vector2(1, 1))
            vec6 = vec1.rotate(degrees = 180, about = vector2.Vector2(1, 1))
            vec7 = vec1.rotate(vector2.Vector2(1, 1), degrees = 180)
            
            # prints <1, 2>
            print(vec4)
        
        :param args: the unnamed arguments (purpose guessed by position)
        :param kwargs: the named arguments (purpose known by name)
        :returns: the new vector formed by rotating this vector
        :rtype: :class:`pygorithm.geometry.vector2.Vector2`
        """
        
        args_counter = 0
        deg_rads = None
        about = None
        
        if 'radians' in kwargs:
            deg_rads = kwargs['radians']
        elif 'degrees' in kwargs:
            deg_rads = kwargs['degrees'] * math.pi / 180
        else:
            deg_rads = args[args_counter]
            args_counter = args_counter + 1
        
        if 'about' in kwargs:
            about = kwargs['about']
        else:
            if len(args) > args_counter:
                about = args[args_counter]
        
        fixed_x = self.x
        fixed_y = self.y
        
        if about is not None:
            fixed_x -= about.x
            fixed_y -= about.y
        
        rotated_x = fixed_x * math.cos(deg_rads) - fixed_y * math.sin(deg_rads)
        rotated_y = fixed_y * math.cos(deg_rads) + fixed_x * math.sin(deg_rads)
        
        final_x = rotated_x
        final_y = rotated_y
        
        if about is not None:
            final_x += about.x
            final_y += about.y
            
        return Vector2(final_x, final_y)
    
    def normalize(self):
        """
        Create the normalized version of this vector
        
        The normalized version will go in the same direction but will 
        have magnitude of 1.
        
        .. note::
            
            This will never return self, even if this vector is already 
            normalized.
        
        Example:
        
        .. code-block:: python

            from pygorithm.geometry import vector2
            
            vec1 = vector2.Vector2(2, 0)
            
            vec2 = vec1.normalize()
            
            # prints <1, 0>
            print(vec2)
            
        :returns: a new normalized version of this vector
        :rtype: :class:`pygorithm.geometry.vector2.Vector2`
        """
        
        return self * (1 / self.magnitude())
    
    def magnitude_squared(self):
        """
        Calculate the square of the magnitude of this vector.
        
        Example:
        
        .. code-block:: python
        
            from pygorithm.geometry import vector2
            
            vec1 = vector2.Vector2(5, 12)
            magn_sq = vec1.magnitude_squared()
            
            # prints 169 (13^2)
            print(magn_sq)
        
        :returns: square of the magnitude of this vector
        :rtype: :class:`numbers.Number`
        """
        
        return self.x * self.x + self.y * self.y
        
    def magnitude(self):
        """
        Calculate the magnitude of this vector
        
        .. note::
        
            It is substantially faster to operate on magnitude squared
            where possible.
        
        Example:

        .. code-block:: python

            from pygorithm.geometry import vector2
            
            vec1 = vector2.Vector2(3, 4)
            magn = vec1.magnitude()
            
            # prints 5
            print(magn)
        
        :returns: magnitude of this vector
        :rtype: :class:`numbers.Number`
        """
        
        return math.sqrt(self.magnitude_squared())