from sort.shuffle import shuffle


def quick_sort(array):
    shuffle(array)
    sort(array, 0, len(array)-1)


def sort(array, lo, hi):
    if lo >= hi:
        return
    j = partitioning(array, lo, hi)
    sort(array, lo, j-1)
    sort(array, j+1, hi)


def partitioning(array, lo, hi):
    k = lo
    lo += 1
    while True:
        while lo <= hi and array[lo] <= array[k]:
            lo += 1
        while hi >= lo and array[hi] >= array[k]:
            hi -= 1

        if lo >= hi:
            break

        array[hi], array[lo] = array[lo], array[hi]

    array[k], array[hi] = array[hi], array[k]
    return hi
