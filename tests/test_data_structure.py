# -*- coding: utf-8 -*-
import unittest
import random 

from pygorithm.data_structures import (
    stack,
    queue,
    linked_list,
    tree,
    graph,
    heap,
    trie,
    quadtree)

from pygorithm.geometry import (vector2, rect2)

class TestStack(unittest.TestCase):
    def test_stack(self):
        myStack = stack.Stack()  # create a stack with default stack size 10
        myStack.push(2)
        myStack.push(10)
        myStack.push(12)
        myStack.push(3)

        self.assertEqual(myStack.pop(), 3)
        self.assertEqual(myStack.peek(), 12)
        self.assertFalse(myStack.is_empty())

        nullStack = stack.Stack()

        self.assertEqual(nullStack.pop(), -1)
        self.assertEqual(nullStack.peek(), -1)
        self.assertTrue(nullStack.is_empty())


class TestInfixToPostfix(unittest.TestCase):
    def test_infix_to_postfix(self):
        myExp = 'a+b*(c^d-e)^(f+g*h)-i'
        myExp = [i for i in myExp]
        myStack = stack.Stack(len(myExp))  # create a stack

        result = stack.InfixToPostfix(myExp, myStack)
        resultString = result.infix_to_postfix()
        expectedResult = 'a b c d ^ e - f g h * + ^ * + i -'
        self.assertTrue(resultString, expectedResult)


class TestKruskal(unittest.TestCase):
    def test_minimum_spanning_tree(self):
        """
        test inspired from the example at the following link: https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
        """
        edges_weighted = [((1, 2), 7), ((2, 3), 8), ((1, 4), 5), ((2, 4), 9),
                          ((2, 5), 7), ((3, 5), 5), ((4, 6), 6), ((5, 6), 8),
                          ((5, 7), 9), ((6, 7), 11), ((4, 5), 15)]
        wgraph = graph.WeightedGraph()
        for (u, v), weight in edges_weighted:
            wgraph.add_edge(u, v, weight)
        expected = [((1, 4), 5), ((3, 5), 5), ((4, 6), 6), ((1, 2), 7), ((2, 5), 7), ((5, 7), 9)]
        self.assertEqual(wgraph.kruskal_mst(), expected)

    def test_minimum_spanning_tree_2(self):
        """
        Test inspired by the gif at the left of the page https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
        """
        edges_weighted = [((1, 2), 3), ((1, 5), 1), ((2, 5), 4), ((2, 3), 5), ((3, 5), 6), ((3, 4), 2), ((4, 5), 7)]
        wgraph = graph.WeightedGraph()
        for (u, v), weight in edges_weighted:
            wgraph.add_edge(u, v, weight)
        expected = [((1, 5), 1), ((3, 4), 2), ((1, 2), 3), ((2, 3), 5)]
        self.assertEqual(wgraph.kruskal_mst(), expected)


class TestQueue(unittest.TestCase):
    def test_queue(self):
        myQueue = queue.Queue()  # create a queue with default queue size 10
        myQueue.enqueue(2)
        myQueue.enqueue(10)
        myQueue.enqueue(12)
        myQueue.enqueue(3)

        self.assertEqual(myQueue.dequeue(), 2)
        self.assertEqual(myQueue.dequeue(), 10)
        self.assertFalse(myQueue.is_empty())
        self.assertEqual(myQueue.dequeue(), 12)
        self.assertEqual(myQueue.dequeue(), 3)
        self.assertTrue(myQueue.is_empty())

    def test_deque(self):
        myDeque = queue.Deque()
        myDeque.insert_front(1)  # 1
        myDeque.insert_rear(2)  # 2 1
        myDeque.insert_front(3)  # 2 1 3
        myDeque.insert_rear(10)  # 10 2 1 3

        self.assertEqual(myDeque.delete_rear(), 10)
        self.assertEqual(myDeque.delete_front(), 3)


class TestLinkedList(unittest.TestCase):
    def test_singly_linked_list(self):
        List = linked_list.SinglyLinkedList()
        List.insert_at_start(3)
        List.insert_at_start(5)
        List.insert_at_start(2)
        List.insert_at_start(1)
        List.insert_at_start(4)
        List.insert_at_end(6)

        expectedResult = [4, 1, 2, 5, 3, 6]
        self.assertEqual(List.get_data(), expectedResult)

    def test_doubly_linked_list(self):
        dll = linked_list.DoublyLinkedList()
        dll.insert_at_start(1)
        dll.insert_at_start(2)
        dll.insert_at_end(3)
        dll.insert_at_start(4)

        expectedResult = [4, 2, 1, 3]
        self.assertEqual(dll.get_data(), expectedResult)

        dll.delete(2)

        expectedResult = [4, 1, 3]
        self.assertEqual(dll.get_data(), expectedResult)

    def test_cicular_linked_list(self):
        cll = linked_list.CircularLinkedList()
        cll.insert(1)
        cll.insert(2)
        cll.insert(3)

        expectedResult = [1, 2, 3]
        self.assertEqual(cll.get_data(), expectedResult)


