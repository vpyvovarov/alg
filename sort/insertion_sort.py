# 1/4 * N * N --
# 1/2 * N * N -- worth case. Array is sorted in reverse order
# N - best case. Already sorted
# ~N - for partial sorted array
# https://visualgo.net/bn/sorting


def insertion_sort(array):
    array_len = len(array)
    for i in range(1, array_len):
        j = i
        while array[j] < array[j-1] and j > 0:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1


if __name__ == "__main__":
    array = [2, 3, 4, 9, 1, 5, 5, 3, 8]
    insertion_sort(array)
    print(array)
