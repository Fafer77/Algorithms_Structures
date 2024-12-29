class DisjoinSet():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) # flattening (path compression)
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

    def detect_graph_cycle(self, edges):
        for edge in edges:
            v = self.find(edge[0])
            u = self.find(edge[1])
            if u == v:
                return True
            self.union(v, u)
        
        return False

edges_with_cycle = [
    (0, 1),
    (1, 2),
    (2, 3),
    (0, 3)
]

edges = [
    (0, 5),
    (1, 5),
    (0, 2),
    (4, 1),
    (3, 1)
]


ds = DisjoinSet(6)
print(ds.detect_graph_cycle(edges))