class TestBinaryTree(unittest.TestCase):
    def test_binary_tree(self):
        root = tree.Node(1)
        root.set_left(tree.Node(2))
        root.set_right(tree.Node(3))
        root.left.set_left(tree.Node(4))

        Tree = tree.BinaryTree()
        inorderTraversal = Tree.inorder(root)
        expectedResult = [4, 2, 1, 3]
        self.assertEqual(inorderTraversal, expectedResult)
        preorderTraversal = Tree.preorder(root)
        expectedResult = [1, 2, 4, 3]
        self.assertEqual(preorderTraversal, expectedResult)
        postorderTraversal = Tree.postorder(root)
        expectedResult = [4, 2, 3, 1]
        self.assertEqual(postorderTraversal, expectedResult)


class TestBinarySearchTree(unittest.TestCase):
    def test_binary_search_tree(self):
        root = tree.BinarySearchTree()
        root.insert(10)
        root.insert(12)
        root.insert(5)
        root.insert(4)
        root.insert(20)
        root.insert(8)
        root.insert(7)
        root.insert(15)
        root.insert(13)

        inorder = root.inorder()
        preorder = root.preorder()
        postorder = root.postorder()
        expectedResult = [4, 5, 7, 8, 10, 12, 13, 15, 20]
        self.assertEqual(inorder, expectedResult)
        expectedResult = [10, 5, 4, 8, 7, 12, 20, 15, 13]
        self.assertEqual(preorder, expectedResult)
        expectedResult = [4, 7, 8, 5, 13, 15, 20, 12, 10]
        self.assertEqual(postorder, expectedResult)

        self.assertTrue(root.find(8))


