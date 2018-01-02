from digraph import DiGraph


class TopologicalSort():

    def dfs(self, graph, start):
        self.marked[start] = True
        for adj in graph.adjacency(start):
            if not self.marked[adj]:
                self.dfs(graph, adj)
        self.stack.append(start)

    def topological_sort(self, graph):
        self.stack = []
        self.marked = [False for _ in range(graph.num_of_vert())]
        self.edge_to = [None for _ in range(graph.num_of_vert())]

        for vert in range(graph.num_of_vert()):
            if not self.marked[vert]:
                self.dfs(graph, vert)

        self.stack.reverse()
        return self.stack


if __name__ == "__main__":
    graph_data = [(4, 2),
                  (2, 3),
                  (3, 2),
                  (6, 0),
                  (0, 1),
                  (2, 0),
                  (11, 12),
                  (12, 9),
                  (9, 10),
                  (9, 11),
                  (7, 9),
                  (10, 12),
                  (11, 4),
                  (4, 3),
                  (3, 5),
                  (6, 8),
                  (8, 6),
                  (5, 4),
                  (0, 5),
                  (6, 4),
                  (6, 9),
                  (7, 6)]
    a = DiGraph(13)
    for edge in graph_data:
        a.add_edge(edge[0], edge[1])
    tsorted = TopologicalSort().topological_sort(a.reverse())
    print(tsorted)
    assert [1, 0, 2, 3, 4, 11, 9, 12, 10, 6, 8, 7, 5] == tsorted
