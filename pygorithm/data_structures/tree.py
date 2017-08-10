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
            self._inorder.append(root.get_data())    # get the data of current node
            self.inorder(root.get_right())               # traverse to rightmost child
        return self._inorder

    # in this we first print the root node and then traverse towards leftmost node and then to the rightmost node
    def preorder(self, root):
        '''
        @type: root:   Node object
        '''
        if root:
            self._preorder.append(root.get_data())   # get the data of current node
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
            self._postorder.append(root.get_data())  # get the data of current node
        return self._postorder

    # easily retrieve the source code of the BinaryTree class
    def get_code(self):
        import inspect
        return inspect.getsource(BinaryTree)
