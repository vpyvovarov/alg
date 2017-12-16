import pydot
from trees.node import Node
from uuid import uuid4


RED = 1
BLACK = 0


class RbNode(Node):

    def __init__(self, key, value, left=None, right=None, size=1, color=RED):
        self.color = color
        super(RbNode, self).__init__(key, value,
                                     left=left, right=right, size=size)


class RBT():

    def __init__(self):
        self.root = None

    def put(self, key, value):
        self.root = self._put(self.root, key, value)

    def _put(self, root, key, value):
        if root is None:
            return RbNode(key, value)

        if root > key:
            root.left = self._put(root.left, key, value)
        elif root < key:
            root.right = self._put(root.right, key, value)
        else:
            # keys are equal, overwrite value
            root.value = value

        if self.is_red(root.right) and not self.is_red(root.left):
            root = self.rotate_to_left(root)
        if self.is_red(root.left) and self.is_red(root.left.left):
            root = self.rotate_to_right(root)
        if self.is_red(root.left) and self.is_red(root.right):
            self.flip_color(root)

        return root

    def rotate_to_right(self, node):
        new_root = node.left
        node.left = node.left.right
        new_root.right = node
        new_root.color = node.color
        node.color = RED

        return new_root

    def rotate_to_left(self, node):
        new_root = node.right
        node.right = node.right.left
        new_root.left = node
        new_root.color = node.color
        node.color = RED

        return new_root

    def flip_color(self, node):
        node.color = RED
        node.left.color = BLACK
        node.right.color = BLACK

    def show_graph(self, name="example1_graph.png"):
        graph = pydot.Dot(graph_type='digraph')
        self._show_graph(self.root, graph)
        graph.write_png(name)

    def _make_node(self, node, graph):
        node_label_tmpl = "%s - %s - %s"

        if node is not None:
            node_text = node_label_tmpl % (node.key, node.value, node.size)
            graph_node = pydot.Node(node_text)
        else:
            # empty node
            graph_node = pydot.Node(str(uuid4()),  style="invis")
        graph.add_node(graph_node)
        return graph_node

    def is_red(self, node):
        if node is None:
            return False
        return node.color == RED

    def _show_graph(self, node, graph):
        if node is not None:
            root = self._make_node(node, graph)

            for child_node in [node.left, node.right]:
                child_node_graph = self._make_node(child_node, graph)
                edge = pydot.Edge(root, child_node_graph)
                if self.is_red(child_node):
                    edge.set_color("red")
                graph.add_edge(edge)
                self._show_graph(child_node, graph)


if __name__ == "__main__":
    from random import shuffle, randint
    a = RBT()
    data = [randint(0, 100) for i in range(10)]
    shuffle(data)
    for i in data:
        a.put(i, i)

    a.show_graph()
