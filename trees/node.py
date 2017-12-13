from functools import total_ordering


@total_ordering
class Node():

    def __init__(self, key, value, left=None, right=None, size=1):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.size = size

    def __eq__(self, other):
        other_key = other
        if issubclass(type(other), self.__class__):
            other_key = other.key
        return self.key == other_key

    def __lt__(self, other):
        other_key = other
        if issubclass(type(other), self.__class__):
            other_key = other.key
        return self.key < other_key


if __name__ == "__main__":
    assert not Node(1, 2) == Node(2, 1)
    assert Node(1, 2) != Node(2, 1)
    assert not Node(1, 2) > Node(2, 1)
    assert Node(1, 2) < Node(2, 1)
    assert not Node(1, 2) >= Node(2, 1)
    assert Node(1, 2) <= Node(2, 1)
    assert Node(2, 2) == Node(2, 2)
    assert Node(2, 2) >= Node(2, 2)
    assert Node(2, 2) == Node(2, 2)
    assert Node(2, 2) == 2
    assert not "B" > Node("C", 2)
