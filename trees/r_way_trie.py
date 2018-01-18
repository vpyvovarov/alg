import pydot
from functools import total_ordering
from collections import defaultdict


@total_ordering
class Node():

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.childrens = defaultdict(lambda: None)

    def __eq__(self, other):
        other_key = other
        if issubclass(type(other), self.__class__):
            other_key = other.key
        return self.key == other_key

    def __lt__(self, other):
        other_key = other
        if issubclass(type(other), self.__class__):
            other_key = other.key
        return self.key < other_key


class RWayTrie():

    def __init__(self):
        self.root = Node()

    def add(self, key, value):
        self.root.childrens[key[0]] = self._add(self.root, key, value, index=0)

    def _add(self, node, key, value, index):

        if node is None:
            node = Node(key[index])

        if node.key != key[index]:
            node = self._add(node.childrens[key[index]], key, value, index)

        if len(key) == index + 1:
            node.value = value
            return node

        next_letter = key[index + 1]
        node.childrens[next_letter] = self._add(node.childrens[next_letter],
                                                key, value, index + 1)
        return node

    def find(self, key):
        pass

    def show_graph(self, name="example_r_trie.png"):
        graph = pydot.Dot(graph_type='graph')
        self._show_graph(self.root, graph)
        graph.write_png(name)

    def _make_node(self, node, graph):
        node_label_tmpl = "%s - %s - %s - %s"

        if node is not None:
            node_text = node_label_tmpl % (node.key,
                                           node.value,
                                           str(id(node)),
                                           str(node.childrens.keys()))
            graph_node = pydot.Node(node_text)
        graph.add_node(graph_node)
        return graph_node

    def _show_graph(self, node, graph):
        if node is not None:
            root = self._make_node(node, graph)

            for child_node in node.childrens.values():
                child_node_graph = self._make_node(child_node, graph)
                edge = pydot.Edge(root, child_node_graph)
                graph.add_edge(edge)
                self._show_graph(child_node, graph)


if __name__ == "__main__":

    data = ["she", "sells", "sea", "shells", "by", "the", "shore"]

    a = RWayTrie()
    for index, word in enumerate(data):
        a.add(word, index)
    a.show_graph()
