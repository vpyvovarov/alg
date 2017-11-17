def select_sort(array):

    for i in range(len(array)):
        _min = i
        for j in range(i+1):
            if array[_min] > array[j]:
                _min = j
        array[i], array[_min] = array[_min], array[i]
