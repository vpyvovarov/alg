# https://alyssaq.github.io/2014/understanding-hough-transform/

import math
from random import randint
import matplotlib.pyplot as plt


def calc_diag(array):
    max_x = array[0][0]
    max_y = array[0][1]

    for element in array:
        if max_x < element[0]:
            max_x = element[0]
        if max_y < element[1]:
            max_y = element[1]

    diag_len = math.ceil(math.sqrt(max_x * max_x + max_x * max_y))
    return diag_len


def hough(array):
    diag_len = calc_diag(array)

    thetas = [degree for degree in range(-90, 90)]
    rhos = [rho for rho in range(-diag_len, diag_len)]

    accumulator = [[0 for _ in range(len(thetas))] for _ in range(len(rhos))]
    for point in array:
        x, y = point
        for t_index, theta in enumerate(thetas):
            rho = round(math.cos(theta) * x + math.sin(theta) * y)
            accumulator[rhos.index(rho)][t_index] += 1

    return accumulator, thetas, rhos


def make_random_points(points_number=10, y_range=(0, 10), x_range=(0, 10)):
    return [(randint(*y_range), randint(*x_range))
            for _ in range(points_number)]


def drow(array, rhos, thetas):
    plt.plot([i[0] for i in array], [i[1] for i in array], 'ro')
    line_y = [i for i in range(len(array))]

    for rho, theta in zip(rhos, thetas):
        line_x = [(rho - y * math.sin(theta)) / math.cos(theta)
                  for y in line_y]
        plt.plot(line_x, line_y, 'b')

    plt.xlabel('x-points')
    plt.ylabel('y-points')
    plt.show()


if __name__ == "__main__":

    array = make_random_points()
    print(array)

    acc, thetas, rhos = hough(array)
    _max = acc[0][0]

    for i in range(len(acc)):
        for j in range(len(acc[i])):
            if acc[i][j] > _max:
                _max = acc[i][j]

    best_suited_rhos = []
    best_suited_thetas = []
    for i in range(len(acc)):
        for j in range(len(acc[i])):
            if acc[i][j] == _max:
                best_suited_rhos.append(rhos[i])
                best_suited_thetas.append(thetas[j])
                print("rho=%s, theta=%s, points = %s"
                      % (rhos[i], thetas[j], _max))

    drow(array, best_suited_rhos, best_suited_thetas)
