from graph import Graph


class EulerFinder():

    def circuit_exists(self, graph):
        for vertex in range(graph.num_of_vert()):
            if len(graph.adj) % 2 != 0:
                return False
        return True

    def find_euler_cicuit(self, graph, start_point=None):
        if start_point is None:
            self.path = []
            start_point = 0
            graph = graph.copy()
        else:
            self.path.append(start_point)

        for next_vertex in graph.adj[start_point]:
            if len(graph.adj[next_vertex]) > 1:
                # prefere not bridges
                # bridge is a edge to vertex of 1st degree
                break

        if next_vertex:
            graph.delete_edge(start_point, next_vertex)
            self.find_euler_cicuit(graph, start_point=next_vertex)
        return self.path


if __name__ == "__main__":
    graph_data = [(0, 1),
                  (0, 3),
                  (1, 2),
                  (2, 3)
                  ]
    a = Graph(4)
    for edge in graph_data:
        a.add_edge(edge[0], edge[1])

    a.show_graph()
    print(EulerFinder().circuit_exists(a))
    print(EulerFinder().find_euler_cicuit(a))
