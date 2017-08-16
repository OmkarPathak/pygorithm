# Author: OMKAR PATHAK
# Created On: 5th August 2017

# Linked List and Node can be accomodated in separate classes for convenience

class Node(object):
    ''' Node class for creating a node for linked list.
        Each node has its data and a pointer that points to next node in the Linked List
    '''
    def __init__(self, data, next=None):
        ''' constructor '''
        self.data = data
        self.next = next

    # easily retrieve the source code of the Node class
    @classmethod
    def get_code(cls):
        ''' return the code for the current class '''
        import inspect
        return inspect.getsource(cls)


class SinglyLinkedList(object):
    # Defining the head of the linked list
    def __init__(self):
        ''' constructor '''
        self.head = None

    def _search(self, node, data):
        ''' searches the node, if valid returns the node else return false '''
        if node == None:
            return False
        if node.data == data:
            return node
        return self._search(node.get_next(), data)

    def get_data(self):
        ''' prints the elements in the linked list '''
        temp = self.head
        List = []
        while (temp):
            # print(temp.data, end=' ')
            List.append(temp.data)
            temp = temp.next

        return List

    def insert_at_start(self, data):
        ''' insert an item at the beginning of the linked list '''
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    def insert_after(self, next_node_data, data):
        ''' insert an item after an element in the linked list '''
        newNode = Node(data)
        currentNode = self._search(self.head, next_node_data)
        newNode.next = currentNode.next
        currentNode.next = newNode

    def insert_at_end(self, data):
        ''' insert an item at the end of the linked list '''
        newNode = Node(data)
        temp = self.head
        while (temp.next != None):  # get last node
            temp = temp.next
        temp.next = newNode

    def delete(self, data):
        ''' to delete specified element from the linked list '''
        temp = self.head
        # if data/key is found in head node itself
        if temp is not None:
            if temp.data == data:
                self.head = temp.next
                temp = None
                return
            else:
                #  else _search all the nodes
                while (temp.next != None):
                    if (temp.data == data):
                        break
                    prev = temp  # save current node as previous so that we can go on to next node
                    temp = temp.next

                # node not found
                if temp == None:
                    return

                prev.next = temp.next
                return

    # easily retrieve the source code of the SinglyLinkedList class
    @staticmethod
    def get_code():
        ''' return the code for the current class '''
        import inspect
        return inspect.getsource(SinglyLinkedList)


class DoublyLinkedList(object):
    def __init__(self):
        ''' constructor '''
        self.head = None

    def get_data(self):
        ''' prints the elements in the linked list '''
        temp = self.head
        List = []
        while (temp):
            # print(temp.data, end=' ')
            List.append(temp.data)
            temp = temp.next

        return List

    def insert_at_start(self, data):
        ''' insert an element at the beginning of the linked list '''
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            self.head.previous = newNode
            newNode.next = self.head
            self.head = newNode

    def insert_at_end(self, data):
        ''' insert an element at the end of the linked list '''
        newNode = Node(data)
        temp = self.head
        while (temp.next != None):
            temp = temp.next
        temp.next = newNode
        newNode.previous = temp

    def delete(self, data):
        ''' to delete specified element from the linked list '''
        temp = self.head
        if (temp.next != None):
            # if head node is to be deleted
            if (temp.data == data):
                temp.next.previous = None
                self.head = temp.next
                temp.next = None
                return
            else:
                while (temp.next != None):
                    if (temp.data == data):
                        break
                    temp = temp.next
                if (temp.next):
                    # if element to be deleted is in between
                    temp.previous.next = temp.next
                    temp.next.previous = temp.previous
                    temp.next = None
                    temp.previous = None
                else:
                    # if element to be deleted is the last element
                    temp.previous.next = None
                    temp.previous = None
                return

        if temp is None:
            return

    # easily retrieve the source code of the DoublyLinkedList class
    @staticmethod
    def get_code():
        ''' returns the code of the current class '''
        import inspect
        return inspect.getsource(DoublyLinkedList)
