# N * log N
# sorted array and partially sorted array the same performance
# https://visualgo.net/bn/sorting


def merge_sort(array):
    step_size = 1
    array_size = len(array)
    while step_size <= array_size:
        j = 0
        while array_size - step_size >= j:
            merge(array, j, j + step_size - 1,
                  min(j + 2 * step_size - 1, array_size - 1))
            j += 2 * step_size
        step_size += step_size


def merge_sort_recursive(array):
    sort(array, 0, len(array)-1)


def sort(array, first, last):
    if last <= first:
        return
    mid = first + (last-first) // 2
    sort(array, first, mid)
    sort(array, mid+1, last)
    merge(array, first, mid, last)


def merge(array, first, mid, last):
    aux = array.copy()
    i = first
    j = mid + 1
    for k in range(first, last+1):
        if i > mid:
            array[k] = aux[j]
            j += 1
        elif j > last:
            array[k] = aux[i]
            i += 1
        elif aux[i] > aux[j]:
            array[k] = aux[j]
            j += 1
        else:
            array[k] = aux[i]
            i += 1
