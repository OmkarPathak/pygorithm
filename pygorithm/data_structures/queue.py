"""
Author: OMKAR PATHAK
Created On: 3rd August 2017
"""
import inspect


class Queue(object):
    """Queue
    Queue implementation
    """
    def __init__(self, limit=10):
        """
        :param limit: Queue limit size, default @ 10
        """
        self.queue = []
        self.front = None
        self.rear = None
        self.limit = limit
        self.size = 0

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def size(self):
        """
        returns the current size of the queue
        """
        return self.size

    def is_empty(self):
        """
        checks if the queue is empty
        """
        return self.size <= 0

    def enqueue(self, data):
        """
        inserts an item into the queue
        """
        if self.size >= self.limit:
            # queue overflow
            return -1
        else:
            self.queue.append(data)

        # assign the rear as size of the queue and front as 0
        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size

        self.size += 1

    def dequeue(self):
        """
        pops an item from the queue which was first inserted
        """
        if self.is_empty():
            # queue underflow
            return -1
        else:
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = 0
            else:
                self.rear = self.size - 1
            return self.queue.pop(0)

    def get_code(self):
        """
        Return source code for Queue class
        :return:
        """
        return inspect.getsource(Queue)


class Deque(object):
    """Deque
    Deque implementation
    """
    def __init__(self, limit=10):
        self.queue = []
        self.limit = limit

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def is_empty(self):
        """
        checks whether the deque is empty
        """
        return len(self.queue) <= 0

    def is_full(self):
        """
        checks whether the deque is full
        """
        return len(self.queue) >= self.limit

    def insert_rear(self, data):
        """
        inserts an element at the rear end of the deque
        """
        if self.is_full():
            return
        else:
            self.queue.insert(0, data)

    def insert_front(self, data):
        """
        inserts an element at the front end of the deque
        """
        if self.is_full():
            return -1
        else:
            self.queue.append(data)

    def delete_rear(self):
        """
        deletes an element from the rear end of the deque
        """
        if self.is_empty():
            return -1
        else:
            return self.queue.pop(0)

    def delete_front(self):
        """
        deletes an element from the front end of the deque
        """
        if self.is_full():
            return
        else:
            return self.queue.pop()

    @staticmethod
    def get_code():
        """
        returns the code of the current class
        """
        return inspect.getsource(Deque)
