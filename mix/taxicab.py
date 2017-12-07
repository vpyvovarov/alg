from trees.heap import MinHeap


def cube_sum_generator():

    heap = MinHeap()
    base = 1

    while True:

        while heap.is_empty() or heap.top()[0] > base ** 3:
            heap.insert((base ** 3 + 1, base, 1))
            base += 1

        _sum, x, y = heap.pop()
        yield _sum, x, y
        y += 1
        if y < x:
            heap.insert((x ** 3 + y ** 3, x, y))


def get_taxicab_numbers_gen():
    previous = [None]
    for item in cube_sum_generator():
        if previous[0] == item[0]:
            yield item, previous
        previous = item


if __name__ == "__main__":
    expected = [((1729, 12, 1), (1729, 10, 9)),
                ((4104, 16, 2), (4104, 15, 9)),
                ((13832, 24, 2), (13832, 20, 18)),
                ((20683, 27, 10), (20683, 24, 19)),
                ((32832, 32, 4), (32832, 30, 18)),
                ((39312, 34, 2), (39312, 33, 15)),
                ((40033, 34, 9), (40033, 33, 16)),
                ((46683, 36, 3), (46683, 30, 27)),
                ((64232, 39, 17), (64232, 36, 26)),
                ((65728, 40, 12), (65728, 33, 31))]
    taxicab = []
    for index, values in enumerate(get_taxicab_numbers_gen()):
        if index > len(expected)-1:
            break
        taxicab.append(values)
    assert taxicab == expected
