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
        if self.rear >= 1: # heap may need to be fixed
            self.heapify_up()

    def heapify_up(self):
        '''
        Start at the end of the tree (first enqueued item).
        
        Compare the rear item to its parent, swap if
        the parent is larger than the child (min-heap property).
        Repeat until the min-heap property is met.
        '''
        child  = self.rear
        parent = self.parent_idx(child)
        while self.queue[child] < self.queue[self.parent_idx(child)]:
            # Swap (sift up) and update child:parent relation
            self.queue[child], self.queue[parent] = self.queue[parent], self.queue[child]
            child = parent
            parent = self.parent_idx(child)

    def pop(self):
        ''' Removes the lowest value element (highest priority) from the heap '''
        min = self.dequeue()
        if self.rear >= 1: # heap may need to be fixed
            self.heapify_down()
        return min

    def favorite(self, parent):
        ''' Determines which child has the highest priority by 3 cases '''
        left  = self.left_child_idx(parent)
        right = self.right_child_idx(parent)
        
        if left <= self.rear and right <= self.rear: # case 1: both nodes exist
            if self.queue[left] <= self.queue[right]:
                return left
            else:
                return right
        elif left <= self.rear: # case 2: only left exists
            return left
        else: # case 3: no children (if left doesn't exist, neither can the right)
            return None
        
    def heapify_down(self):
        '''
        Select the root and sift down until min-heap property is met.

        While a favorite child exists, and that child is smaller
        than the parent, swap them (sift down).
        '''
        cur = ROOT = 0 # start at the root
        fav = self.favorite(cur) # determine favorite child
        while self.queue[fav] is not None:
            if self.queue[cur] > self.queue[fav]:
                # Swap (sift down) and update parent:favorite relation
                fav = self.favorite(cur)
                self.queue[cur], self.queue[fav] = self.queue[fav], self.queue[cur]
                cur = fav
            else:
                return

    def get_code(self):
        import inspect
        return inspect.getsource(Heap)

