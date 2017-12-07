from heap import MinHeap, MaxHeap
from sys import maxsize


class MedianHeap():

    def __init__(self):
        self._left_heap = MaxHeap()
        self._right_heap = MinHeap()

    def insert(self, value):
        right_top = maxsize
        if not self._right_heap.is_empty():
            right_top = self._right_heap.top()

        if value < right_top:
            self._left_heap.insert(value)
        else:
            self._right_heap.insert(value)

        self.balance()

    def balance(self):
        left_size = self._left_heap.size()
        right_size = self._right_heap.size()

        if abs(left_size - right_size) <= 1:
            return
        if left_size > right_size:
            poped = self._left_heap.pop()
            self._right_heap.insert(poped)
        else:
            poped = self._right_heap.pop()
            self._left_heap.insert(poped)
        self.balance()

    def median(self):
        left_size = self._left_heap.size()
        right_size = self._right_heap.size()
        if left_size > right_size:
            _median = self._left_heap.top()
        else:
            _median = self._right_heap.top()
        return _median

    def pop_median(self):
        left_size = self._left_heap.size()
        right_size = self._right_heap.size()
        if left_size > right_size:
            _median = self._left_heap.pop()
        else:
            _median = self._right_heap.pop()
        self.balance()
        return _median

    def is_empty(self):
        return self._left_heap.is_empty() and self._right_heap.is_empty()

    def __str__(self):
        return "left: %s. right: %s." % (self._left_heap, self._right_heap)


if __name__ == "__main__":
    h = MedianHeap()
    a = [2, 4, 6, 8, 2, 8, 3, 1, 9]
    for value in a:
        h.insert(value)

    print(h)

    while not h.is_empty():
        print(h.pop_median())
        print(h)
