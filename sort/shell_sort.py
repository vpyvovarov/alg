# N ** 3/2 -- worst case
# Mostly performance is much better. Performance measure is still open problem
# Open problem is also optimal h-sorting sequensce
# https://visualgo.net/bn/sorting


def shell_sort(array):
    array_len = len(array)

    for h in h_sequence(array_len):
        for i in range(array_len):
            j = i
            while array[j] < array[j-h] and j > 0:
                array[j], array[j-h] = array[j-h], array[j]
                j -= h


def h_formula(x):
    return 3 * x + 1


def h_sequence(array_size):
    h = 1
    values = []
    while h < array_size / 2:
        values.append(h)
        h = h_formula(h)

    for h in reversed(values):
        yield h
