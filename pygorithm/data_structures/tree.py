# Author: OMKAR PATHAK
# Created On: 9th August 2017

# Node class to create a node for binary tree
class Node(object):
    ''' Node class for creating a node for tree.
        Each node has its data and a pointer that points to next node in the Linked List
    '''
    def __init__(self, data = None):
        self.left = None
        self.right = None
        self.data = data

    def set_left(self, node):
        ''' for setting the left child of the node '''
        self.left = node

    def set_right(self, node):
        ''' for setting the right child of the node '''
        self.right = node

    def get_left(self):
        ''' for getting the left child of the node '''
        return self.left

    def get_right(self):
        ''' for getting the right child of the node '''
        return self.right

    def set_data(self, data):
        ''' for setting the data of the node '''
        self.data = data

    def get_data(self):
        ''' for getting the data of the node '''
        return self.data

    # easily retrieve the source code of the Node class
    def get_code(self):
        ''' returns the code of the current class '''
        import inspect
        return inspect.getsource(Node)

class BinaryTree(object):
    ''' BinaryTree class to create a binary tree '''
    def __init__(self):
        self._inorder = []
        self._preorder = []
        self._postorder = []

    def inorder(self, root):
        '''
        @type: root:   Node object
        in this we traverse first to the leftmost node, then print its data and then traverse for rightmost node
        '''
        if root:
            self.inorder(root.get_left())                # traverse to leftmost child
            self._inorder.append(root.get_data())        # get the data of current node
            self.inorder(root.get_right())               # traverse to rightmost child
        return self._inorder

    def preorder(self, root):
        '''
        @type: root:   Node object
        in this we first print the root node and then traverse towards leftmost node and then to the rightmost node
        '''
        if root:
            self._preorder.append(root.get_data())       # get the data of current node
            self.preorder(root.get_left())               # traverse to leftmost child
            self.preorder(root.get_right())              # traverse to rightmost child
        return self._preorder

    def postorder(self, root):
        '''
        @type: root:   Node object
        in this we first traverse to the leftmost node and then to the rightmost node and then print the data
        '''
        if root:
            self.postorder(root.get_left())              # traverse to leftmost child
            self.postorder(root.get_right())             # traverse to rightmost child
            self._postorder.append(root.get_data())      # get the data of current node
        return self._postorder

    # easily retrieve the source code of the BinaryTree class
    def get_code(self):
        ''' returns the code of the current class '''
        import inspect
        return inspect.getsource(BinaryTree)

class BSTNode(object):
    ''' class for creating a node for Binary Search tree '''
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self._inorder = []
        self._preorder = []
        self._postorder = []

    def set_left(self, node):
        ''' for setting the left child of the node '''
        self.leftChild = node

    def set_right(self, node):
        ''' for setting the right child of the node '''
        self.rightChild = node

    def get_left(self):
        ''' returns the left child of the current node '''
        return self.leftChild

    def get_right(self):
        ''' returns the right child of the current node '''
        return self.rightChild

    # for setting data of a node
    def set_data(self, data):
        ''' for setting the data of a node '''
        self.data = data

    # for getting data of a node
    def get_data(self):
        ''' returns the data of the current node '''
        return self.data

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

    def min_val_bst_node(self, BSTNode):
        ''' for returning the node with the lowest value '''
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
            temp = self.min_val_bst_node(self.rightChild)
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
        in this we first traverse to the leftmost node and then print the data and then move to the rightmost child
        '''
        if root:
            self.inorder(root.get_left())                # traverse to leftmost child
            self._inorder.append(root.get_data())        # get the data of current node
            self.inorder(root.get_right())               # traverse to rightmost child
        return self._inorder

    def preorder(self, root):
        '''
        @type: root:   Node object
        in this we first print the root node and then traverse towards leftmost node and then to the rightmost node
        '''
        if root:
            self._preorder.append(root.get_data())       # get the data of current node
            self.preorder(root.get_left())               # traverse to leftmost child
            self.preorder(root.get_right())              # traverse to rightmost child
        return self._preorder

    def postorder(self, root):
        '''
        @type: root:   Node object
        in this we first traverse to the leftmost node and then to the rightmost node and then print the data
        '''
        if root:
            self.postorder(root.get_left())              # traverse to leftmost child
            self.postorder(root.get_right())             # traverse to rightmost child
            self._postorder.append(root.get_data())      # get the data of current node
        return self._postorder

    # easily retrieve the source code of the BSTNode class
    def get_code(self):
        ''' returns the code of current class '''
        import inspect
        return inspect.getsource(BSTNode)

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        ''' inserts a node in the tree '''
        if self.root:
            return self.root.insert(data)
        else:
            self.root = BSTNode(data)
            return True

    def delete(self, data):
        ''' deletes the node with the specified data from the tree '''
        if self.root is not None:
            return self.root.delete(data)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        ''' finding the preorder of the tree '''
        if self.root is not None:
            return self.root.preorder(self.root)

    def inorder(self):
        ''' finding the inorder of the tree '''
        print()
        if self.root is not None:
            return self.root.inorder(self.root)

    def postorder(self):
        ''' finding the postorder of the tree '''
        print()
        if self.root is not None:
            return self.root.postorder(self.root)

    # easily retrieve the source code of the BinarySearchTree class
    def get_code(self):
        ''' returns the code of the current class '''
        import inspect
        return inspect.getsource(BinarySearchTree)
