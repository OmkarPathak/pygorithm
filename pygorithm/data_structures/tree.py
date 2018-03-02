"""
Author: OMKAR PATHAK
Created On: 9th August 2017

Node class to create a node 
for binary tree
"""
import inspect


class Node(object):
    """
    Node class for creating a node for tree.
    Each node has its data and a pointer
    that points to next node in the Linked List
    """
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def set_left(self, node):
        """
        for setting the left child of the node
        """
        self.left = node

    def set_right(self, node):
        """
        for setting the right child of the node
        """
        self.right = node

    def get_left(self):
        """
        for getting the left child of the node
        """
        return self.left

    def get_right(self):
        """
        for getting the right child of the node
        """
        return self.right

    def set_data(self, data):
        """
        for setting the data of the node
        """
        self.data = data

    def get_data(self):
        """
        for getting the data of the node
        """
        return self.data

    @staticmethod
    def get_code():
        """
        returns the code of the current class
        """
        return inspect.getsource(Node)


class BinaryTree(object):
    """
    BinaryTree class to create a binary tree
    """
    def __init__(self):
        self._in_order = []
        self._pre_order = []
        self._post_order = []

    def insert(self, data):
        """
        insert data to root or create a root node
        """
        if self.root:
           self.root.set_data(data)
        else:
           self.root = Node()
           self.root.set_data(data)
        
    def inorder(self, root):
        """
        in this we traverse first to the leftmost node,
        then print its data and then traverse for rightmost node
        :param root: Node object
        """
        if root:
            # traverse to leftmost child
            self.inorder(root.get_left())
            # get the data of current node
            self._in_order.append(root.get_data())
            # traverse to rightmost child
            self.inorder(root.get_right())
        return self._in_order

    def preorder(self, root):
        """
        in this we first print the root node and then
        traverse towards leftmost node and then to the rightmost node
        :param root: Node object
        """
        if root:
            # get the data of current node
            self._pre_order.append(root.get_data())
            # traverse to leftmost child
            self.preorder(root.get_left())
            # traverse to rightmost child
            self.preorder(root.get_right())
        return self._pre_order

    def postorder(self, root):
        """
        in this we first traverse to the leftmost node and then
        to the rightmost node and then print the data
        :param root: Node object
        """
        if root:
            # traverse to leftmost child
            self.postorder(root.get_left())
            # traverse to rightmost child
            self.postorder(root.get_right())
            # traverse to rightmost child
            self._post_order.append(root.get_data())
        return self._post_order

    def number_of_nodes(self, root):
        """
        counting number of nodes
        """
        # need testing
        left_number = 0;
        right_number = 0;

        #number of nodes left side
        if root.get_left():
            left_number = self.number_of_nodes(root.get_left())

        #numbeof nodes right side
        if root.get_right():
            right_number = self.number_of_nodes(root.get_right())

        return left_number + right_number + 1
    
    @staticmethod
    def get_code():
        """
        returns the code of the current class
        """
        return inspect.getsource(BinaryTree)