class TestGraph(unittest.TestCase):
    def test_topological_sort(self):
        myGraph = graph.TopologicalSort()
        myGraph.add_edge(5, 2)
        myGraph.add_edge(5, 0)
        myGraph.add_edge(4, 0)
        myGraph.add_edge(4, 1)
        myGraph.add_edge(2, 3)
        myGraph.add_edge(3, 1)

        ans = myGraph.topological_sort()
        expectedResult = [5, 4, 2, 3, 1, 0]
        self.assertEqual(ans, expectedResult)

    def test_cycle_in_directed_graph(self):
        myGraph = graph.CheckCycleDirectedGraph()
        myGraph.add_edge(0, 1)
        myGraph.add_edge(0, 2)
        myGraph.add_edge(1, 2)
        myGraph.add_edge(2, 0)
        myGraph.add_edge(2, 3)
        myGraph.add_edge(3, 3)

        self.assertTrue(myGraph.check_cycle())

    def test_add_edge_in_undirected_graph(self):
        myGraph = graph.CheckCycleUndirectedGraph()
        myGraph.add_edge(0, 1)
        myGraph.add_edge(0, 2)

        setFrom0 = myGraph.graph[0]
        setFrom1 = myGraph.graph[1]
        setFrom2 = myGraph.graph[2]

        self.assertIsNotNone(setFrom0)
        self.assertIsNotNone(setFrom1)
        self.assertIsNotNone(setFrom2)

        self.assertIn(1, setFrom0)
        self.assertIn(0, setFrom1)
        self.assertIn(2, setFrom0)
        self.assertIn(0, setFrom2)

    def test_cycle_in_undirected_graph(self):
        myGraph = graph.CheckCycleUndirectedGraph()
        myGraph.add_edge(0, 1)
        myGraph.add_edge(0, 2)
        myGraph.add_edge(1, 2)
        myGraph.add_edge(2, 0)
        myGraph.add_edge(2, 3)
        myGraph.add_edge(3, 3)

        self.assertTrue(myGraph.check_cycle())

    def test_creating_weighted_undirected_graph(self):
        myGraph = graph.WeightedUndirectedGraph()
        myGraph.add_edge(0, 1, 1)

        self.assertIn(0, myGraph.graph[1])
        self.assertIn(1, myGraph.graph[0])
        self.assertEqual(1, myGraph.get_edge_weight(0, 1))
        self.assertEqual(1, myGraph.get_edge_weight(1, 0))

        myGraph.add_edge(0, 2, 3)

        self.assertIn(0, myGraph.graph[2])
        self.assertIn(0, myGraph.graph[1])
        self.assertIn(1, myGraph.graph[0])
        self.assertIn(2, myGraph.graph[0])
        self.assertEqual(1, myGraph.get_edge_weight(0, 1))
        self.assertEqual(1, myGraph.get_edge_weight(1, 0))
        self.assertEqual(3, myGraph.get_edge_weight(0, 2))
        self.assertEqual(3, myGraph.get_edge_weight(2, 0))

        myGraph.add_edge(2, 3, 7)
        self.assertIn(0, myGraph.graph[2])
        self.assertIn(3, myGraph.graph[2])
        self.assertIn(2, myGraph.graph[3])
        self.assertNotIn(0, myGraph.graph[3])
        self.assertNotIn(3, myGraph.graph[0])
        self.assertEqual(7, myGraph.get_edge_weight(2, 3))
        self.assertIsNone(myGraph.get_edge_weight(0, 3))

    def test_removing_from_weighted_undirected_graph(self):
        myGraph = graph.WeightedUndirectedGraph()
        myGraph.add_edge(0, 1, 1)
        myGraph.add_edge(0, 2, 1)
        myGraph.add_edge(0, 3, 1)
        myGraph.add_edge(0, 4, 1)
        myGraph.add_edge(4, 5, 1)
        myGraph.add_edge(2, 6, 1)

        self.assertEqual(1, myGraph.get_edge_weight(0, 1))
        self.assertEqual(1, myGraph.get_edge_weight(0, 2))
        self.assertEqual(1, myGraph.get_edge_weight(0, 3))
        self.assertEqual(1, myGraph.get_edge_weight(0, 4))
        self.assertEqual(1, myGraph.get_edge_weight(4, 5))
        self.assertEqual(1, myGraph.get_edge_weight(2, 6))

        myGraph.remove_edge(0, 1)

        self.assertIsNone(myGraph.get_edge_weight(0, 1))
        self.assertEqual(1, myGraph.get_edge_weight(0, 2))
        self.assertEqual(1, myGraph.get_edge_weight(0, 3))
        self.assertEqual(1, myGraph.get_edge_weight(0, 4))
        self.assertEqual(1, myGraph.get_edge_weight(4, 5))
        self.assertEqual(1, myGraph.get_edge_weight(2, 6))

        myGraph.remove_edge(0, 2)

        self.assertIsNone(myGraph.get_edge_weight(0, 1))
        self.assertIsNone(myGraph.get_edge_weight(0, 2))
        self.assertEqual(1, myGraph.get_edge_weight(0, 3))
        self.assertEqual(1, myGraph.get_edge_weight(0, 4))
        self.assertEqual(1, myGraph.get_edge_weight(4, 5))
        self.assertEqual(1, myGraph.get_edge_weight(2, 6))

        myGraph.remove_edge(0)

        self.assertIsNone(myGraph.get_edge_weight(0, 1))
        self.assertIsNone(myGraph.get_edge_weight(0, 2))
        self.assertIsNone(myGraph.get_edge_weight(0, 3))
        self.assertIsNone(myGraph.get_edge_weight(0, 4))
        self.assertEqual(1, myGraph.get_edge_weight(4, 5))
        self.assertEqual(1, myGraph.get_edge_weight(2, 6))

    def test_gridify_weighted_undirected_graph(self):
        rt2 = 1.4142135623730951
        myGraph = graph.WeightedUndirectedGraph()
        myGraph.gridify(4, 1)

        self.assertEqual(1, myGraph.get_edge_weight((0, 0), (0, 1)))
        self.assertAlmostEqual(rt2, myGraph.get_edge_weight((0, 0), (1, 1)))

        self.assertIsNone(myGraph.get_edge_weight((0, 0), (2, 0)))
        self.assertEqual(1, myGraph.get_edge_weight((2, 3), (3, 3)))
        self.assertIsNone(myGraph.get_edge_weight((3, 3), (3, 4)))


class TestHeap(unittest.TestCase):
    def test_heap(self):
        myHeap = heap.Heap()
        myHeap.insert(6)
        myHeap.insert(3)
        myHeap.insert(5)
        myHeap.insert(12)
        myHeap.insert(1)

        expectedResult = [1, 3, 5, 12, 6]
        self.assertEqual(myHeap.queue, expectedResult)

        self.assertEqual(myHeap.pop(), 1)
        expectedResult = [3, 5, 12, 6]
        self.assertEqual(myHeap.queue, expectedResult)

        self.assertEqual(myHeap.pop(), 3)
        expectedResult = [5, 12, 6]
        self.assertEqual(myHeap.queue, expectedResult)

        self.assertEqual(myHeap.pop(), 5)
        expectedResult = [6, 12]
        self.assertEqual(myHeap.queue, expectedResult)

        self.assertEqual(myHeap.pop(), 6)
        expectedResult = [12]
        self.assertEqual(myHeap.queue, expectedResult)

        self.assertEqual(myHeap.pop(), 12)
        expectedResult = []
        self.assertEqual(myHeap.queue, expectedResult)


