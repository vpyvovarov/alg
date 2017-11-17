import pytest
from itertools import combinations_with_replacement
from sort.select_sort import select_sort


@pytest.mark.parametrize("sorting_function", (select_sort,))
def test(sorting_function):
    arrays = list(combinations_with_replacement(range(10), 10))
    for array in arrays:
        sorting_function(list(array))
        assert all(array[i] <= array[i+1] for i in range(len(array)-1))
