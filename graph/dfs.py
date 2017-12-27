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
    from graph import Graph
    graph_data = [(0, 1),
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
    a = Graph(10)
    for edge in graph_data:
        a.add_edge(edge[0], edge[1])

    a.show_graph()
    dfs_path = DFS(a, 0)
    print(dfs_path.marked)
    assert not dfs_path.has_path(9)
    assert dfs_path.has_path(3)
    assert dfs_path.path(7)
