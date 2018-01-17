from collections import Counter


def count_sorting(array):
    """ Suitable for sorting array length of which is far bigger than alphabet
        O(n) = R + N where R - is alphabet N is len of array
        Sort is stable
    """
    count = Counter(array)
    alphabet = sorted(count.keys())

    for letter, next_letter in zip(alphabet, alphabet[1:]):
        count[next_letter] += count[letter]

    previous = 0
    for letter in alphabet:
        previous, count[letter] = count[letter], previous

    aux = array[:]

    for current_letter in aux:
        position = count[current_letter]
        count[current_letter] += 1
        array[position] = current_letter


if __name__ == "__main__":
    from random import randint
    array = [randint(1, 3) for _ in range(10)]
    print(array)
    count_sorting(array)
    print(array)
