from adjacencyList import Graph

class GraphT(Graph):
    def __init__(self, n):
        super().__init__(n)

    def transpose(self):
        num_vertices = len(self.adjacency_list)
        transposed_list = [[] for _ in range(num_vertices)]

        for v in range(num_vertices):
            for u in self.adjacency_list[v]:
                transposed_list[u].append(v)
        
        return transposed_list


g = GraphT(8)
g.add_edge(3, 5)
g.add_edge(3, 4)
g.add_edge(2, 4)
g.add_edge(5, 2)
g.add_edge(7, 5)
g.add_edge(5, 7)

print(g.transpose())
