# -*- coding: utf-8 -*-
import unittest

from pygorithm.data_structures import (
    stack,
    queue,
    linked_list,
    tree,
    graph,
    heap,
    trie)


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


if __name__ == '__main__':
    unittest.main()
