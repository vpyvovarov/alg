import pydot


class Graph():

    def __init__(self, num_of_v):
        self.adj = [[] for _ in range(num_of_v)]

    def num_of_vert(self):
        return len(self.adj)

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


class DFS():
    """
    Build DFS in time proportional to sum of degrees of all vertices
    Find path in time proportional to length of the path
    is_connected in constant time
    """
    def __init__(self, graph, _from):
        self.marked = [False for _ in range(graph.num_of_vert())]
        self.edge_to = [None for _ in range(graph.num_of_vert())]
        self.dfs(graph, _from)
        self._from = _from

    def has_path(self, v):
        return self.marked[v]

    def path(self, _to):
        if not self.has_path(_to):
            return
        path = []
        v = _to
        while v != self._from:
            path.append(v)
            v = self.edge_to[v]
        return path

    def dfs(self, graph, _from):

        self.marked[_from] = True
        for adj in graph.adjacency(_from):
            if not self.marked[adj]:
                self.dfs(graph, adj)
                self.edge_to[adj] = _from


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
                  (7, 1)]
    a = Graph(10)
    for edge in graph_data:
        a.add_edge(edge[0], edge[1])

    a.show_graph()
    path = DFS(a, 0)
    print(path.marked)
    print(path.has_path(9))
    print(path.has_path(3))
    print(path.path(6))
