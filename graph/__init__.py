import pydot


class Graph():
    
    def __init__(self, num_of_v):
        self.adj = [[] for _ in range(num_of_v)]
    
    def add_edge(self, v1, v2):
        self.adj[v1].append(v2)
        self.adj[v2].append(v1)
    
    def adjacency(self, v):
        return self.adj[v]

    def show_graph(self, name="graph.png"):
        graph = pydot.Dot(graph_type='digraph')
        node_label_tmpl = "%s"
        for v1 in self.adj:
            v1_node = pydot.Node(node_label_tmpl % v1)
            graph.add_node(v1_node)
            for v2 in self.adj[v1]:
                v2_node = pydot.Node(node_label_tmpl % v2)
                graph.add_node(v2_node)
                edge = pydot.Edge(v1_node, v2_node)
                graph.add_edge(edge)

        graph.write_png(name)

if __name__ == "__manin__":
    graph_data = [(0, 1),
                  (0, 2),
                  (0, 3),
                  (1, 4),
                  (5, 4)]
    a = Graph(len(graph_data))
    for edge in graph_data:
        a.add_edge(edge[0], edge[1])
    
    a.show_graph