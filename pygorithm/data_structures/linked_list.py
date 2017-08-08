# Author: OMKAR PATHAK
# Created On: 5th August July 2017

# Linked List and Node can be accomodated in separate classes for convenience

class Node(object):
    # Each node has its data and a pointer that points to next node in the Linked List
    def __init__(self, data, next = None):
        self.data = data;
        self.next = next;

    # function to set data
    def setData(self, data):
        self.data = data;

    # function to get data of a particular node
    def getData(self):
        return self.data

    # function to set next node
    def setNext(self, next):
        self.next = next

    # function to get the next node
    def getNext(self):
        return self.next

    # easily retrieve the source code of the Node class
    def get_code(self):
        import inspect
        return inspect.getsource(Node)

class SinglyLinkedList(object):
    # Defining the head of the linked list
    def __init__(self):
        self.head = None

    # printing the data in the linked list
    def get_data(self):
        temp = self.head
        List = []
        while(temp):
            # print(temp.data, end=' ')
            List.append(temp.data)
            temp = temp.next

        return List

    # inserting the node at the beginning
    def insert_at_start(self, data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    # inserting the node in between the linked list (after a specific node)
    def insert_between(self, next_node_data, data):
        # if (previousNode.next is None):
        #     print('Previous node should have next node!')
        # else:
        newNode = Node(data)
        currentNode = self.search(self.head, next_node_data)
        newNode.next = currentNode.next
        currentNode.next = newNode

    # inserting at the end of linked list
    def insert_at_end(self, data):
        newNode = Node(data)
        temp = self.head
        while(temp.next != None):         # get last node
            temp = temp.next
        temp.next = newNode

    # deleting an item based on data(or key)
    def delete(self, data):
        temp = self.head
        # if data/key is found in head node itself
        if (temp.next is not None):
            if(temp.data == data):
                self.head = temp.next
                temp = None
                return
            else:
                #  else search all the nodes
                while(temp.next != None):
                    if(temp.data == data):
                        break
                    prev = temp          #save current node as previous so that we can go on to next node
                    temp = temp.next

                # node not found
                if temp == None:
                    return

                prev.next = temp.next
                return

    # iterative search
    def search(self, node, data):
        if node == None:
            return False
        if node.data == data:
            return node
        return self.search(node.getNext(), data)

    # easily retrieve the source code of the SinglyLinkedList class
    def get_code(self):
        import inspect
        return inspect.getsource(SinglyLinkedList)

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None

    # printing the data in the linked list
    def get_data(self):
        temp = self.head
        List = []
        while(temp):
            # print(temp.data, end=' ')
            List.append(temp.data)
            temp = temp.next

        return List

    # for inserting at beginning of linked list
    def insert_at_start(self, data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            self.head.previous = newNode
            newNode.next = self.head
            self.head = newNode

    # for inserting at end of linked list
    def insert_at_end(self, data):
        newNode = Node(data)
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = newNode
        newNode.previous = temp

    # deleting a node from linked list
    def delete(self, data):
        temp = self.head
        if(temp.next != None):
            # if head node is to be deleted
            if(temp.data == data):
                temp.next.previous = None
                self.head = temp.next
                temp.next = None
                return
            else:
                while(temp.next != None):
                    if(temp.data == data):
                        break
                    temp = temp.next
                if(temp.next):
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

        if (temp == None):
            return

    # easily retrieve the source code of the DoublyLinkedList class
    def get_code(self):
        import inspect
        return inspect.getsource(DoublyLinkedList)
