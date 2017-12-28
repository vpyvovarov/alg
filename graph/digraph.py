import pydot
from graph import Graph


class DiGraph(Graph):

    def add_edge(self, v1, v2):
        self.adj[v1].append(v2)

    def show_graph(self, name="digraph_show.png"):
        graph = pydot.Dot(graph_type='digraph')
        node_label_tmpl = "%s"
        for index, adj in enumerate(self.adj):
            v1_node = pydot.Node(node_label_tmpl % index)
            graph.add_node(v1_node)
            for v2 in adj:
                v2_node = pydot.Node(node_label_tmpl % v2)
                graph.add_node(v2_node)
                edge = pydot.Edge(v1_node, v2_node)
                graph.add_edge(edge)
        graph.write_png(name)


if __name__ == "__main__":
    graph_data = [(0, 1),
                  (1, 0),
                  (2, 0),
                  (3, 0),
                  (0, 2),
                  (0, 3),
                  (1, 4),
                  (5, 4),
                  (4, 2),
                  (6, 3),
                  (6, 1),
                  (8, 9),
                  (5, 7),
                  (7, 1)]
    a = DiGraph(10)
    for edge in graph_data:
        a.add_edge(edge[0], edge[1])

    a.show_graph()
