from random import randint
import matplotlib.pyplot as plt
from collections import defaultdict
from sys import maxsize


def make_random_points(points_number=10, y_range=(0, 10), x_range=(0, 10)):
    result = []
    while len(result) < points_number:
        point = (randint(*y_range), randint(*x_range))
        if point not in result:
            result.append(point)
    return result


def find_lines(array):
    result = []

    for root_index, root_point in enumerate(array[:-1]):

        slope_dict = defaultdict(lambda: [root_point])

        for index, point in enumerate(array[root_index+1:]):

            if (root_point[1] - point[1]) != 0:
                slope = (root_point[0] - point[0]) / (root_point[1] - point[1])
            else:
                slope = maxsize

            slope_dict[slope].append(point)

        for key, values in slope_dict.items():

            if len(values) > 2:
                points = set(values)

                # verify if this is not subline of longer line
                flag = True
                for found_points in result:
                    if points.issubset(found_points):
                        flag = False
                if flag:
                    result.append(points)

    return result


def drow(array, colinear_points):
    plt.plot([i[0] for i in array], [i[1] for i in array], 'ro')
    for points in colinear_points:
        x = [i[0] for i in points]
        y = [i[1] for i in points]
        plt.plot(x, y)

    plt.xlabel('x-points')
    plt.ylabel('y-points')
    plt.show()


if __name__ == "__main__":
    array = make_random_points()
    print(array)
    colinear_points = find_lines(array)
    print(colinear_points)
    drow(array, colinear_points)
