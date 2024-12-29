class Graph():
    def __init__(self, n, m):
        self.adjacency_list = [[] for _ in range(n)]
        self.max_edges = m
        self.edges = 0

    def add_edge(self, v, u, i):
        try:
            if (self.edges >= self.max_edges):
                raise ValueError(f'Maximum number of edges had already been reached {self.max_edges}')
            
            self.adjacency_list[v].append((u, i))
            self.edges += 1
        except ValueError as e: 
            print(e)

    def create_line_graph(self):
        line_graph = [[] for _ in range(self.max_edges)]
        for v, neighbors in enumerate(self.adjacency_list):
            for u_edge_pair in neighbors:
                u, edge_id = u_edge_pair
                for w_edge_pair in self.adjacency_list[u]:
                    w, snd_edge_id = w_edge_pair
                    if w != v:
                        line_graph[edge_id].append((u, w, snd_edge_id))
        return line_graph

G = Graph(5, 8)
G.add_edge(4, 1, 1)
G.add_edge(2, 3, 2)
G.add_edge(2, 1, 3)
G.add_edge(3, 1, 4)
G.add_edge(0, 2, 5)

G3 = Graph(5, 6)
G3.add_edge(0, 1, 0)
G3.add_edge(1, 2, 1)
G3.add_edge(2, 3, 2)
G3.add_edge(3, 4, 3)
G3.add_edge(4, 0, 4)
G3.add_edge(1, 4, 5)

GE = G3.create_line_graph()
print(GE)
