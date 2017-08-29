"""
Author: OMKAR PATHAK
Created On: 5th August 2017

Linked l_list and Node can be accommodated
in separate classes for convenience
"""
import inspect


class Node(object):
    """
    Node class for creating a node
    for linked list.
    Each node has its data and a pointer that
    points to next node in the Linked l_list
    """
    def __init__(self, data, next_node=None):
        """
        constructor
        :param data:
        :param next_node:
        """
        self.data = data
        self.next = next_node

    @staticmethod
    def get_code():
        """
        return the code for the current class
        """
        return inspect.getsource(Node)


class SinglyLinkedList(object):
    """
    Defining the head of the linked list
    """
    def __init__(self):
        """
        constructor
        """
        self.head = None

    def _search(self, node, data):
        """
        searches the node, if valid returns the node else return false
        """
        if node is None:
            return False
        if node.data == data:
            return node
        return self._search(node.get_next(), data)

    def get_data(self):
        """
        prints the elements in the linked list
        """
        temp = self.head
        l_list = []
        while temp:
            l_list.append(temp.data)
            temp = temp.next

        return l_list

    def insert_at_start(self, data):
        """
        insert an item at the beginning of the linked list
        """
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, next_node_data, data):
        """
        insert an item after an element in the linked list
        """
        new_node = Node(data)
        current_node = self._search(self.head, next_node_data)
        new_node.next = current_node.next
        current_node.next = new_node

    def insert_at_end(self, data):
        """
        insert an item at the end of the linked list
        """
        new_node = Node(data)
        temp = self.head
        # get last node
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def delete(self, data):
        """
        to delete specified element from the linked list
        """
        temp = self.head
        # if data/key is found in head node itself
        if temp is not None:
            if temp.data == data:
                self.head = temp.next
                return
            else:
                # else search all the nodes
                while temp.next is not None:
                    if temp.data == data:
                        break
                    # save current node as previous so that we can go on to next node
                    prev = temp
                    temp = temp.next

                # node not found
                if temp is None:
                    return

                # TODO: local variable 'prev' might be referenced before assignment
                # TODO: Fix this
                prev.next = temp.next
                return

    @staticmethod
    def get_code():
        """
        return the code for the current class
        """
        return inspect.getsource(SinglyLinkedList)


class DoublyLinkedList(object):
    """DoublyLinkedList
    DoublyLinkedList Class
    """
    def __init__(self):
        """
        constructor
        """
        self.head = None

    def get_data(self):
        """
        prints the elements in the linked list
        """
        temp = self.head
        l_list = []
        while temp:
            l_list.append(temp.data)
            temp = temp.next
        return l_list

    def insert_at_start(self, data):
        """
        insert an element at the beginning of the linked list
        """
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        """
        insert an element at the end of the linked list
        """
        new_node = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.previous = temp

    def delete(self, data):
        """
        to delete specified element from the linked list
        """
        temp = self.head
        if temp.next is not None:
            # if head node is to be deleted
            if temp.data == data:
                temp.next.previous = None
                self.head = temp.next
                temp.next = None
                return
            else:
                while temp.next is not None:
                    if temp.data == data:
                        break
                    temp = temp.next
                if temp.next:
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

    @staticmethod
    def get_code():
        """
        returns the code of the current class
        """
        return inspect.getsource(DoublyLinkedList)

class CircularLinkedList(object):
    '''
    Class for circular linked list
    '''
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def clear(self):
        ''' clears the head and tails of the linked list '''
        self.tail = None
        self.head = None

    def get_data(self):
        """
        prints the elements in the linked list
        """
        l_list = []
        current = self.tail
        while True:
            l_list.append(current.data)
            current = current.next
            if current == self.tail:
                break
        return l_list

    def insert(self, data):
        ''' inserts the data in to the linked list '''
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.head.next = self.tail
        self.size += 1

    def delete(self, data):
        ''' deletes the specified element from linked list '''
        current = self.tail
        prev = self.tail
        while prev == current or prev != self.head:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                    self.head.next = self.tail
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

    @staticmethod
    def get_code():
        """
        returns the code of the current class
        """
        return inspect.getsource(CircularLinkedList)

if __name__ == '__main__':
    cll = CircularLinkedList()
    cll.insert(1)
    cll.insert(2)
    cll.insert(3)
    print(cll.get_data())
