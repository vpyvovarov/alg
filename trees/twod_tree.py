import pydot
from math import sqrt
import matplotlib.pyplot as plt
from uuid import uuid4


VERTICAL = True
HORISONTAL = False


class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def left(self, other):
        return self.x <= other.x

    def right(self, other):
        return self.x >= other.x

    def below(self, other):
        return self.y <= other.y

    def above(self, other):
        return self.y >= other.y

    def distance(self, other):
        return sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2))

    def __str__(self):
        return "x=%s, y=%s" % (self.x, self.y)


class Rectangle():

    def __init__(self, lower_left_point, upper_right_point):
        self.first_point = lower_left_point
        self.second_point = upper_right_point

    def point_is_on_left(self, point):
        return self.first_point.left(point) and self.second_point.left(point)

    def point_is_on_right(self, point):
        return self.first_point.right(point) and self.second_point.right(point)

    def point_is_above(self, point):
        return point.above(self.first_point) and point.above(self.second_point)

    def point_is_below(self, point):
        return point.below(self.first_point) and point.below(self.second_point)

    def orthogonal_cross(self, point, direction):
        """ Verify if there is orthogonal from `point` to this rectangle.
            If `direction` is VERTICAL than orthogonal should be
            parallel to y-coordinat
            If `direction` is HORISONTAL than orthogonal should be
            parallel to x-coordinat
        """
        if direction is VERTICAL:
            return self.verical_cross(point)
        else:
            return self.horisontal_cross(point)

    def verical_cross(self, point):
        max_x = max([self.first_point.x, self.second_point.x])
        min_x = min([self.first_point.x, self.second_point.x])
        return max_x > point.x > min_x

    def horisontal_cross(self, point):
        max_y = max([self.first_point.y, self.second_point.y])
        min_y = min([self.first_point.y, self.second_point.y])
        return max_y > point.y > min_y

    def inside_rect(self, point):
        return self.first_point.x <= point.x <= self.second_point.x and \
               self.first_point.y <= point.y <= self.second_point.y

    def get_clockwize_points(self):
        """ Generate all point for this rectangle"""
        return [Point(self.first_point.x, self.first_point.y),
                Point(self.first_point.x, self.second_point.y),
                Point(self.second_point.x, self.second_point.y),
                Point(self.second_point.x, self.first_point.y)]


class PointNode():
    """ Node for tree"""
    def __init__(self, point, direction, left=None, right=None):
        self.direction = direction
        self.point = point
        self.left = left
        self.right = right


