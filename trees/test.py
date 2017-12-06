import random
from itertools import combinations_with_replacement
from trees.heap import Heap


def test():
    arrays = list(combinations_with_replacement(range(10), 10))
    for array in arrays:
        array = list(array)
        sorted_array = array.copy()
        random.shuffle(array)
        heap = Heap()
        for item in array:
            heap.insert(item)

        result = list()
        while not heap.is_empty():
            result.append(heap.pop_max())
        result.reverse()
        assert sorted_array == result
