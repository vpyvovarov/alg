from trees.heap import MinHeap


class LasyPrime():
    """
    Compute MST
    E log E  and at most E extra space
    """

    def prime(self, graph):
        vert = 0
        self.mst = []
        self.sorted_edges = MinHeap()
        self.marked = [vert]

        self.visit(vert, graph)
        while len(self.mst) < graph.num_of_vert() and \
                not self.sorted_edges.is_empty():
            next_edge = self.sorted_edges.pop()
            a = next_edge.either()
            b = next_edge.other(a)

            if a in self.marked and b in self.marked:
                continue
            self.mst.append(next_edge)
            vert = a if a not in self.marked else b
            self.visit(vert, graph)

        return self.mst

    def visit(self, vert, graph):
        self.marked.append(vert)
        for edge in graph.adjacency(vert):
            other = edge.other(vert)
            if other not in self.marked:
                self.sorted_edges.insert(edge)

    def preaty_print_result(self, mst):
        weight_sum = 0
        for edge in mst:
            print(edge)
            weight_sum += edge.weight
        print(weight_sum)


if __name__ == "__main__":
    from ewg import EWG, Edge
    graph_data = [(0, 1, 0.1),
                  (0, 2, 0.2),
                  (0, 3, 0.3),
                  (1, 4, 0.4),
                  (5, 4, 0.5),
                  (4, 2, 0.6),
                  (6, 3, 0.7),
                  (6, 1, 0.8),
                  (8, 9, 0.9),
                  (5, 7, 1.0),
                  (7, 1, 1.1)]
    a = EWG(10)
    for edge in graph_data:
        a.add_edge(Edge(edge[0], edge[1], edge[2]))

    a.show_graph()
    mst = LasyPrime().prime(a)
    LasyPrime().preaty_print_result(mst)
