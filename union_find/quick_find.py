
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
