"""
Author: Timothy Moore
Created On: 31th August 2017

Defines a two-dimensional quadtree of arbitrary
depth and bucket size.
"""
import inspect
import math
from collections import deque

from pygorithm.geometry import (vector2, polygon2, rect2)

class QuadTreeEntity(object):
    """
    This is the minimum information required for an object to 
    be usable in a quadtree as an entity. Entities are the 
    things that you are trying to compare in a quadtree.
    
    :ivar aabb: the axis-aligned bounding box of this entity
    :type aabb: :class:`pygorithm.geometry.rect2.Rect2`
    """
    def __init__(self, aabb):
        """
        Create a new quad tree entity with the specified aabb
        
        :param aabb: axis-aligned bounding box
        :type aabb: :class:`pygorithm.geometry.rect2.Rect2`
        """
        self.aabb = aabb
    
    def __repr__(self):
        """
        Create an unambiguous representation of this entity.
        
        Example:
        
        .. code-block:: python
            
            from pygorithm.geometry import (vector2, rect2)
            from pygorithm.data_structures import quadtree
            
            _ent = quadtree.QuadTreeEntity(rect2.Rect2(5, 5))
            
            # prints quadtreeentity(aabb=rect2(width=5, height=5, mincorner=vector2(x=0, y=0)))
            print(repr(_ent))
        
        :returns: unambiguous representation of this quad tree entity
        :rtype: string
        """
        return "quadtreeentity(aabb={})".format(repr(self.aabb))
    
    def __str__(self):
        """
        Create a human readable representation of this entity
        
        Example:
        
        .. code-block:: python
            
            from pygorithm.geometry import (vector2, rect2)
            from pygorithm.data_structures import quadtree
            
            _ent = quadtree.QuadTreeEntity(rect2.Rect2(5, 5))
            
            # prints entity(at rect(5x5 at <0, 0>))
            print(str(_ent))
        
        :returns: human readable representation of this entity
        :rtype: string
        """
        return "entity(at {})".format(str(self.aabb))
        
