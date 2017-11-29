from sort.shuffle import shuffle


def sort_3_way(array):
    shuffle(array)
    sort(array, 0, len(array)-1)


def sort(array, lo, hi):
    if lo >= hi:
        return
    gt = hi
    i = lt = lo
    part_el = array[lo]
    while i <= gt:
        if array[i] < part_el:
            array[lt], array[i] = array[i], array[lt]
            lt += 1
            i += 1
        elif array[i] > part_el:
            array[gt], array[i] = array[i], array[gt]
            gt -= 1
        else:
            i += 1

    sort(array, lo, lt - 1)
    sort(array, gt + 1, hi)
