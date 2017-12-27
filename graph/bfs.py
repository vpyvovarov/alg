from dfs import DFS


class Queue():

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def put(self, item):
        self.items.insert(0, item)

    def get(self):
        return self.items.pop()


class BFS(DFS):
    """
    Build BFS in time proportional to sum of degrees of all vertices
    Find path in time proportional to length of the path
    is_connected in constant time
    """

    def dfs(self, graph, _from):
        self.marked[_from] = True
        unexplored_vert = Queue()
        unexplored_vert.put(_from)

        while not unexplored_vert.is_empty():
            vert = unexplored_vert.get()
            self.marked[vert] = True
            for adj in graph.adjacency(vert):
                if not self.marked[adj]:
                    unexplored_vert.put(adj)
                    self.edge_to[adj] = vert


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

    bfs_path = BFS(a, 0)
    print(bfs_path.marked)
    assert not bfs_path.has_path(9)
    assert bfs_path.has_path(3)
    assert bfs_path.path(7)
