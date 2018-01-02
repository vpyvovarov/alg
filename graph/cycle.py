from graph import Graph


class CycleDetection():

    def dfs(self, vert, previous, graph):
        self.marked[vert] = True
        for adj in graph.adjacency(vert):
            if not self.marked[adj]:
                if self.dfs(adj, vert, graph):
                    return True
            elif previous is not None and previous != adj:
                return True
        return False

    def contain_cycle(self, graph):

        self.marked = [False for _ in range(graph.num_of_vert())]
        self.edge_to = [None for _ in range(graph.num_of_vert())]
        for i in range(graph.num_of_vert()):
            if not self.marked[i]:
                if self.dfs(i, None, graph):
                    return True
        return False


def make_graph(graph_data):
    graph = Graph(5)
    for edge in graph_data:
        graph.add_edge(edge[0], edge[1])
    return graph


if __name__ == "__main__":
    graph_data = [(1, 0),
                  (0, 2),
                  (2, 0),
                  (0, 3),
                  (2, 4)]

    without_cycle = make_graph(graph_data)
    without_cycle.show_graph("without_cycle.png")
    assert not CycleDetection().contain_cycle(without_cycle)

    graph_data.append((4, 3))
    with_cycle = make_graph(graph_data)
    with_cycle.show_graph("with_cycle.png")
    assert CycleDetection().contain_cycle(with_cycle)
