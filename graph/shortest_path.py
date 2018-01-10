from sys import maxsize
from trees.heap import MutableHeap


class MinMutableHeap(MutableHeap):

    def compare(self, a, b):
        return a[-1] < b[-1]


class SP():

    def __init__(self, graph, start_vertex):
        self.graph = graph
        self.start_vertex = start_vertex
        self.dist_to = [maxsize] * self.graph.num_of_vert()
        self.edge_to = [-1] * self.graph.num_of_vert()
        self.pq = MinMutableHeap()

        self.dist_to[start_vertex] = 0.0
        self.pq.insert((start_vertex, 0.0))

        covered_vert = 0

        while covered_vert < self.graph.num_of_vert() and not self.pq.is_empty():
            vert, dist = self.pq.pop()

            for edge in self.graph.adjacency(vert):
                self.relax(edge)

    def distance_to(self, vertex):
        return self.dist_to[vertex]

    def path_to(self, vertex):
        path = []
        while self.edge_to[vertex] and vertex != self.start_vertex:
            path.append(self.edge_to[vertex])
            vertex = self.edge_to[vertex].start()
        return path

    def relax(self, edge):
        new_dist = self.dist_to[edge.start()] + edge.weight
        if self.dist_to[edge.end()] > new_dist:
            previous_dist = self.dist_to[edge.end()]
            self.dist_to[edge.end()] = new_dist
            self.edge_to[edge.end()] = edge
            if self.pq.contains((edge.end(), new_dist)):
                self.pq.change((edge.end(), previous_dist),
                               (edge.end(), new_dist))
            else:
                self.pq.insert((edge.end(), new_dist))

    def pretty_print(self, path):
        for edge in path:
            print(edge)


if __name__ == "__main__":
    from dewg import DirectedEdge, DirectedEDG
    graph_data = [(0, 1, 0.1),
                  (0, 2, 0.2),
                  (0, 3, 0.3),
                  (1, 4, 0.4),
                  (5, 4, 0.5),
                  (4, 2, 0.6),
                  (6, 3, 0.7),
                  (6, 1, 0.8),
                  (8, 9, 0.2),
                  (5, 8, 0.2),
                  (9, 0, 0.2),
                  (5, 7, 1.0),
                  (7, 1, 1.1)]
    a = DirectedEDG(10)
    for edge in graph_data:
        a.add_edge(DirectedEdge(edge[0], edge[1], edge[2]))

    a.show_graph()

    sp = SP(a, 5)
    path = sp.path_to(2)
    sp.pretty_print(path)
    print(sp.distance_to(2))
