import random


def shuffle(array):

    for i in range(len(array)):
        index = random.randint(0, i)
        array[i], array[index] = array[index], array[i]
