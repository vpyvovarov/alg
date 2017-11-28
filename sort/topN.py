from quick_sort import partitioning, quick_sort


def topk(array, k):
    hi = len(array) - 1
    lo = 0
    while hi > lo:
        j = partitioning(a, lo, hi)
        if j > k:
            hi = j - 1
        elif j < k:
            lo = j + 1
        else:
            break
    return array[k]


if __name__ == "__main__":
    a = [3, 5, 4, 3, 2, 9, 7, 8, 1]
    k = 2
    print(a)
    k_number = topk(a, k)
    quick_sort(a)
    print(a)
    print("correct answer is %s, got %s" % (a[k], k_number))
