# 1/2 * N * N --
# 1/2 * N * N -- for partial sorted array
# 1/2 * N * N -- for sorted array
# https://visualgo.net/bn/sorting


def select_sort(array):

    for i in range(len(array)):
        _min = i
        for j in range(i+1, len(array)):
            if array[_min] > array[j]:
                _min = j
        array[i], array[_min] = array[_min], array[i]
