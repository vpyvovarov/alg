class Heap():

    def __init__(self):
        self._nodes = []
    
    def insert(self, value):
        print("insert value: %s" % value)
        self._nodes.append(value)
        self.swim(len(self._nodes)-1)
    
    def pop_max(self):
        return_value = self._nodes[0]
        self._nodes[0] = self._nodes.pop()
        self.sink(0)
        return return_value

    def is_empty(self):
        return bool(len(self._nodes))
    
    def swim(self, index):
        # import pdb; pdb.set_trace()
        if self._nodes[index] > self._nodes[index//2]:
            self._nodes[index], self._nodes[index//2] = self._nodes[index//2], self._nodes[index]
            self.swim(index//2)
    
    def sink(self, index):
        first_children_index = min([index * 2, len(self._nodes)-1])
        second_children_index = min([first_children_index + 1, len(self._nodes)-1])
        max_children_index = first_children_index if self._nodes[first_children_index] >= self._nodes[second_children_index] else second_children_index

        if self._nodes[index] < self._nodes[max_children_index]:
            self._nodes[index], self._nodes[max_children_index] = self._nodes[max_children_index], self._nodes[index]
            self.sink(max_children_index)
    
    def __str__(self):
        return str(self._nodes)

if __name__ == "__main__":
    h = Heap()
    a = [2, 4, 6, 8, 2, 8, 3, 1, 9]
    for value in a:
        h.insert(value)
    
    print(h)
    while h.is_empty():
        print(h.pop_max())