class TestTrie(unittest.TestCase):
    def test_stack(self):
        myTrie = trie.Trie()
        myTrie.insert('the')
        myTrie.insert('turtle')
        myTrie.insert('thesaurus')
        myTrie.insert('chocolate')
        myTrie.insert('flying')

        self.assertEqual(myTrie.find_words('th'), ['the', 'thesaurus'])
        self.assertEqual(myTrie.find_words('e'), None)

        self.assertEqual(myTrie.search('chocolate'), True)
        self.assertEqual(myTrie.search('flying'), True)
        self.assertEqual(myTrie.search('walking'), False)

class TestQuadTreeNode(unittest.TestCase):
    def setUp(self):
        self.rect1 = rect2.Rect2(1, 1, vector2.Vector2(2, 2))
        
    def test_constructor(self):
        ent = quadtree.QuadTreeEntity(self.rect1)
        
        self.assertIsNotNone(ent.aabb)
        self.assertEqual(1, ent.aabb.width)
        self.assertEqual(1, ent.aabb.height)
        self.assertEqual(2, ent.aabb.mincorner.x)
        self.assertEqual(2, ent.aabb.mincorner.y)
        
    def test_repr(self):
        ent = quadtree.QuadTreeEntity(self.rect1)
        
        exp = "quadtreeentity(aabb=rect2(width=1, height=1, mincorner=vector2(x=2, y=2)))"
        self.assertEqual(exp, repr(ent))
    
    def test_str(self):
        ent = quadtree.QuadTreeEntity(self.rect1)
        
        exp = "entity(at rect(1x1 at <2, 2>))"
        self.assertEqual(exp, str(ent))

