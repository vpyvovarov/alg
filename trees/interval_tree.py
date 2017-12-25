import pydot
from uuid import uuid4


class IntervalNode():

    def __init__(self, start, end, max_end=None, left=None, right=None):
        self.start = start
        self.end = end
        self.max_end = self.end
        self.left = left
        self.right = right

    def __str__(self):
        return "%s - %s" % (self.start, self.end)

    def intersect(self, start, end):
        return self.start <= start and self.end >= end


class IntervalTree():

    def __init__(self):
        self.root = None

    def insert(self, start, end):
        self.root = self._insert(start, end,  self.root)

    def _insert(self, start, end, root):

        if root is None:
            return IntervalNode(start, end)

        if root.start > start:
            root.left = self._insert(start, end, root.left)
            possible_max_end = root.left.max_end
        else:
            root.right = self._insert(start, end, root.right)
            possible_max_end = root.right.max_end

        if root.max_end < possible_max_end:
            root.max_end = possible_max_end

        return root

    def intersection(self, start, end):
        return self._intersection(start, end, self.root)

    def _intersection(self, start, end, node):

        if node is None:
            return

        if node.intersect(start, end):
            return node

        elif node.left is None:
            return self._intersection(start, end, node.right)
        elif node.left.max_end < start:
            return self._intersection(start, end, node.right)
        else:
            return self._intersection(start, end, node.left)

    def show_graph(self, name="interval_tree.png"):
        graph = pydot.Dot(graph_type='digraph')
        self._show_graph(self.root, graph)
        graph.write_png(name)

    def _make_node(self, node, graph):
        node_label_tmpl = "%s - %s - %s"

        if node is not None:
            node_text = node_label_tmpl % (node.start, node.end, node.max_end)
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
    from random import randint
    a = IntervalTree()

    data = []
    intervals_num = 10
    interval_range_low = 0
    interval_range_high = 20
    intervals = []
    for _ in range(intervals_num):
        start = randint(interval_range_low, interval_range_high - 1)
        end = randint(start, interval_range_high)
        intervals.append([start, end])

    for interval in intervals:
        print(interval)
        a.insert(interval[0], interval[1])

    a.show_graph()
    res = a.intersection(2, 3)
    print()
    print("[%s, %s]" % (res.start, res.end))
