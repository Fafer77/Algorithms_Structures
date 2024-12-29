from adjacencyList import Graph

class GraphDegree(Graph):
    def __init__(self, n):
        super().__init__(n)

    def degree(self):
        n = len(self.adjacency_list)
        degree_list = [0 for _ in range(n)]
        for v in range(n):
            for u in self.adjacency_list[v]:
                if v == u:
                    degree_list[v] += 2
                else:
                    degree_list[v] += 1
                    degree_list[u] += 1
        
        max_degree = degree_list[0]
        for i in range(1, n):
            if degree_list[i] > max_degree:
                max_degree = degree_list[i]

        return max_degree
    

g = GraphDegree(8)
g.add_edge(3, 5)
g.add_edge(3, 4)
g.add_edge(2, 4)
g.add_edge(5, 2)
g.add_edge(7, 5)
g.add_edge(5, 7)

print(g.degree())
