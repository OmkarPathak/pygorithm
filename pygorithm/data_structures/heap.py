# Author: ALLSTON MICKEY
# Created On: 11th August 2017

from queue import Queue

# min-heap implementation as priority queue
class Heap(Queue):
    def parent_idx(self, idx):
        return idx / 2

    def left_child_idx(self, idx):
        return (idx * 2) + 1

    def right_child_idx(self, idx):
        return (idx * 2) + 2

    def insert(self, data):
        super(Heap, self).enqueue(data)
        if self.rear >= 1:
            self.heapify_up()

    def heapify_up(self):
        """
        Start at the end of the tree (first enqueued item).
        
        Compare the rear item to its parent, swap if
        the parent is larger than the child (min-heap property).
        Repeat until the min-heap property is met.
        """
        child  = self.rear
        parent = self.parent_idx(child)
        while self.queue[child] < self.queue[self.parent_idx(child)]:
            self.queue[child], self.queue[parent] = self.queue[parent], self.queue[child]
            child = parent
            parent = self.parent_idx(child)
