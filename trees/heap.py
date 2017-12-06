class Heap():

    def __init__(self):
        self._nodes = [None]

    def insert(self, value):
        self._nodes.append(value)
        self.swim(len(self._nodes)-1)

    def pop_max(self):
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
        while index > 1 and self._nodes[index] > self._nodes[index//2]:
            self._nodes[index], self._nodes[index//2] = self._nodes[index//2], self._nodes[index]
            index = index // 2

    def sink(self, index):
        if index * 2 > len(self._nodes)-1:
            return
        first_child = index * 2
        second_child = min([first_child + 1, len(self._nodes)-1])
        if self._nodes[first_child] >= self._nodes[second_child]:
            max_child = first_child
        else:
            max_child = second_child

        if self._nodes[index] < self._nodes[max_child]:
            self._nodes[index], self._nodes[max_child] = self._nodes[max_child], self._nodes[index]
            self.sink(max_child)

    def __str__(self):
        return str(self._nodes[1:])
