# -*- coding: utf-8 -*-
import unittest

from pygorithm.data_structures import (
    stack,
    queue,
    linked_list,
    tree,
    heap)

class TestStack(unittest.TestCase):
    def test_stack(self):
        myStack = stack.Stack()     # create a stack with default stack size 10
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
        myStack = stack.Stack(len(myExp))     # create a stack

        result = stack.InfixToPostfix(myExp, myStack)
        resultString = result.infix_to_postfix()
        expectedResult = 'a b c d ^ e - f g h * + ^ * + i -'
        self.assertTrue(resultString, expectedResult)

class TestQueue(unittest.TestCase):
    def test_queue(self):
        myQueue = queue.Queue()     # create a queue with default queue size 10
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
        myDeque.insert_front(1)    # 1
        myDeque.insert_rear(2)     # 2 1
        myDeque.insert_front(3)    # 2 1 3
        myDeque.insert_rear(10)    # 10 2 1 3

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

class TestHeap(unittest.TestCase):
    def test_heap(self):
        myHeap = heap.Heap(limit = 4)
        myHeap.insert(2)   # [2]
        myHeap.insert(10)  # [2, 10]
        myHeap.insert(12)  # [2, 10, 12]
        myHeap.insert(3)   # [2,  3, 10, 12]
        
        expectedResult = [2, 3, 10, 12]
        self.assertEqual(myHeap.queue(), expectedResult)

        self.assertEqual(myHeap.pop(), 2)
        expectedResult = [3, 10, 12]
        self.assertEqual(myHeap.queue(), expectedResult)

        self.assertEqual(myHeap.pop(), 3)
        expectedResult = [10, 12]
        self.assertEqual(myHeap.queue(), expectedResult)
        
        self.assertEqual(myHeap.pop(), 10)
        expectedResult = [12]
        self.assertEqual(myHeap.queue(), expectedResult)

        self.assertEqual(myHeap.pop(), 12)
        expectedResult = []
        self.assertEqual(myHeap.queue(), expectedResult)

        self.assertTrue(myHeap.is_empty())

if __name__ == '__main__':
    unittest.main()
