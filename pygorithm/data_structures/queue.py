# Author: OMKAR PATHAK
# Created On: 3rd August 2017

# queue implementation
class Queue(object):
    '''

    size    : return the current size of the queue
    enqueue : insert an item into the queue
    dequeue : remove an item from the queue which was first inserted
    isEmpty : check if the queue is empty

    '''

    def __init__(self, limit = 10):
        '''
        @param: limit: queue size
        '''
        self.queue = []
        self.front = None
        self.rear = None
        self.limit = limit
        self.size = 0

    # for printing the contents of the queue
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # to check if queue is empty
    def isEmpty(self):
        return self.size <= 0

    # to add an element from the rear end of the queue
    def enqueue(self, data):
        if self.size >= self.limit:
            return -1          # queue overflow
        else:
            self.queue.append(data)

        # assign the rear as size of the queue and front as 0
        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size

        self.size += 1

    # to pop an element from the front end of the queue
    def dequeue(self):
        if self.isEmpty():
            return -1          # queue underflow
        else:
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = 0
            else:
                self.rear = self.size - 1
            return self.queue.pop(0)

    # return the size of the queue
    def size(self):
        return self.size

    # easily retrieve the source code of the Queue class
    def get_code(self):
        import inspect
        return inspect.getsource(Queue)

class Deque(object):
    '''

    isEmpty     : checks whether the deque is empty
    isFull      : checks whether the deque is full
    insertRear  : inserts an element at the rear end of the deque
    insertFront : inserts an element at the front end of the deque
    deleteRear  : deletes an element from the rear end of the deque
    deleteFront : deletes an element from the front end of the deque

    '''

    def __init__(self, limit = 10):
        self.queue = []
        self.limit = limit

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # check if queue is empty
    def isEmpty(self):
        return len(self.queue) <= 0

    # check if queue is full
    def isFull(self):
        return len(self.queue) >= self.limit

    # for inserting at rear
    def insertRear(self, data):
        if self.isFull():
            return
        else:
            self.queue.insert(0, data)

    # for inserting at front end
    def insertFront(self, data):
        if self.isFull():
            return
        else:
            self.queue.append(data)

    # deleting from rear end
    def deleteRear(self):
        if self.isEmpty():
            return
        else:
            return self.queue.pop(0)

    # deleting from front end
    def deleteFront(self):
        if self.isFull():
            return
        else:
            return self.queue.pop()
