import pydot


class Graph():

    def __init__(self, num_of_v):
        self.adj = [[] for _ in range(num_of_v)]

    def add_edge(self, v1, v2):
        self.adj[v1].append(v2)
        self.adj[v2].append(v1)

    def adjacency(self, v):
        return self.adj[v]

    def show_graph(self, name="graph_show.png"):
        graph = pydot.Dot(graph_type='graph', simplify=True)
        node_label_tmpl = "%s"
        for index, adj in enumerate(self.adj):
            v1_node = pydot.Node(node_label_tmpl % index)
            graph.add_node(v1_node)
            for v2 in adj:
                v2_node = pydot.Node(node_label_tmpl % v2)
                graph.add_node(v2_node)
                edge = pydot.Edge(v1_node, v2_node, arrowhead=False)
                graph.add_edge(edge)
        graph.write_png(name)


if __name__ == "__main__":
    graph_data = [(0, 1),
                  (0, 2),
                  (0, 3),
                  (1, 4),
                  (5, 4),
                  (4, 2),
                  (6, 3),
                  (6, 1),
                  (8, 9),
                  (8, 7),
                  (7, 1),
                  (9, 0)]
    a = Graph(10)
    for edge in graph_data:
        a.add_edge(edge[0], edge[1])

    a.show_graph()
