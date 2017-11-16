
class QuickFind():

    def __init__(self, num_of_elements):
        self.num_of_elements = num_of_elements
        self.elements = list(range(self.num_of_elements))

    def union(self, a, b):
        a_value = self.elements[a]
        b_value = self.elements[b]

        if a_value == b_value:
            return

        for index, _ in enumerate(self.elements):
            if self.elements[index] == b_value:
                self.elements[index] = a_value

    def connected(self, a, b):
        return self.elements[a] == self.elements[b]

    def __str__(self):
        row_format = "{:>5}" * self.num_of_elements
        indexes = row_format.format("", *range(self.num_of_elements))
        elements = row_format.format("", *self.elements)
        return indexes + "\n" + elements


if __name__ == "__main__":
    obj = QuickFind(10)
    print(obj)
    obj.union(2, 3)
    obj.union(3, 4)
    obj.union(0, 5)
    obj.union(6, 7)
    print(obj)
    obj.union(0, 6)
    print(obj)

    for a, b in [(0, 1), (1, 0), (1, 8), (7, 8), (7, 1), (4, 5)]:
        error = "%s is connected to %s"
        assert not obj.connected(a, b), error % (a, b)
        assert not obj.connected(b, a), error % (b, a)

    for a, b in [(0, 5), (0, 6), (0, 7), (2, 2), (2, 3), (4, 3)]:
        error = "%s is not connected to %s"
        assert obj.connected(a, b), error % (a, b)
        assert obj.connected(b, a), error % (b, a)
