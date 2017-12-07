import pytest
import random
from itertools import combinations_with_replacement
from trees.heap import MaxHeap, MinHeap


def _heap_sort(array, _class):
    array = list(array)
    sorted_array = array.copy()
    random.shuffle(array)
    heap = _class()
    for item in array:
        heap.insert(item)

    result = list()
    while not heap.is_empty():
        result.append(heap.pop())
    return sorted_array, result


@pytest.mark.parametrize("_class", (MaxHeap, MinHeap))
def test(_class):
    arrays = list(combinations_with_replacement(range(10), 10))
    for array in arrays:
        sorted_array, heap_sorted = _heap_sort(array, _class)
        if _class == MaxHeap:
            heap_sorted.reverse()
        assert sorted_array == heap_sorted
