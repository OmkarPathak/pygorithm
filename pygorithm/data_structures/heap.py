"""
Author: ALLSTON MICKEY
Contributed: OMKAR PATHAK
Created On: 11th August 2017
"""
from __future__ import division
from pygorithm.data_structures import queue
import inspect


class Heap(queue.Queue):
    """
    min-heap implementation as queue
    """

    @staticmethod
    def parent_idx(idx):
        """
        retrieve the parent
        """
        return idx // 2

    @staticmethod
    def left_child_idx(idx):
        """
        retrieve the left child
        """
        return (idx * 2) + 1

    @staticmethod
    def right_child_idx(idx):
        """
        retrieve the right child
        """
        return (idx * 2) + 2

    def insert(self, data):
        """
        inserting an element in the heap
        """
        # TODO: Fix this if we want this compatible with 2.7
        super().enqueue(data)
        if self.rear >= 1:  # heap may need to be fixed
            self.heapify_up()

    def heapify_up(self):
        """
        Start at the end of the tree (last enqueued item).

        Compare the rear item to its parent, swap if
        the parent is larger than the child (min-heap property).
        Repeat until the min-heap property is met.

        Best Case:   O(1), item is inserted at correct position, no swaps needed
        Worst Case:  O(log n), item needs to be swapped throughout all levels of tree
        """
        child = self.rear
        parent = self.parent_idx(child)
        while self.queue[child] < self.queue[self.parent_idx(child)]:
            # Swap (sift up) and update child:parent relation
            self.queue[child], self.queue[parent] = self.queue[parent], self.queue[child]
            child = parent
            parent = self.parent_idx(child)

    def pop(self):
        """
        Removes the lowest value element (highest priority, at root) from the heap
        """
        min = super().dequeue()
        if self.rear >= 1:  # heap may need to be fixed
            self.heapify_down()
        return min

    def favorite(self, parent):
        """
        Determines which child has the highest priority by 3 cases
        """
        left = self.left_child_idx(parent)
        right = self.right_child_idx(parent)

        # case 1: both nodes exist
        if left <= self.rear and right <= self.rear:
            if self.queue[left] <= self.queue[right]:
                return left
            else:
                return right
        # case 2: only left exists
        elif left <= self.rear:
            return left
        # case 3: no children (if left doesn't exist, neither can the right)
        else:
            return None

    def heapify_down(self):
        """
        Select the root and sift down until min-heap property is met.

        While a favorite child exists, and that child is smaller
        than the parent, swap them (sift down).

        Best Case:   O(1), item is inserted at correct position, no swaps needed
        Worst Case:  O(logn), item needs to be swapped throughout all levels of tree
        """
        cur = 0  # start at the root
        fav = self.favorite(cur)  # determine favorite child
        while self.queue[fav] is not None:
            if self.queue[cur] > self.queue[fav]:
                # Swap (sift down) and update parent:favorite relation
                fav = self.favorite(cur)
                self.queue[cur], self.queue[fav] = self.queue[fav], self.queue[cur]
                cur = fav
            else:
                return

    # TODO: Is this necessary?
    @staticmethod
    def time_complexities():
        return "[Insert & Pop] Best Case: O(1), Worst Case: O(logn)"

    def get_code(self):
        """
        returns the code for the current class
        """
        return inspect.getsource(Heap)
