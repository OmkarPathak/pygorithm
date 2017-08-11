# Author: OMKAR PATHAK
# Created On: 9th August 2017

# Node class to create a node for binary tree
class Node(object):
    def __init__(self, data = None):
        self.left = None
        self.right = None
        self.data = data

    # for setting left node
    def set_left(self, node):
        self.left = node

    # for setting right node
    def set_right(self, node):
        self.right = node

    # for getting the left node
    def get_left(self):
        return self.left

    # for getting right node
    def get_right(self):
        return self.right

    # for setting data of a node
    def set_data(self, data):
        self.data = data

    # for getting data of a node
    def get_data(self):
        return self.data

    # easily retrieve the source code of the Node class
    def get_code(self):
        import inspect
        return inspect.getsource(Node)

# BinaryTree class to create a binary tree
class BinaryTree(object):
    def __init__(self):
        self._inorder = []
        self._preorder = []
        self._postorder = []

    # in this we traverse first to the leftmost node, then print its data and then traverse for rightmost node
    def inorder(self, root):
        '''
        @type: root:   Node object
        '''
        if root:
            self.inorder(root.get_left())                # traverse to leftmost child
            self._inorder.append(root.get_data())        # get the data of current node
            self.inorder(root.get_right())               # traverse to rightmost child
        return self._inorder

    # in this we first print the root node and then traverse towards leftmost node and then to the rightmost node
    def preorder(self, root):
        '''
        @type: root:   Node object
        '''
        if root:
            self._preorder.append(root.get_data())       # get the data of current node
            self.preorder(root.get_left())               # traverse to leftmost child
            self.preorder(root.get_right())              # traverse to rightmost child
        return self._preorder

    # in this we first traverse to the leftmost node and then to the rightmost node and then print the data
    def postorder(self, root):
        '''
        @type: root:   Node object
        '''
        if root:
            self.postorder(root.get_left())              # traverse to leftmost child
            self.postorder(root.get_right())             # traverse to rightmost child
            self._postorder.append(root.get_data())      # get the data of current node
        return self._postorder

    # easily retrieve the source code of the BinaryTree class
    def get_code(self):
        import inspect
        return inspect.getsource(BinaryTree)

class BSTNode(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self._inorder = []
        self._preorder = []
        self._postorder = []

    # for setting left node
    def set_left(self, node):
        self.leftChild = node

    # for setting right node
    def set_right(self, node):
        self.rightChild = node

    # for getting the left node
    def get_left(self):
        return self.leftChild

    # for getting right node
    def get_right(self):
        return self.rightChild

    # for setting data of a node
    def set_data(self, data):
        self.data = data

    # for getting data of a node
    def get_data(self):
        return self.data

    # easily retrieve the source code of the Node class
    def get_code(self):
        import inspect
        return inspect.getsource(BSTNode)

    def insert(self, data):
        ''' For inserting the data in the Tree '''
        if self.data == data:
            return False        # As BST cannot contain duplicate data

        elif data < self.data:
            ''' Data less than the root data is placed to the left of the root '''
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = BSTNode(data)
                return True

        else:
            ''' Data greater than the root data is placed to the right of the root '''
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = BSTNode(data)
                return True

    def minValueBSTNode(self, BSTNode):
        current = BSTNode

        # loop down to find the leftmost leaf
        while(current.leftChild is not None):
            current = current.leftChild

        return current

    def delete(self, data):
        ''' For deleting the BSTNode '''
        if self is None:
            return root

        # if current BSTNode's data is less than that of root BSTNode, then only search in left subtree else right subtree
        if data < self.data:
            self.leftChild = self.leftChild.delete(data)
        elif data > self.data:
            self.rightChild = self.rightChild.delete(data)
        else:
            # deleting BSTNode with one child
            if self.leftChild is None:
                temp = self.rightChild
                self = None
                return temp
            elif self.rightChild is None:
                temp = self.leftChild
                self = None
                return temp

            # deleting BSTNode with two children
            # first get the inorder successor
            temp = self.minValueBSTNode(self.rightChild)
            self.data = temp.data
            self.rightChild = self.rightChild.delete(temp.data)

        return self

    def find(self, data):
        ''' This function checks whether the specified data is in tree or not '''
        if(data == self.data):
            return True
        elif(data < self.data):
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def inorder(self, root):
        '''
        @type: root:   Node object
        '''
        if root:
            self.inorder(root.get_left())                # traverse to leftmost child
            self._inorder.append(root.get_data())        # get the data of current node
            self.inorder(root.get_right())               # traverse to rightmost child
        return self._inorder

    # in this we first print the root node and then traverse towards leftmost node and then to the rightmost node
    def preorder(self, root):
        '''
        @type: root:   Node object
        '''
        if root:
            self._preorder.append(root.get_data())       # get the data of current node
            self.preorder(root.get_left())               # traverse to leftmost child
            self.preorder(root.get_right())              # traverse to rightmost child
        return self._preorder

    # in this we first traverse to the leftmost node and then to the rightmost node and then print the data
    def postorder(self, root):
        '''
        @type: root:   Node object
        '''
        if root:
            self.postorder(root.get_left())              # traverse to leftmost child
            self.postorder(root.get_right())             # traverse to rightmost child
            self._postorder.append(root.get_data())      # get the data of current node
        return self._postorder

    # easily retrieve the source code of the BSTNode class
    def get_code(self):
        import inspect
        return inspect.getsource(BSTNode)

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = BSTNode(data)
            return True

    def delete(self, data):
        if self.root is not None:
            return self.root.delete(data)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        if self.root is not None:
            return self.root.preorder(self.root)

    def inorder(self):
        print()
        if self.root is not None:
            return self.root.inorder(self.root)

    def postorder(self):
        print()
        if self.root is not None:
            return self.root.postorder(self.root)

    # easily retrieve the source code of the BinarySearchTree class
    def get_code(self):
        import inspect
        return inspect.getsource(BinarySearchTree)