class TwoDTree():
    """2D tree"""

    def __init__(self):
        self.root = None

    def insert(self, point):
        self.root = self._insert(point, self.root)

    def _insert(self, point, root, direction=VERTICAL):
        if root is None:
            return PointNode(point, direction=direction)
        if root.direction == VERTICAL:
            if point.left(root.point):
                root.left = self._insert(point, root.left,
                                         direction=not(root.direction))
            if point.right(root.point):
                root.right = self._insert(point, root.right,
                                          direction=not(root.direction))
        else:
            if point.above(root.point):
                root.right = self._insert(point, root.right,
                                          direction=not(root.direction))
            if point.below(root.point):
                root.left = self._insert(point, root.left,
                                         direction=not(root.direction))
        return root

    def range_search(self, rect_point_one, rect_point_two):
        """Return all points that are inside rectangle"""
        result = []
        rectangle = Rectangle(rect_point_one, rect_point_two)
        self._range_search(self.root, rectangle, result)
        return result

    def _range_search(self, node, rectangle, accumulator):

        if node is None:
            return

        if rectangle.inside_rect(node.point):
            accumulator.append(node.point)

        if rectangle.orthogonal_cross(node.point, node.direction):
            self._range_search(node.left, rectangle, accumulator)
            self._range_search(node.right, rectangle, accumulator)

        elif rectangle.point_is_on_left(node.point) and \
                node.direction == VERTICAL:
            self._range_search(node.left, rectangle, accumulator)

        elif rectangle.point_is_below(node.point) and \
                node.direction == HORISONTAL:
            self._range_search(node.right, rectangle, accumulator)

        elif rectangle.point_is_on_right(node.point) and \
                node.direction == VERTICAL:
            self._range_search(node.right, rectangle,  accumulator)

        elif rectangle.point_is_above(node.point) and \
                node.direction == HORISONTAL:
            self._range_search(node.left, rectangle,  accumulator)

    def find_closest_point(self, point):
        return self._find_closest_point(self.root, point, self.root.point)

    def _find_closest_point(self, node, destination, best_match):

        if node is None:
            return best_match

        # check if current is best match
        distance = destination.distance(node.point)
        min_distance = destination.distance(best_match)

        if distance < min_distance:
            best_match = node.point

        # where to go first
        if (node.point.left(destination) and node.direction == VERTICAL) or  \
           (node.point.below(destination) and node.direction == HORISONTAL):
            first_subtree = node.right
            second_subtree = node.left
        else:
            first_subtree = node.left
            second_subtree = node.right

        best_match = self._find_closest_point(first_subtree,
                                              destination, best_match)

        # should we check second subtree
        min_distance = destination.distance(best_match)
        if node.direction == VERTICAL:
            orthogonal_point = Point(node.point.x, destination.y)
        else:
            orthogonal_point = Point(destination.x, node.point.y)

        distance_to_orthogonal = destination.distance(orthogonal_point)

        if distance_to_orthogonal < min_distance:
            best_match = self._find_closest_point(second_subtree,
                                                  destination, best_match)

        return best_match

    def visualize_range_search(self, rectangle, points, found_points):
        rect_points = rectangle.get_clockwize_points()
        previous_point = rect_points[-1]
        for point in rect_points:
            plt.plot([point.x, previous_point.x],
                     [point.y, previous_point.y], 'r-')
            previous_point = point

        for point in points:
            plt.plot([point.x], [point.y], 'bo')

        for point in found_points:
            plt.plot([point.x], [point.y], 'go')

        plt.ylabel('range search')
        plt.show()

    def visualize_closest_point(self, points, closest_point, destination):

        for point in points:
            plt.plot([point.x], [point.y], 'bo')
        plt.plot([closest_point.x], [closest_point.y], 'go')
        plt.plot([destination.x], [destination.y], 'ro')

        plt.ylabel('closest point search')
        plt.show()

    def show_graph(self, name="2d_tree.png"):
        graph = pydot.Dot(graph_type='digraph')
        self._show_graph(self.root, graph)
        graph.write_png(name)

    def _make_node(self, node, graph):
        node_label_tmpl = "%s - %s - %s"

        if node is not None:
            node_text = node_label_tmpl % (node.point.x, node.point.y,
                                           "|" if node.direction else "-")
            graph_node = pydot.Node(node_text)
        else:
            # empty node
            graph_node = pydot.Node(str(uuid4()), style="invis")
        graph.add_node(graph_node)
        return graph_node

    def _show_graph(self, node, graph):
        if node is not None:
            root = self._make_node(node, graph)

            for child_node in [node.left, node.right]:
                child_node_graph = self._make_node(child_node, graph)
                edge = pydot.Edge(root, child_node_graph)
                graph.add_edge(edge)
                self._show_graph(child_node, graph)


if __name__ == "__main__":
    from random import shuffle
    a = TwoDTree()

    data = []
    points_num = 100
    x_list = [i for i in range(points_num)]
    y_list = [i for i in range(points_num)]
    shuffle(x_list)
    shuffle(y_list)

    data = [Point(x_list.pop(), y_list.pop()) for i in range(points_num)]

    for i in data:
        print(i)
        a.insert(i)

    a.show_graph()
    destination = Point(10, 10)
    closest_point = a.find_closest_point(destination)
    a.visualize_closest_point(data, closest_point, destination)

    points = a.range_search(Point(10, 10), Point(30, 40))
    print()
    for point in points:
        print(point)
    print(len(points))
    a.visualize_range_search(Rectangle(Point(10, 10), Point(30, 40)),
                             data, points)
