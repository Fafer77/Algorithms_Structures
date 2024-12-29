import sys

class Graph():
    def __init__(self, V):
        self.V = V
        self.graph = [[0 for col in range(V)] for row in range(V)]

    def print_mst(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def min_dist(self, dist, mst_set):
        min_dist = sys.maxsize
        for v in range(self.V):
            if dist[v] < min_dist and mst_set[v] == False:
                min_dist = dist[v]
                min_index = v
        return min_index

    def prims(self):
        dist = [sys.maxsize] * (self.V)
        dist[0] = 0
        mst_set = [False] * (self.V)
        parent = [-1] * (self.V)
        
        for _ in range(self.V):
            u = self.min_dist(dist, mst_set)
            mst_set[u] = True

            for w in range(self.V):
                if self.graph[u][w] and mst_set[w] == False \
                and dist[w] > self.graph[u][w]:
                    dist[w] = self.graph[u][w]
                    parent[w] = u  

        self.print_mst(parent)

                    
if __name__ == '__main__':
    g = Graph(5)
    g.graph = [[0, 2, 0, 6, 0],
               [2, 0, 3, 8, 5],
               [0, 3, 0, 0, 7],
               [6, 8, 0, 0, 9],
               [0, 5, 7, 9, 0]]

    g.prims()
