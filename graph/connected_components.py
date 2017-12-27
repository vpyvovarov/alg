from dfs import DFS


class CC(DFS):

    def __init__(self, graph):
        self.edge_to = [None for _ in range(graph.num_of_vert())]
        self.marked = [False for _ in range(graph.num_of_vert())]
        self.analyze(graph)

    def is_connected(self, a, b):
        return self.edge_to[b] == self.edge_to[a]

    def count(self):
        return len(set(self.edge_to))

    def dfs(self, graph, _from, start_vert):

        self.marked[_from] = True
        for adj in graph.adjacency(_from):
            if not self.marked[adj]:
                self.dfs(graph, adj, start_vert)
                self.edge_to[adj] = start_vert

    def analyze(self, graph):
        for vert in range(graph.num_of_vert()):
            if not self.marked[vert]:
                self.edge_to[vert] = vert
                self.dfs(graph, vert, vert)


if __name__ == "__main__":
    from graph import Graph
    graph_data = [(0, 1),
                  (6, 3),
                  (6, 1),
                  (7, 1)]
    a = Graph(10)
    for edge in graph_data:
        a.add_edge(edge[0], edge[1])

    a.show_graph()

    cc = CC(a)
    assert cc.count() == 6
    print(cc.edge_to)
    assert cc.is_connected(3, 0)
    assert not cc.is_connected(4, 5)
    assert not cc.is_connected(0, 4)
