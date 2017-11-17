class QuickUnion():

    def __init__(self, num_of_elements):
        self.num_of_elements = num_of_elements
        self.elements = list(range(self.num_of_elements))

    def union(self, a, b):
        a_root = self.root(a)
        b_root = self.root(b)

        if a_root == b_root:
            return
        self.elements[a_root] = b_root

    def root(self, a):
        while a != self.elements[a]:
            index = self.elements[a]
            a = self.elements[index]
        return a

    def connected(self, a, b):
        return self.root(a) == self.root(b)

    def __str__(self):
        row_format = "{:5}" * self.num_of_elements
        indexes = row_format.format("", *range(self.num_of_elements))
        elements = row_format.format("", *self.elements)
        return indexes + "\n" + elements
