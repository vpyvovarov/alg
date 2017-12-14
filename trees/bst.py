import pydot
from trees.node import Node
from uuid import uuid4


class BST():

    def __init__(self):
        self.root = None

    def put(self, key, value):
        self.root = self._put(self.root, key, value)

    def _put(self, root, key, value):
        if root is None:
            return Node(key, value)

        if root > key:
            root.left = self._put(root.left, key, value)
        elif root < key:
            root.right = self._put(root.right, key, value)
        else:
            # keys are equal, overwrite value
            root.value = value
        root.size = 1 + self.size(root.left) + self.size(root.right)
        return root

    def min(self, node=None):
        node = node or self.root
        while node.left is not None:
            node = node.left
        return node

    def max(self, node=None):
        node = node or self.root
        while node.right is not None:
            node = node.right
        return node

    def floor(self, key):
        return self._floor(self.root, key)

    def _floor(self, node, key):
        if node is None:
            return None
        if node.key > key:
            return self._floor(node.left, key)
        elif node.key == key:
            return node

        possible_floor = self._floor(node.right, key)
        if possible_floor is None:
            return node
        else:
            return possible_floor

    def ceil(self, key):
        return self._ceil(self.root, key)

    def _ceil(self, node, key):
        if node is None:
            return None
        if node.key < key:
            return self._ceil(node.right, key)
        elif node.key == key:
            return node

        possible_ceil = self._ceil(node.left, key)
        if possible_ceil is None:
            return node
        else:
            return possible_ceil

    def inorder(self):
        res = []
        self._inorder(self.root, res)
        return res

    def _inorder(self, node, accumulator):
        if node is None:
            return

        self._inorder(node.left, accumulator)
        accumulator.append(node.key)
        self._inorder(node.right, accumulator)

    def size(self, node):
        if node is None:
            return 0
        return node.size

    def delete_min(self):
        self.root = self._delete_min(self.root)

    def _delete_min(self, node):
        if node.left is None:
            return node.right
        node.left = self._delete_min(node.left)
        node.size = 1 + self.size(node.left) + self.size(node.right)
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if node.key > key:
            node.left = self._delete(node.left, key)
        elif node.key < key:
            node.right = self._delete(node.right, key)
        else:
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right

            right_min_node = self.min(node.right)
            node.right = self._delete_min(node.right)
            node.key = right_min_node.key
            node.value = right_min_node.value
        node.size = 1 + self.size(node.left) + self.size(node.right)
        return node

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

    def _show_graph(self, node, graph):
        if node is not None:
            root = self._make_node(node, graph)

            for child_node in [node.left, node.right]:
                child_node_graph = self._make_node(child_node, graph)
                edge = pydot.Edge(root, child_node_graph)
                graph.add_edge(edge)
                self._show_graph(child_node, graph)


if __name__ == "__main__":
    from random import shuffle, randint
    a = BST()
    data = [randint(0, 100) for i in range(10)]
    shuffle(data)
    for i in data:
        a.put(i, i)

    a.show_graph()
    print("min= %s" % a.min().key)
    print("max= %s" % a.max().key)
    print("floor 20 = %s" % a.floor(20).key)
    print("ceil 20 = %s" % a.ceil(20).key)
    print("in order : %s" % a.inorder())
    node_to_delete = a.inorder()[3]
    print("deleting node %s" % node_to_delete)
    a.delete(node_to_delete)
    print("in order : %s" % a.inorder())
    a.delete_min()
    print("min= %s" % a.min().key)
    print("max= %s" % a.max().key)
    print("floor 20 = %s" % a.floor(20).key)
    print("ceil 20 = %s" % a.ceil(20).key)
    print("in order : %s" % a.inorder())
    a.show_graph("example2_graph.png")
