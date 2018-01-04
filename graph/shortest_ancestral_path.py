from bfs import BFS
from sys import maxsize


class SAP():

    def get_sap(self, graph, a, b):
        bfs_a = BFS(graph, a)
        bfs_b = BFS(graph, b)
        a_connection = \
            [index for index, value in enumerate(bfs_a.marked) if value]
        b_connection = \
            [index for index, value in enumerate(bfs_b.marked) if value]
        common_verticies = set(a_connection).intersection(b_connection)
        min_distance = maxsize
        sap = -1
        for vert in common_verticies:
            current_distance = bfs_a.distance_to(b) + bfs_b.distance_to(a)
            if min_distance > current_distance:
                min_distance = current_distance
                sap = vert
        return sap


if __name__ == "__main__":
    from digraph import DiGraph
    graph_data = [(0, 1),
                  (1, 0),
                  (2, 0),
                  (3, 0),
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
    a = DiGraph(10)
    for edge in graph_data:
        a.add_edge(edge[0], edge[1])

    a.show_graph()
    sap = SAP().get_sap(a, 0, 5)
    print(sap)
