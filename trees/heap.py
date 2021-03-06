class Heap():

    def __init__(self):
        self._nodes = [None]

    def insert(self, value):
        self._nodes.append(value)
        self.swim(len(self._nodes)-1)

    def pop(self):
        if self.is_empty():
            return
        return_value = self._nodes[1]
        new_root = self._nodes.pop()
        if not self.is_empty():
            self._nodes[1] = new_root
            self.sink(1)
        return return_value

    def is_empty(self):
        return len(self._nodes) <= 1

    def swim(self, index):
        while index > 1 and self.compare(self._nodes[index],
                                         self._nodes[index//2]):
            self._nodes[index], self._nodes[index//2] = self._nodes[index//2], self._nodes[index]
            index = index // 2

    def sink(self, index):
        if index * 2 > len(self._nodes)-1:
            return
        first_child = index * 2
        second_child = min([first_child + 1, len(self._nodes)-1])
        if self.compare(self._nodes[first_child],
                        self._nodes[second_child]):
            max_child = first_child
        else:
            max_child = second_child

        if self.compare(self._nodes[max_child], self._nodes[index]):
            self._nodes[index], self._nodes[max_child] = self._nodes[max_child], self._nodes[index]
            self.sink(max_child)

    def compare(self, a, b):
        raise NotImplementedError()

    def __str__(self):
        return str(self._nodes[1:])

    def top(self):
        return self._nodes[1]

    def size(self):
        return len(self._nodes) - 1


class MutableHeap(Heap):

    def contains(self, key):
        return key in self._nodes

    def change(self, key, new_value):
        index = self._nodes.index(key)
        if index:
            self._nodes[index] = new_value
            self.swim(index)
            self.sink(index)


class MaxHeap(Heap):

    def compare(self, a, b):
        return a > b


class MinHeap(Heap):

    def compare(self, a, b):
        return a < b
