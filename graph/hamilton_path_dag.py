from topological_sort import TopologicalSort


class HamiltonPathDAG(TopologicalSort):
    """
    If a topological sort has the property that all pairs of consecutive
     vertices in the sorted order are connected by edges, then these edges
     form a directed Hamiltonian path in the DAG. If a Hamiltonian
     path exists, the topological sort order is unique. Conversely, if a
     topological sort does not form a Hamiltonian path, the DAG will have
     two or more valid topological orderings
    """

    def hamilton_circuit(self, graph):
        topological_order = self.topological_sort(graph)
        previous_vert = topological_order[-1]
        for vert in topological_order:
            if vert not in graph.adj[previous_vert]:
                return []
            previous_vert = vert
        return topological_order


if __name__ == "__main__":
    from digraph import DiGraph
    graph_data = [(0, 1),
                  (1, 2),
                  (2, 3)]
    a = DiGraph(4)
    for edge in graph_data:
        a.add_edge(edge[0], edge[1])

    a.show_graph()
    assert HamiltonPathDAG().hamilton_circuit(a) == []
    a.add_edge(3, 0)
    assert HamiltonPathDAG().hamilton_circuit(a) == [0, 1, 2, 3]
