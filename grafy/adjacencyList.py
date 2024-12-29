class Graph():
    def __init__(self, n):
        self.adjacency_list = [[] for _ in range(n)]
        self.n = n

    def add_edge(self, v, u):
        self.adjacency_list[v].append(u)
    
    def delete_edge(self, v, u):
        if u in self.adjacency_list[v]:
            self.adjacency_list[v].remove(u)