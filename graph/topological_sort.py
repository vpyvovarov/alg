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

        return self.stack


if __name__ == "__main__":
    graph_data = [(0, 5),
                  (0, 1),
                  (3, 5),
                  (5, 2),
                  (6, 0),
                  (1, 4),
                  (0, 2),
                  (3, 6),
                  (3, 4),
                  (6, 4),
                  (3, 2)]
    a = DiGraph(7)
    for edge in graph_data:
        a.add_edge(edge[0], edge[1])

    a.show_graph()
    tsorted = TopologicalSort().topological_sort(a)
    print(tsorted)
    assert [2, 5, 4, 1, 0, 6, 3] == tsorted
