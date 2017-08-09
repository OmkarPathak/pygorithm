import unittest

from pygorithm.data_structures import (
    stack,
    queue,
    linked_list)

class TestStack(unittest.TestCase):
    def test_stack(self):
        myStack = stack.Stack()     # create a stack with default stack size 10
        myStack.push(2)
        myStack.push(10)
        myStack.push(12)
        myStack.push(3)

        self.assertEqual(myStack.pop(), 3)
        self.assertEqual(myStack.peek(), 12)
        self.assertFalse(myStack.isEmpty())

        nullStack = stack.Stack() 

        self.assertEqual(nullStack.pop(), -1)
        self.assertEqual(nullStack.peek(), -1)
        self.assertTrue(nullStack.isEmpty())

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
        self.assertFalse(myQueue.isEmpty())
        self.assertEqual(myQueue.dequeue(), 12)
        self.assertEqual(myQueue.dequeue(), 3)
        self.assertTrue(myQueue.isEmpty())

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

if __name__ == '__main__':
    unittest.main()
