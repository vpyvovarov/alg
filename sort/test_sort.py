import pytest
import random
from itertools import combinations_with_replacement
from sort.select_sort import select_sort
from sort.insertion_sort import insertion_sort
from sort.shell_sort import shell_sort


@pytest.mark.parametrize("sorting_function",
                         (select_sort, insertion_sort, shell_sort))
def test(sorting_function):
    arrays = list(combinations_with_replacement(range(10), 10))
    for array in arrays:
        array = list(array)
        random.shuffle(array)
        sorting_function(array)
        assert all(array[i] <= array[i+1] for i in range(len(array)-1)), array
