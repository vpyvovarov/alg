import pydot
from ewg import Edge, EWG


class DirectedEdge(Edge):

    def start(self):
        return self.a

    def end(self):
        return self.b


class DirectedEDG(EWG):

    def add_edge(self, edge):
        self.adj[edge.start()].append(edge)

    def show_graph(self, name="dewg_show.png"):
        graph = pydot.Dot(graph_type='digraph')
        node_label_tmpl = "%s"
        for index, adj in enumerate(self.adj):
            v1_node = pydot.Node(node_label_tmpl % index)
            graph.add_node(v1_node)
            for edge in adj:
                v2_node = pydot.Node(node_label_tmpl % edge.other(index))
                graph.add_node(v2_node)
                edge = pydot.Edge(v1_node, v2_node,
                                  label=str(edge.weight))
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
    a = DirectedEDG(10)
    for edge in graph_data:
        a.add_edge(DirectedEdge(edge[0], edge[1], edge[2]))

    a.show_graph()
