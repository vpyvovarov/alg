import pytest
import random
from itertools import combinations_with_replacement
from collections import Counter
from sort.select_sort import select_sort
from sort.insertion_sort import insertion_sort
from sort.shell_sort import shell_sort
from sort.shuffle import shuffle
from sort.merge_sort import merge_sort, merge_sort_recursive
from sort.quick_sort import quick_sort
from sort.sort_3_way import sort_3_way


@pytest.mark.parametrize("sorting_function",
                         (select_sort,
                          insertion_sort,
                          shell_sort, merge_sort,
                          merge_sort_recursive,
                          quick_sort,
                          sort_3_way))
def test(sorting_function):
    arrays = list(combinations_with_replacement(range(10), 10))
    for array in arrays:
        array = list(array)
        random.shuffle(array)
        sorting_function(array)
        assert all(array[i] <= array[i+1] for i in range(len(array)-1)), array


def test_shuffle_randomnes():
    list_size = 10
    num_of_iteratons = 100000
    expected_probability = 1/10
    allowed_deviation = 0.005
    array = list(range(list_size))
    counters = [Counter() for _ in range(list_size)]
    for _ in range(num_of_iteratons):
        shuffle(array)
        for counter, element in zip(counters, array):
            counter[element] += 1

    for c in counters:
        for element, count in c.items():
            current_probability = count / num_of_iteratons
            current_deviation = abs(current_probability - expected_probability)
            assert current_deviation < allowed_deviation, \
            "Element %s distibution is wrong. Expeted %s, got %s" % (element, current_probability, expected_probability) # noqa