class BSTNode(object):
    """
    class for creating a node for binary Search tree
    """
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self._in_order = []
        self._pre_order = []
        self._post_order = []

    def set_left(self, node):
        """
        for setting the left child of the node
        """
        self.left_child = node

    def set_right(self, node):
        """
        for setting the right child of the node
        """
        self.right_child = node

    def get_left(self):
        """
        returns the left child of the current node
        """
        return self.left_child

    def get_right(self):
        """
        returns the right child of the current node
        """
        return self.right_child

    def set_data(self, data):
        """
        for setting the data of a node
        """
        self.data = data

    def get_data(self):
        """
        returns the data of the current node
        """
        return self.data

    def insert(self, data):
        """
        For inserting the data in the Tree
        """
        if self.data == data:
            # As BST cannot contain duplicate data
            return False

        elif data < self.data:
            # Data less than the root data is placed to the left of the root
            if self.left_child:
                return self.left_child.insert(data)
            else:
                self.left_child = BSTNode(data)
                return True

        else:
            # Data greater than the root data is placed to the right of the root
            if self.right_child:
                return self.right_child.insert(data)
            else:
                self.right_child = BSTNode(data)
                return True

    @staticmethod
    def min_val_bst_node(bst_node):
        """
        for returning the node with the lowest value
        """
        current = bst_node

        # loop down to find the leftmost leaf
        while current.left_child is not None:
            current = current.left_child

        return current

    def delete(self, data):
        """
        For deleting the bst_node
        """
        if self is None:
            return None

        # if current bst_node's data is less than that of root bst_node,
        # then only search in left subtree else right subtree
        if data < self.data:
            self.left_child = self.left_child.delete(data)
        elif data > self.data:
            self.right_child = self.right_child.delete(data)
        else:
            # deleting bst_node with one child
            if self.left_child is None:
                temp = self.right_child
                return temp
            elif self.right_child is None:
                temp = self.left_child
                return temp

            # deleting bst_node with two children
            # first get the inorder successor
            temp = self.min_val_bst_node(self.right_child)
            self.data = temp.data
            self.right_child = self.right_child.delete(temp.data)

        return self

    def find(self, data):
        """
        This function checks whether the specified data is in tree or not
        """
        if data == self.data:
            return True
        elif data < self.data:
            if self.left_child:
                return self.left_child.find(data)
            else:
                return False
        else:
            if self.right_child:
                return self.right_child.find(data)
            else:
                return False

    def inorder(self, root):
        """
        in this we first traverse to the leftmost node and
        then print the data and then move to the rightmost child
        :param root: Node object
        """
        if root:
            # traverse to leftmost child
            self.inorder(root.get_left())
            # get the data of current node
            self._in_order.append(root.get_data())
            # traverse to rightmost child
            self.inorder(root.get_right())
        return self._in_order

    def preorder(self, root):
        """
        in this we first print the root node and then
        traverse towards leftmost node and then to the rightmost node
        :param root: Node object
        """
        if root:
            # get the data of current node
            self._pre_order.append(root.get_data())
            # traverse to leftmost child
            self.preorder(root.get_left())
            # traverse to rightmost child
            self.preorder(root.get_right())              
        return self._pre_order

    def postorder(self, root):
        """
        in this we first traverse to the leftmost node
        and then to the rightmost node and then print the data
        :param root: Node object
        """
        if root:
            # traverse to leftmost child
            self.postorder(root.get_left())
            # traverse to rightmost child
            self.postorder(root.get_right())
            # get the data of current node
            self._post_order.append(root.get_data())      
        return self._post_order

    @staticmethod
    def get_code():
        """
        returns the code of current class
        """
        return inspect.getsource(BSTNode)


class BinarySearchTree(object):
   
    def __init__(self):
        self.root = None

    def insert(self, data):
        """
        inserts a node in the tree
        """
        if self.root:
            return self.root.insert(data)
        else:
            self.root = BSTNode(data)
            return True

    def delete(self, data):
        """
        deletes the node with the specified data from the tree
        """
        if self.root is not None:
            return self.root.delete(data)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        """
        finding the preorder of the tree
        """
        if self.root is not None:
            return self.root.preorder(self.root)

    def inorder(self):
        """
        finding the inorder of the tree
        """
        if self.root is not None:
            return self.root.inorder(self.root)

    def postorder(self):
        """
        finding the postorder of the tree
        """
        if self.root is not None:
            return self.root.postorder(self.root)
    
    def number_of_nodes(self, root):
        """
        counting number of nodes
        """
        # need testing
        left_number = 0;
        right_number = 0;

        #number of nodes left side
        if root.get_left():
            left_number = self.number_of_nodes(root.get_left())

        #numbeof nodes right side
        if root.get_right():
            right_number = self.number_of_nodes(root.get_right())

        return left_number + right_number + 1
    
    @staticmethod
    def get_code():
        """
        returns the code of the current class
        """
        return inspect.getsource(BinarySearchTree)
