"""
Author: OMKAR PATHAK
Created On: 3rd August 2017
"""
from string import ascii_letters
import inspect


class Stack(object):
    """
    Stack object
    """
    def __init__(self, limit=10):
        """
        :param limit: the stack size
        """
        self.stack = []
        self.limit = limit

    def __str__(self):
        return ' '.join([str(i) for i in self.stack])

    def push(self, data):
        """
        pushes an item into the stack
        returns -1 if the stack is empty
        """
        if len(self.stack) >= self.limit:
            # indicates stack overflow
            return -1       
        else:
            self.stack.append(data)

    def pop(self):
        """
        pops the topmost item from the stack
        returns -1 if the stack is empty
        """
        if len(self.stack) <= 0:
            # indicates stack underflow
            return -1       
        else:
            return self.stack.pop()

    def peek(self):
        """
        returns the topmost element of the stack
        returns -1 if the stack is empty
        """
        if len(self.stack) <= 0:
            # stack underflow
            return -1       
        else:
            return self.stack[len(self.stack) - 1]

    def is_empty(self):
        """
        checks if the stack is empty
        returns boolean value, True or False
        """
        return self.size() == 0

    def size(self):
        """
        returns the current size of the stack
        """
        return len(self.stack)

    @staticmethod
    def get_code():
        """
        returns the code for current class
        """
        return inspect.getsource(Stack)


class InfixToPostfix(object):
    """InfixToPostfix
    get the postfix of the given infix expression
    """

    def __init__(self, expression=None, stack=None):
        """
        :param expression: the infix expression to be converted to postfix
        :param stack: stack to perform infix to postfix operation
        """
        self.expression = list(expression)
        self.my_stack = stack

    @staticmethod
    def _is_operand(char):
        """
        utility function to find whether the given character is an operator
        """
        # OLD VERSION
        # return ord(char) >= ord('a') and ord(char) <= ord('z') \
        #        or ord(char) >= ord('A') and ord(char) <= ord('Z')
        return True if ord(char) in [ord(c) for c in ascii_letters] else False

    @staticmethod
    def _precedence(char):
        """
        utility function to find precedence of the specified character
        """
        if char == '+' or char == '-':
            return 1
        elif char == '*' or char == '/':
            return 2
        elif char == '^':
            return 3
        else:
            return -1

    def infix_to_postfix(self):
        """
        function to generate postfix expression from infix expression
        """
        postfix = []

        for i in range(len(self.expression)):
            if self._is_operand(self.expression[i]):
                postfix.append(self.expression[i])
            elif self.expression[i] == '(':
                self.my_stack.push(self.expression[i])
            elif self.expression[i] == ')':
                top_operator = self.my_stack.pop()
                while not self.my_stack.is_empty() and top_operator != '(':
                    postfix.append(top_operator)
                    top_operator = self.my_stack.pop()
            else:
                while not self.my_stack.is_empty() and self._precedence(self.expression[i]) <= self._precedence(
                        self.my_stack.peek()):
                    postfix.append(self.my_stack.pop())
                self.my_stack.push(self.expression[i])

        while not self.my_stack.is_empty():
            postfix.append(self.my_stack.pop())
        return ' '.join(postfix)

    @staticmethod
    def get_code():
        """
        returns the code of the current class
        """
        return inspect.getsource(InfixToPostfix)
