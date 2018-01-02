from topological_sort import TopologicalSort
from connected_components import CC
from digraph import DiGraph


class StrongComponents(CC):
    """
    In direct graphs two verticies v and w are strongly connected if there
     is a direct path from w to v and from w to v.
     1. v is strongly connected to v
     2. if v is strongly connected to w then w is strongly connected to w
     3. if v is strongly connected to w and w is strongly connected to x then
     x is strongly connected to v.
     Computational time E + V
    """
    def analyze(self, graph):
        reversed = graph.reverse()
        tsorted = TopologicalSort().topological_sort(reversed)
        print(tsorted)
        for vert in tsorted:
            if not self.marked[vert]:
                self.edge_to[vert] = vert
                self.dfs(graph, vert, vert)


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

    a.show_graph()
    sc = StrongComponents(a)
    print(sc.edge_to)
    assert [1, 0, 2, 3, 4, 11, 9, 12, 10, 6, 8, 7, 5] == sc.edge_to