class QuadTree(object):
    """
    A quadtree is a sorting tool for two-dimensional space, most
    commonly used to reduce the number of required collision 
    calculations in a two-dimensional scene. In this context, 
    the scene is stepped without collision detection, then a 
    quadtree is constructed from all of the boundaries
    
    .. caution::
        
        Just because a quad tree has split does not mean entities will be empty. Any
        entities which overlay any of the lines of the split will be included in the 
        parent of the quadtree.
    
    .. tip::
        
        It is important to tweak bucket size and depth to the problem, but a common error 
        is too small a bucket size. It is typically not reasonable to have a bucket size 
        smaller than 16; A good starting point is 64, then modify as appropriate. Larger
        buckets reduce the overhead of the quad tree which could easily exceed the improvement
        from reduced collision checks. The max depth is typically just a sanity check since 
        depth greater than 4 or 5 would either indicate a badly performing quadtree (too 
        dense objects, use an r-tree or kd-tree) or a very large world (where an iterative 
        quadtree implementation would be appropriate).
    
    :ivar bucket_size: maximum number objects per bucket (before :py:attr:`.max_depth`)
    :type bucket_size: int
    :ivar max_depth: maximum depth of the quadtree 
    :type max_depth: int
    :ivar depth: the depth of this node (0 being the topmost)
    :type depth: int
    :ivar location: where this quad tree node is situated
    :type location: :class:`pygorithm.geometry.rect2.Rect2`
    :ivar entities: the entities in this quad tree and in NO OTHER related quad tree
    :type entities: list of :class:`.QuadTreeEntity`
    :ivar children: either None or the 4 :class:`.QuadTree` children of this node
    :type children: None or list of :class:`.QuadTree`
    """
    
    def __init__(self, bucket_size, max_depth, location, depth = 0, entities = None):
        """
        Initialize a new quad tree. 
        
        .. warning::
            
            Passing entities to this quadtree will NOT cause it to split automatically!
            You must call :py:meth:`.think` for that. This allows for more predictable
            performance per line.
            
        :param bucket_size: the number of entities in this quadtree 
        :type bucket_size: int
        :param max_depth: the maximum depth for automatic splitting 
        :type max_depth: int
        :param location: where this quadtree is located
        :type location: :class:`pygorithm.geometry.rect2.Rect2`
        :param depth: the depth of this node
        :type depth: int
        :param entities: the entities to initialize this quadtree with 
        :type entities: list of :class:`.QuadTreeEntity` or None for empty list
        """
        self.bucket_size = bucket_size
        self.max_depth = max_depth
        self.location = location
        self.depth = depth
        self.entities = entities if entities is not None else []
        self.children = None
    
    def think(self, recursive = False):
        """
        Call :py:meth:`.split` if appropriate
        
        Split this quad tree if it has not split already and it has more 
        entities than :py:attr:`.bucket_size` and :py:attr:`.depth` is 
        less than :py:attr:`.max_depth`.
        
        If `recursive` is True, think is called on the :py:attr:`.children` with 
        recursive set to True after splitting.
        
        :param recursive: if `think(True)` should be called on :py:attr:`.children` (if there are any)
        :type recursive: bool
        """
        if not self.children and self.depth < self.max_depth and len(self.entities) > self.bucket_size:
            self.split()
        
        if recursive:
            if self.children:
                for child in self.children:
                    child.think(True)
    
    def split(self):
        """
        Split this quadtree.
        
        .. caution::
            
            A call to split will always split the tree or raise an error. Use 
            :py:meth:`.think` if you want to ensure the quadtree is operating
            efficiently.
            
        .. caution::
            
            This function will not respect :py:attr:`.bucket_size` or 
            :py:attr:`.max_depth`.
            
        :raises ValueError: if :py:attr:`.children` is not empty
        """
        if self.children:
            raise ValueError("cannot split twice")
        
        _cls = type(self)
        def _cstr(r):
            return _cls(self.bucket_size, self.max_depth, r, self.depth + 1)
        
        _halfwidth = self.location.width / 2
        _halfheight = self.location.height / 2
        _x = self.location.mincorner.x
        _y = self.location.mincorner.y
        
        self.children = [
            _cstr(rect2.Rect2(_halfwidth, _halfheight, vector2.Vector2(_x, _y))),
            _cstr(rect2.Rect2(_halfwidth, _halfheight, vector2.Vector2(_x + _halfwidth, _y))),
            _cstr(rect2.Rect2(_halfwidth, _halfheight, vector2.Vector2(_x + _halfwidth, _y + _halfheight))),
            _cstr(rect2.Rect2(_halfwidth, _halfheight, vector2.Vector2(_x, _y + _halfheight))) ]
            
        _newents = []
        for ent in self.entities:
            quad = self.get_quadrant(ent)
            
            if quad < 0:
                _newents.append(ent)
            else:
                self.children[quad].entities.append(ent)
        self.entities = _newents
        
        
    
    def get_quadrant(self, entity):
        """
        Calculate the quadrant that the specified entity belongs to.
        
        Touching a line is considered overlapping a line. Touching is 
        determined using :py:meth:`math.isclose`
        
        Quadrants are:
        
         - -1: None (it overlaps 2 or more quadrants)
         -  0: Top-left
         -  1: Top-right
         -  2: Bottom-right
         -  3: Bottom-left
         
        .. caution::
            
            This function does not verify the entity is contained in this quadtree.
        
        This operation takes O(1) time.
        
        :param entity: the entity to place
        :type entity: :class:`.QuadTreeEntity`
        :returns: quadrant
        :rtype: int
        """
        
        _aabb = entity.aabb
        _halfwidth = self.location.width / 2
        _halfheight = self.location.height / 2
        _x = self.location.mincorner.x
        _y = self.location.mincorner.y
        
        if math.isclose(_aabb.mincorner.x, _x + _halfwidth):
            return -1
        if math.isclose(_aabb.mincorner.x + _aabb.width, _x + _halfwidth):
            return -1
        if math.isclose(_aabb.mincorner.y, _y + _halfheight):
            return -1
        if math.isclose(_aabb.mincorner.y + _aabb.height, _y + _halfheight):
            return -1
        
        _leftside_isleft = _aabb.mincorner.x < _x + _halfwidth
        _rightside_isleft = _aabb.mincorner.x + _aabb.width < _x + _halfwidth
        
        if _leftside_isleft != _rightside_isleft:
            return -1
        
        _topside_istop = _aabb.mincorner.y < _y + _halfheight
        _botside_istop = _aabb.mincorner.y + _aabb.height < _y + _halfheight
        
        if _topside_istop != _botside_istop:
            return -1
            
        _left = _leftside_isleft
        _top = _topside_istop
        
        if _left:
            if _top:
                return 0
            else:
                return 3
        else:
            if _top:
                return 1
            else:
                return 2
        
    
    def insert_and_think(self, entity):
        """
        Insert the entity into this or the appropriate child.
        
        This also acts as thinking (recursively). Using :py:meth:`.insert_and_think`
        iteratively is slightly less efficient but has more predictable performance
        than initializing with a large number of entities then thinking is slightly
        faster but may hang. Both may exceed recursion depth if :py:attr:`.max_depth`
        is too large.
        
        :param entity: the entity to insert
        :type entity: :class:`.QuadTreeEntity`
        """
        if not self.children and len(self.entities) == self.bucket_size and self.depth < self.max_depth:
            self.split()
        
        quad = self.get_quadrant(entity) if self.children else -1
        if quad < 0:
            self.entities.append(entity)
        else:
            self.children[quad].insert_and_think(entity)
        
    def retrieve_collidables(self, entity, predicate = None):
        """
        Find all entities that could collide with the specified entity.
        
        .. warning::
            
            If entity is, itself, in the quadtree, it will be returned. The 
            predicate may be used to prevent this using your preferred equality
            method.
            
        The predicate takes 1 positional argument (the entity being considered)
        and returns `False` if the entity should never be returned, even if it 
        might collide with the entity. It should return `True` otherwise.
        
        :param entity: the entity to find collidables for
        :type entity: :class:`.QuadTreeEntity`
        :param predicate: the predicate
        :type predicate: :class:`types.FunctionType` or None
        :returns: potential collidables (never `None)
        :rtype: list of :class:`.QuadTreeEntity`
        """
        result = list(filter(predicate, self.entities))
        quadrant = self.get_quadrant(entity) if self.children else -1
        
        if quadrant >= 0:
            result.extend(self.children[quadrant].retrieve_collidables(entity, predicate))
        elif self.children:
            for child in self.children:
                touching, overlapping, alwaysNone = rect2.Rect2.find_intersection(entity.aabb, child.location, find_mtv=False)
                if touching or overlapping:
                    result.extend(child.retrieve_collidables(entity, predicate))
        
        return result
        
    def _iter_helper(self, pred):
        """
        Calls pred on each child and childs child, iteratively.
        
        pred takes one positional argument (the child).
        
        :param pred: function to call
        :type pred: `types.FunctionType`
        """
        
        _stack = deque()
        _stack.append(self)
        
        while _stack:
            curr = _stack.pop()
            if curr.children:
                for child in curr.children:
                    _stack.append(child)
            
            pred(curr)
    
    def find_entities_per_depth(self):
        """
        Calculate the number of nodes and entities at each depth level in this
        quad tree. Only returns for depth levels at or equal to this node.
        
        This is implemented iteratively. See :py:meth:`.__str__` for usage example.
        
        :returns: dict of depth level to number of entities
        :rtype: dict int: int
        """
        
        container = { 'result': {} }
        def handler(curr, container=container):
            container['result'][curr.depth] = container['result'].get(curr.depth, 0) + len(curr.entities)
        self._iter_helper(handler)
        
        return container['result']
    
    def find_nodes_per_depth(self):
        """
        Calculate the number of nodes at each depth level.
        
        This is implemented iteratively. See :py:meth:`.__str__` for usage example.
        
        :returns: dict of depth level to number of nodes
        :rtype: dict int: int
        """
        
        nodes_per_depth = {}
        self._iter_helper(lambda curr, d=nodes_per_depth: d.update({ (curr.depth, d.get(curr.depth, 0) + 1) }))
        return nodes_per_depth
        
    def sum_entities(self, entities_per_depth=None):
        """
        Sum the number of entities in this quad tree and all lower quad trees.
        
        If `entities_per_depth` is not None, that array is used to calculate the sum 
        of entities rather than traversing the tree. Either way, this is implemented
        iteratively. See :py:meth:`.__str__` for usage example.
        
        :param entities_per_depth: the result of :py:meth:`.find_entities_per_depth`
        :type entities_per_depth: `dict int: (int, int)` or None
        :returns: number of entities in this and child nodes
        :rtype: int
        """
        if entities_per_depth is not None:
            return sum(entities_per_depth.values())
            
        container = { 'result': 0 }
        def handler(curr, container=container):
            container['result'] += len(curr.entities)
        self._iter_helper(handler)
        
        return container['result']
        
    def calculate_avg_ents_per_leaf(self):
        """
        Calculate the average number of entities per leaf node on this and child
        quad trees. 
        
        In the ideal case, the average entities per leaf is equal to the bucket size,
        implying maximum efficiency. Note that, as always with averages, this might 
        be misleading if this tree has reached its max depth.
        
        This is implemented iteratively. See :py:meth:`.__str__` for usage example.
        
        :returns: average number of entities at each leaf node
        :rtype: :class:`numbers.Number`
        """
        container = { 'leafs': 0, 'total': 0 }
        def handler(curr, container=container):
            if not curr.children:
                container['leafs'] += 1
                container['total'] += len(curr.entities)
        self._iter_helper(handler)
        return container['total'] / container['leafs']
        
    def calculate_weight_misplaced_ents(self, sum_entities=None):
        """
        Calculate a rating for misplaced entities.
        
        A misplaced entity is one that is not on a leaf node. That weight is multiplied
        by 4*remaining maximum depth of that node, to indicate approximately how 
        many additional calculations are required.
        
        The result is then divided by the total number of entities on this node (either
        calculated using :py:meth:`.sum_entities` or provided) to get the approximate 
        cost of the misplaced nodes in comparison with the placed nodes. A value greater 
        than 1 implies a different tree type (such as r-tree or kd-tree) should probably be
        used.
        
        This is implemented iteratively. See :py:meth:`.__str__` for usage example.
        
        :param sum_entities: the number of entities on this node
        :type sum_entities: int or None
        :returns: weight of misplaced entities
        :rtype: :class:`numbers.Number`
        """
        
        # this iteration requires more context than _iter_helper provides.
        # we must keep track of parents as well in order to correctly update
        # weights
        
        nonleaf_to_max_child_depth_dict = {}
        
        # stack will be (quadtree, list (of parents) or None)
        _stack = deque()
        _stack.append((self, None))
        while _stack:
            curr, parents = _stack.pop()
            if parents:
                for p in parents:
                    nonleaf_to_max_child_depth_dict[p] = max(nonleaf_to_max_child_depth_dict.get(p, 0), curr.depth)
            
            if curr.children:
                new_parents = list(parents) if parents else []
                new_parents.append(curr)
                for child in curr.children:
                    _stack.append((child, new_parents))
        
        _weight = 0
        for nonleaf, maxchilddepth in nonleaf_to_max_child_depth_dict.items():
            _weight += len(nonleaf.entities) * 4 * (maxchilddepth - nonleaf.depth)
        
        _sum = self.sum_entities() if sum_entities is None else sum_entities
        return _weight / _sum
    
    def __repr__(self):
        """
        Create an unambiguous representation of this quad tree.
        
        This is implemented iteratively.
        
        Example:
        
        .. code-block:: python
            
            from pygorithm.geometry import (vector2, rect2)
            from pygorithm.data_structures import quadtree
            
            # create a tree with a up to 2 entities in a bucket that 
            # can have a depth of up to 5.
            _tree = quadtree.QuadTree(1, 5, rect2.Rect2(100, 100))
            
            # add a few entities to the tree
            _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(2, 2, vector2.Vector2(5, 5))))
            _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(2, 2, vector2.Vector2(95, 5))))
            
            # prints quadtree(bucket_size=1, max_depth=5, location=rect2(width=100, height=100, mincorner=vector2(x=0, y=0)), depth=0, entities=[], children=[quadtree(bucket_size=1, max_depth=5, location=rect2(width=50.0, height=50.0, mincorner=vector2(x=0, y=0)), depth=1, entities=[quadtreeentity(aabb=rect2(width=2, height=2, mincorner=vector2(x=5, y=5)))], children=None), quadtree(bucket_size=1, max_depth=5, location=rect2(width=50.0, height=50.0, mincorner=vector2(x=50.0, y=0)), depth=1, entities=[quadtreeentity(aabb=rect2(width=2, height=2, mincorner=vector2(x=95, y=5)))], children=None), quadtree(bucket_size=1, max_depth=5, location=rect2(width=50.0, height=50.0, mincorner=vector2(x=50.0, y=50.0)), depth=1, entities=[], children=None), quadtree(bucket_size=1, max_depth=5, location=rect2(width=50.0, height=50.0, mincorner=vector2(x=0, y=50.0)), depth=1, entities=[], children=None)])
        
        :returns: unambiguous, recursive representation of this quad tree
        :rtype: string
        """
        return "quadtree(bucket_size={}, max_depth={}, location={}, depth={}, entities={}, children={})".format(self.bucket_size, self.max_depth, repr(self.location), self.depth, self.entities, self.children)
    
    def __str__(self):
        """
        Create a human-readable representation of this quad tree
        
        .. caution::
            
            Because of the complexity of quadtrees it takes a fair amount of calculation to
            produce something somewhat legible. All returned statistics have paired functions.
            This uses only iterative algorithms to calculate statistics.
        
        Example:
        
        .. code-block:: python
            
            from pygorithm.geometry import (vector2, rect2)
            from pygorithm.data_structures import quadtree
            
            # create a tree with a up to 2 entities in a bucket that 
            # can have a depth of up to 5.
            _tree = quadtree.QuadTree(2, 5, rect2.Rect2(100, 100))
            
            # add a few entities to the tree
            _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(2, 2, vector2.Vector2(5, 5))))
            _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(2, 2, vector2.Vector2(95, 5))))
            
            # prints quadtree(at rect(100x100 at <0, 0>) with 0 entities here (2 in total); (nodes, entities) per depth: [ 0: (1, 0), 1: (4, 2) ] (allowed max depth: 5, actual: 1), avg ent/leaf: 0.5 (target 1), misplaced weight 0.0 (0 best, >1 bad)
            print(_tree)
        
        :returns: human-readable representation of this quad tree
        :rtype: string
        """
        
        nodes_per_depth = self.find_nodes_per_depth()
        _ents_per_depth = self.find_entities_per_depth()
        
        _nodes_ents_per_depth_str = "[ {} ]".format(', '.join("{}: ({}, {})".format(dep, nodes_per_depth[dep], _ents_per_depth[dep]) for dep in nodes_per_depth.keys()))
        
        _sum = self.sum_entities(entities_per_depth=_ents_per_depth)
        _max_depth = max(_ents_per_depth.keys())
        _avg_ent_leaf = self.calculate_avg_ents_per_leaf()
        _mispl_weight = self.calculate_weight_misplaced_ents(sum_entities=_sum)
        return "quadtree(at {} with {} entities here ({} in total); (nodes, entities) per depth: {} (allowed max depth: {}, actual: {}), avg ent/leaf: {} (target {}), misplaced weight {} (0 best, >1 bad)".format(self.location, len(self.entities), _sum, _nodes_ents_per_depth_str, self.max_depth, _max_depth, _avg_ent_leaf, self.bucket_size, _mispl_weight)
        
    @staticmethod
    def get_code():
        """
        Get the code for the QuadTree class
        
        :returns: code for QuadTree
        :rtype: string
        """
        return inspect.getsource(QuadTree)