class TestQuadTree(unittest.TestCase):
    def setUp(self):
        self.big_rect = rect2.Rect2(1000, 1000)
        self.big_rect_sub_1 = rect2.Rect2(500, 500)
        self.big_rect_sub_2 = rect2.Rect2(500, 500, vector2.Vector2(500, 0))
        self.big_rect_sub_3 = rect2.Rect2(500, 500, vector2.Vector2(500, 500))
        self.big_rect_sub_4 = rect2.Rect2(500, 500, vector2.Vector2(0, 500))
        random.seed()
        
    
    def test_constructor(self):
        _tree = quadtree.QuadTree(64, 5, self.big_rect)
        
        self.assertEqual(64, _tree.bucket_size)
        self.assertEqual(5, _tree.max_depth)
        self.assertEqual(1000, _tree.location.width)
        self.assertEqual(1000, _tree.location.height)
        self.assertEqual(0, _tree.location.mincorner.x)
        self.assertEqual(0, _tree.location.mincorner.y)
        self.assertEqual(0, _tree.depth)
        self.assertIsNotNone(_tree.entities)
        self.assertEqual(0, len(_tree.entities))
        self.assertIsNone(_tree.children)
        
    def test_get_quadrant(self):
        _tree = quadtree.QuadTree(64, 5, self.big_rect)
        
        ent1  = quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(320, 175)))
        quad1 = _tree.get_quadrant(ent1)
        self.assertEqual(0, quad1)
        
        ent2  = quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(600, 450)))
        quad2 = _tree.get_quadrant(ent2)
        self.assertEqual(1, quad2)
        
        ent3  = quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(700, 950)))
        quad3 = _tree.get_quadrant(ent3)
        self.assertEqual(2, quad3)
        
        ent4  = quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(0, 505)))
        quad4 = _tree.get_quadrant(ent4)
        self.assertEqual(3, quad4)
        
    def test_get_quadrant_none(self):
        _tree = quadtree.QuadTree(64, 5, self.big_rect)
        
        ent1 = quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(497, 150)))
        self.assertEqual(-1, _tree.get_quadrant(ent1))
        
        ent2 = quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(800, 499)))
        self.assertEqual(-1, _tree.get_quadrant(ent2))
        
        ent3 = quadtree.QuadTreeEntity(rect2.Rect2(15, 15, vector2.Vector2(486, 505)))
        self.assertEqual(-1, _tree.get_quadrant(ent3))
        
        ent4 = quadtree.QuadTreeEntity(rect2.Rect2(5, 20, vector2.Vector2(15, 490)))
        self.assertEqual(-1, _tree.get_quadrant(ent4))
        
        ent5 = quadtree.QuadTreeEntity(rect2.Rect2(17, 34, vector2.Vector2(485, 470)))
        self.assertEqual(-1, _tree.get_quadrant(ent5))
        
    def test_get_quadrant_shifted(self):
        _tree = quadtree.QuadTree(64, 5, self.big_rect_sub_3)
        
        ent1 = quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(515, 600)))
        self.assertEqual(0, _tree.get_quadrant(ent1))
        
        ent2 = quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(800, 550)))
        self.assertEqual(1, _tree.get_quadrant(ent2))
        
        ent3 = quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(950, 850)))
        self.assertEqual(2, _tree.get_quadrant(ent3))
        
        ent4 = quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(515, 751)))
        self.assertEqual(3, _tree.get_quadrant(ent4))
        
    def test_get_quadrant_0_shifted(self):
        _tree = quadtree.QuadTree(64, 5, rect2.Rect2(500, 800, vector2.Vector2(200, 200)))
        
        ent1 = quadtree.QuadTreeEntity(rect2.Rect2(5, 10, vector2.Vector2(445, 224)))
        self.assertEqual(-1, _tree.get_quadrant(ent1))
        
        ent2 = quadtree.QuadTreeEntity(rect2.Rect2(11, 17, vector2.Vector2(515, 585)))
        self.assertEqual(-1, _tree.get_quadrant(ent2))
        
        ent3 = quadtree.QuadTreeEntity(rect2.Rect2(20, 20, vector2.Vector2(440, 700)))
        self.assertEqual(-1, _tree.get_quadrant(ent3))
        
        ent4 = quadtree.QuadTreeEntity(rect2.Rect2(15, 15, vector2.Vector2(215, 590)))
        self.assertEqual(-1, _tree.get_quadrant(ent4))
        
        ent5 = quadtree.QuadTreeEntity(rect2.Rect2(7, 12, vector2.Vector2(449, 589)))
        self.assertEqual(-1, _tree.get_quadrant(ent5))
        
    def test_split_empty(self):
        _tree1 = quadtree.QuadTree(64, 5, self.big_rect)
        self.assertIsNone(_tree1.children)
        _tree1.split()
        self.assertIsNotNone(_tree1.children)
        self.assertEqual(4, len(_tree1.children))
        
        self.assertEqual(500, _tree1.children[0].location.width)
        self.assertEqual(500, _tree1.children[0].location.height)
        self.assertEqual(0, _tree1.children[0].location.mincorner.x)
        self.assertEqual(0, _tree1.children[0].location.mincorner.y)
        self.assertEqual(1, _tree1.children[0].depth)
        self.assertEqual(64, _tree1.children[0].bucket_size)
        self.assertEqual(5, _tree1.children[0].max_depth)
        
        self.assertEqual(500, _tree1.children[1].location.width)
        self.assertEqual(500, _tree1.children[1].location.height)
        self.assertEqual(500, _tree1.children[1].location.mincorner.x)
        self.assertEqual(0, _tree1.children[1].location.mincorner.y)
        
        self.assertEqual(500, _tree1.children[2].location.width)
        self.assertEqual(500, _tree1.children[2].location.height)
        self.assertEqual(500, _tree1.children[2].location.mincorner.x)
        self.assertEqual(500, _tree1.children[2].location.mincorner.y)
        
        self.assertEqual(500, _tree1.children[3].location.width)
        self.assertEqual(500, _tree1.children[3].location.height)
        self.assertEqual(0, _tree1.children[3].location.mincorner.x)
        self.assertEqual(500, _tree1.children[3].location.mincorner.y)
        
        # bottom-right
        _tree2 = _tree1.children[2]
        _tree2.split()
        
        self.assertEqual(250, _tree2.children[0].location.width)
        self.assertEqual(250, _tree2.children[0].location.height)
        self.assertEqual(500, _tree2.children[0].location.mincorner.x)
        self.assertEqual(500, _tree2.children[0].location.mincorner.y)
        self.assertEqual(2, _tree2.children[0].depth)
        
        self.assertEqual(250, _tree2.children[1].location.width)
        self.assertEqual(250, _tree2.children[1].location.height)
        self.assertEqual(750, _tree2.children[1].location.mincorner.x)
        self.assertEqual(500, _tree2.children[1].location.mincorner.y)
        
        self.assertEqual(250, _tree2.children[2].location.width)
        self.assertEqual(250, _tree2.children[2].location.height)
        self.assertEqual(750, _tree2.children[2].location.mincorner.x)
        self.assertEqual(750, _tree2.children[2].location.mincorner.y)
        
        self.assertEqual(250, _tree2.children[3].location.width)
        self.assertEqual(250, _tree2.children[3].location.height)
        self.assertEqual(500, _tree2.children[3].location.mincorner.x)
        self.assertEqual(750, _tree2.children[3].location.mincorner.y)
    
    def test_split_entities(self):
        
        ent1 = quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(50, 50)))
        ent2 = quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(550, 75)))
        ent3 = quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(565, 585)))
        ent4 = quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(95, 900)))
        ent5 = quadtree.QuadTreeEntity(rect2.Rect2(10, 10, vector2.Vector2(495, 167)))
        
        _tree = quadtree.QuadTree(64, 5, self.big_rect, entities = [ ent1, ent2, ent3, ent4, ent5 ])
        _tree.split()
        
        self.assertEqual(1, len(_tree.children[0].entities))
        self.assertEqual(50, _tree.children[0].entities[0].aabb.mincorner.x)
        self.assertEqual(50, _tree.children[0].entities[0].aabb.mincorner.y)
        
        self.assertEqual(1, len(_tree.children[1].entities))
        self.assertEqual(550, _tree.children[1].entities[0].aabb.mincorner.x)
        self.assertEqual(75, _tree.children[1].entities[0].aabb.mincorner.y)
        
        self.assertEqual(1, len(_tree.children[2].entities))
        self.assertEqual(565, _tree.children[2].entities[0].aabb.mincorner.x)
        self.assertEqual(585, _tree.children[2].entities[0].aabb.mincorner.y)
        
        self.assertEqual(1, len(_tree.children[3].entities))
        self.assertEqual(95, _tree.children[3].entities[0].aabb.mincorner.x)
        self.assertEqual(900, _tree.children[3].entities[0].aabb.mincorner.y)
        
        self.assertEqual(1, len(_tree.entities))
        self.assertEqual(495, _tree.entities[0].aabb.mincorner.x)
        self.assertEqual(167, _tree.entities[0].aabb.mincorner.y)
        
        _tree2 = _tree.children[3]
        _tree2.split()
        
        for i in range(3):
            self.assertEqual(0, len(_tree2.children[i].entities), msg="i={}".format(i))
        
        self.assertEqual(1, len(_tree2.children[3].entities))
        self.assertEqual(95, _tree2.children[3].entities[0].aabb.mincorner.x)
        self.assertEqual(900, _tree2.children[3].entities[0].aabb.mincorner.y)
    
    # note for test_think and test_insert we're testing the worst-case scenario
    # for a quad tree (everythings all bunched up in a corner) hence the instant
    # flow to max depth. this case is why max_depth is necessary. To see why you 
    # don't need that much max_depth, the rect sizes are
    # 1000 (depth 0), 500 (depth 1), 250 (depth 2), 125 (depth 3), 62.5 (depth 4),
    # 31.25 (depth 5), 15.625 (depth 6), etc. As you can see, they would have to be 
    # extremely bunched (or stacked) and tiny to actually cause a stack overflow (in the 
    # examples it's only 6 deep), but the quadtree isn't improving anything 
    # (even at 1000x1000 world!) past depth 5 or so.
    
    def test_think(self):
        ent1 = quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(15, 15)))
        ent2 = quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(20, 20)))
        ent3 = quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(0, 0)))
        ent4 = quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(5, 0)))
        ent5 = quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(0, 5)))
        _tree = quadtree.QuadTree(2, 2, self.big_rect, entities = [ ent1, ent2, ent3, ent4, ent5 ])
        
        _tree.think(True)
        
        self.assertIsNotNone(_tree.children) # depth 1
        self.assertIsNotNone(_tree.children[0].children) # depth 2
        self.assertIsNone(_tree.children[0].children[0].children) # depth 3 shouldn't happen because
        self.assertEqual(5, len(_tree.children[0].children[0].entities)) # max_depth reached
        
        
        _tree2 = quadtree.QuadTree(2, 2, self.big_rect, entities = [ ent1, ent2 ])
        _tree2.think(True)
        self.assertIsNone(_tree2.children)
        
    def test_insert(self):
        _tree = quadtree.QuadTree(2, 2, self.big_rect)
        _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(15, 15))))
        self.assertIsNone(_tree.children)
        _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(20, 20))))
        self.assertIsNone(_tree.children)
        _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(0, 0))))
        self.assertIsNotNone(_tree.children) # depth 1
        self.assertIsNotNone(_tree.children[0].children) # depth 2
        self.assertIsNone(_tree.children[0].children[0].children) # depth 3 shouldn't happen because
        self.assertEqual(3, len(_tree.children[0].children[0].entities)) # max_depth reached
        
    def test_retrieve(self):
        _tree = quadtree.QuadTree(2, 2, self.big_rect)
        
        ent1 = quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(25, 25)))
        _tree.insert_and_think(ent1)
        
        retr = _tree.retrieve_collidables(ent1)
        self.assertIsNotNone(retr)
        self.assertEqual(1, len(retr))
        self.assertEqual(25, retr[0].aabb.mincorner.x)
        self.assertEqual(25, retr[0].aabb.mincorner.y)
        
        # note this is not nicely in a quadrant
        ent2 = quadtree.QuadTreeEntity(rect2.Rect2(20, 10, vector2.Vector2(490, 300)))
        _tree.insert_and_think(ent2)
        
        retr = _tree.retrieve_collidables(ent1)
        self.assertIsNotNone(retr)
        self.assertEqual(2, len(retr)) # both ent1 and ent2 are "collidable" in this quad tree
        
        # this should cause a split (bucket_size)
        ent3 = quadtree.QuadTreeEntity(rect2.Rect2(15, 10, vector2.Vector2(700, 450)))
        _tree.insert_and_think(ent3)
        
        ent4 = quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(900, 900)))
        _tree.insert_and_think(ent4)
        
        # ent1 should collide with ent1 or ent2
        # ent2 with ent1 or ent2, or ent3
        # ent3 with ent2 or ent3
        # ent4 with ent2 or ent4
        retr = _tree.retrieve_collidables(ent1)
        self.assertIsNotNone(retr)
        self.assertEqual(2, len(retr)) 
        self.assertIsNotNone(next((e for e in retr if e.aabb.mincorner.x == 25), None), str(retr))
        self.assertIsNotNone(next((e for e in retr if e.aabb.mincorner.x == 490), None), str(retr))
        
        retr = _tree.retrieve_collidables(ent2)
        self.assertEqual(3, len(retr))
        self.assertIsNotNone(next((e for e in retr if e.aabb.mincorner.x == 25), None), str(retr))
        self.assertIsNotNone(next((e for e in retr if e.aabb.mincorner.x == 490), None), str(retr))
        self.assertIsNotNone(next((e for e in retr if e.aabb.mincorner.x == 700), None), str(retr))
        
        retr = _tree.retrieve_collidables(ent3)
        self.assertEqual(2, len(retr))
        self.assertIsNotNone(next((e for e in retr if e.aabb.mincorner.x == 490), None), str(retr))
        self.assertIsNotNone(next((e for e in retr if e.aabb.mincorner.x == 700), None), str(retr))
        
        retr = _tree.retrieve_collidables(ent4)
        self.assertEqual(2, len(retr))
        self.assertIsNotNone(next((e for e in retr if e.aabb.mincorner.x == 900), None), str(retr))
        self.assertIsNotNone(next((e for e in retr if e.aabb.mincorner.x == 490), None), str(retr))
        
    def test_ents_per_depth(self):
        _tree = quadtree.QuadTree(3, 5, self.big_rect)
        _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(75, 35)))) 
        self.assertDictEqual({ 0: 1 }, _tree.find_entities_per_depth())
        _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(300, 499))))
        self.assertDictEqual({ 0: 2 }, _tree.find_entities_per_depth())
        _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(800, 600))))
        self.assertDictEqual({ 0: 3 }, _tree.find_entities_per_depth())
        _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(450, 300))))
        self.assertDictEqual({ 0: 1, 1: 3 }, _tree.find_entities_per_depth())
        _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(150, 100))))
        self.assertDictEqual({ 0: 1, 1: 4 }, _tree.find_entities_per_depth())
        _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(80, 40))))
        self.assertDictEqual({ 0: 1, 1: 1, 2: 4 }, _tree.find_entities_per_depth())
    
    def test_nodes_per_depth(self):
        _tree = quadtree.QuadTree(1, 5, self.big_rect)
        _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(50, 50))))
        self.assertDictEqual({ 0: 1 }, _tree.find_nodes_per_depth())
        _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(450, 450))))
        self.assertDictEqual({ 0: 1, 1: 4, 2: 4 }, _tree.find_nodes_per_depth())
        _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(550, 550))))
        self.assertDictEqual({ 0: 1, 1: 4, 2: 4 }, _tree.find_nodes_per_depth())
        _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(850, 550))))
        self.assertDictEqual({ 0: 1, 1: 4, 2: 8 }, _tree.find_nodes_per_depth())
        
    def test_sum_ents(self):
        # it shouldn't matter where we put entities in, adding entities
        # to a quadtree should increment this number by 1. So lets fuzz!
        
        _tree = quadtree.QuadTree(64, 5, self.big_rect)
        for i in range(1000):
            w = random.randrange(1, 10)
            h = random.randrange(1, 10)
            x = random.uniform(0, 1000 - w)
            y = random.uniform(0, 1000 - h)
            ent = quadtree.QuadTreeEntity(rect2.Rect2(w, h, vector2.Vector2(x, y)))
            _tree.insert_and_think(ent)
            
            # avoid calculating sum every loop which would take way too long.
            # on average, try to sum about 50 times total (5% of the time),
            # evenly split between both ways of summing
            rnd = random.random()
            if rnd > 0.95 and rnd <= 0.975:
                _sum = _tree.sum_entities()
                self.assertEqual(i+1, _sum)
            elif rnd > 0.975:
                _sum = _tree.sum_entities(_tree.find_entities_per_depth())
                self.assertEqual(i+1, _sum)
            
    def test_avg_ents_per_leaf(self):
        _tree = quadtree.QuadTree(3, 5, self.big_rect)
        _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(75, 35)))) 
        self.assertEqual(1, _tree.calculate_avg_ents_per_leaf()) # 1 ent on 1 leaf
        _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(300, 499))))
        self.assertEqual(2, _tree.calculate_avg_ents_per_leaf()) # 2 ents 1 leaf
        _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(800, 600))))
        self.assertEqual(3, _tree.calculate_avg_ents_per_leaf()) # 3 ents 1 leaf
        _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(450, 300))))
        self.assertEqual(0.75, _tree.calculate_avg_ents_per_leaf()) # 3 ents 4 leafs (1 misplaced)
        _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(150, 100))))
        self.assertEqual(1, _tree.calculate_avg_ents_per_leaf()) # 4 ents 4 leafs (1 misplaced)
        _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(450, 450))))
        self.assertAlmostEqual(5/7, _tree.calculate_avg_ents_per_leaf()) # 5 ents 7 leafs (1 misplaced)
        
    def test_misplaced_ents(self):
        _tree = quadtree.QuadTree(3, 5, self.big_rect)
        _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(75, 35)))) 
        self.assertEqual(0, _tree.calculate_weight_misplaced_ents()) # 0 misplaced, 1 total
        _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(300, 499))))
        self.assertEqual(0, _tree.calculate_weight_misplaced_ents()) # 0 misplaced, 2 total
        _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(800, 600))))
        self.assertEqual(0, _tree.calculate_weight_misplaced_ents()) # 0 misplaced 3 total
        _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(550, 700))))
        self.assertAlmostEqual(1, _tree.calculate_weight_misplaced_ents()) # 1 misplaced (1 deep), 4 total
        _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(900, 900))))
        self.assertAlmostEqual(4/5, _tree.calculate_weight_misplaced_ents()) # 1 misplaced (1 deep), 5 total
        _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(5, 5, vector2.Vector2(950, 950))))
        self.assertAlmostEqual(8/6, _tree.calculate_weight_misplaced_ents()) # 1 misplaced (2 deep), 6 total
        
    def test_repr(self):
        _tree = quadtree.QuadTree(1, 5, rect2.Rect2(100, 100))
        
        _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(2, 2, vector2.Vector2(5, 5))))
        _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(2, 2, vector2.Vector2(95, 5))))
        
        _olddiff = self.maxDiff
        def cleanup(self2=self):
            self2.maxDiff = _olddiff
            
        self.addCleanup(cleanup)
        self.maxDiff = None
        self.assertEqual("quadtree(bucket_size=1, max_depth=5, location=rect2(width=100, height=100, mincorner=vector2(x=0, y=0)), depth=0, entities=[], children=[quadtree(bucket_size=1, max_depth=5, location=rect2(width=50.0, height=50.0, mincorner=vector2(x=0, y=0)), depth=1, entities=[quadtreeentity(aabb=rect2(width=2, height=2, mincorner=vector2(x=5, y=5)))], children=None), quadtree(bucket_size=1, max_depth=5, location=rect2(width=50.0, height=50.0, mincorner=vector2(x=50.0, y=0)), depth=1, entities=[quadtreeentity(aabb=rect2(width=2, height=2, mincorner=vector2(x=95, y=5)))], children=None), quadtree(bucket_size=1, max_depth=5, location=rect2(width=50.0, height=50.0, mincorner=vector2(x=50.0, y=50.0)), depth=1, entities=[], children=None), quadtree(bucket_size=1, max_depth=5, location=rect2(width=50.0, height=50.0, mincorner=vector2(x=0, y=50.0)), depth=1, entities=[], children=None)])", repr(_tree))
        
    def test_str(self):
        _tree = quadtree.QuadTree(1, 5, rect2.Rect2(100, 100))
        
        _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(2, 2, vector2.Vector2(5, 5))))
        _tree.insert_and_think(quadtree.QuadTreeEntity(rect2.Rect2(2, 2, vector2.Vector2(95, 5))))
        
        _olddiff = self.maxDiff
        def cleanup(self2=self):
            self2.maxDiff = _olddiff
            
        self.addCleanup(cleanup)
        self.maxDiff = None
        self.assertEqual("quadtree(at rect(100x100 at <0, 0>) with 0 entities here (2 in total); (nodes, entities) per depth: [ 0: (1, 0), 1: (4, 2) ] (allowed max depth: 5, actual: 1), avg ent/leaf: 0.5 (target 1), misplaced weight 0.0 (0 best, >1 bad)", str(_tree))
        
if __name__ == '__main__':
    unittest.main()
