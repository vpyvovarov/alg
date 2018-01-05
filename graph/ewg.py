import pydot
from functools import total_ordering


@total_ordering
class Edge():

    def __init__(self, a, b, weight):
        self.weight = weight
        self.a = a
        self.b = b

    def either(self):
        return self.a

    def other(self, a):
        return self.b if a == self.a else self.a

    def __str__(self):
        return "%s -> %s %s" % (self.a, self.b, self.weight)

    def __eq__(self, other):
        return self.weight == other.weight

    def __lt__(self, other):
        return self.weight < other.weight


class EWG():

    def __init__(self, num_of_v):
        self.adj = [[] for _ in range(num_of_v)]

    def num_of_vert(self):
        return len(self.adj)

    def add_edge(self, edge):
        a = edge.either()
        b = edge.other(a)
        self.adj[a].append(edge)
        self.adj[b].append(edge)

    def edges(self):
        result = set()
        for edges in self.adj.values():
            result.update(edges)
        return result

    def adjacency(self, v):
        return self.adj[v]

    def show_graph(self, name="ewg_show.png"):
        graph = pydot.Dot(graph_type='graph', simplify=True)
        node_label_tmpl = "%s"
        for index, adj in enumerate(self.adj):
            v1_node = pydot.Node(node_label_tmpl % index)
            graph.add_node(v1_node)
            for edge in adj:
                v2_node = pydot.Node(node_label_tmpl % edge.other(index))
                graph.add_node(v2_node)
                edge = pydot.Edge(v1_node, v2_node,
                                  label=str(edge.weight),
                                  arrowhead=False)
                graph.add_edge(edge)
        graph.write_png(name)


if __name__ == "__main__":
    graph_data = [(0, 1, 0.1),
                  (0, 2, 0.2),
                  (0, 3, 0.3),
                  (1, 4, 0.4),
                  (5, 4, 0.5),
                  (4, 2, 0.6),
                  (6, 3, 0.7),
                  (6, 1, 0.8),
                  (8, 9, 0.9),
                  (5, 7, 1.0),
                  (7, 1, 1.1)]
    a = EWG(10)
    for edge in graph_data:
        a.add_edge(Edge(edge[0], edge[1], edge[2]))

    a.show_graph()
