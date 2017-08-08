# Author: OMKAR PATHAK
# Created On: 3rd August July 2017

# stack implementation
class Stack(object):
    '''
    size    : return the current size of the stack
    push    : push an item into the stack
    pop     : pop the topmost item from the stack
    peek    : return the topmost element of the stack
    isEmpty : check if the stack is empty

    '''

    def __init__(self, limit = 10):
        '''
        @param : limit: the stack size
        '''
        self.stack = []
        self.limit = limit

    # for printing the stack contents
    def __str__(self):
        return ' '.join([str(i) for i in self.stack])

    # for pushing an element on to the stack
    def push(self, data):
        if len(self.stack) >= self.limit:
            return -1       # indicates stack overflow
        else:
            self.stack.append(data)

    # for popping the uppermost element
    def pop(self):
        if len(self.stack) <= 0:
            return -1       # indicates stack underflow
        else:
            return self.stack.pop()

    # for peeking the top-most element of the stack
    def peek(self):
        if len(self.stack) <= 0:
            return -1       # stack underflow
        else:
            return self.stack[len(self.stack) - 1]

    # to check if stack is empty
    def isEmpty(self):
        return self.stack == []

    # for checking the size of stack
    def size(self):
        return len(self.stack)

    # easily retrieve the source code of the Stack class
    def get_code(self):
        import inspect
        return inspect.getsource(Stack)

class InfixToPostfix(object):
    '''
    infix_to_postfix : get the postfix of the given infix expression

    '''

    def __init__(self, expression = [], stack = None):
        '''
        @param: expression : the infix expression to be converted to postfix
        @param: stack      : stack to perform infix to postfix operation
        '''
        self.myExp = list(expression)
        self.myStack = stack

    # function to check whether the given character of the expression is operand
    def _isOperand(self, char):
        return (ord(char) >= ord('a') and ord(char) <= ord('z')) or (ord(char) >= ord('A') and ord(char) <= ord('Z'))

    # self defined precedence for each operator
    def _precedence(self, char):
        if char == '+' or char == '-':
            return 1
        elif char == '*' or char  == '/':
            return 2
        elif char == '^':
            return 3
        else:
            return -1

    # function to convert infix to postfix 
    def infix_to_postfix(self):
        postFix = []
        for i in range(len(self.myExp)):
            if (self._isOperand(self.myExp[i])):
                postFix.append(self.myExp[i])
            elif(self.myExp[i] == '('):
                self.myStack.push(self.myExp[i])
            elif(self.myExp[i] == ')'):
                topOperator = self.myStack.pop()
                while(not self.myStack.isEmpty() and topOperator != '('):
                    postFix.append(topOperator)
                    topOperator = self.myStack.pop()
            else:
                while (not self.myStack.isEmpty()) and (self._precedence(self.myExp[i]) <= self._precedence(self.myStack.peek())):
                    postFix.append(self.myStack.pop())
                self.myStack.push(self.myExp[i])

        while(not self.myStack.isEmpty()):
            postFix.append(self.myStack.pop())
        return ' '.join(postFix)

    # easily retrieve the source code of the Stack class
    def get_code(self):
        import inspect
        return inspect.getsource(InfixToPostfix)
