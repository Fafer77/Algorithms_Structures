import sys

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for col in range(vertices)]
                      for row in range(vertices)]

    def print_solution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])

    def _min_distance(self, dist, processed):
        mini = sys.maxsize
        for u in range(self.V):
            if dist[u] < mini and processed[u] == False:
                mini = dist[u]
                min_index = u
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * (self.V)
        dist[src] = 0
        processed = [False] * (self.V)
        parent = [-1] * (self.V)

        for v in range(self.V):
            u = self._min_distance(dist, processed)
            processed[u] = True

            for w in range(self.V):
                if(self.graph[u][w] != 0 and not processed[w] and dist[u] != sys.maxsize and
                    dist[u] + self.graph[u][w] < dist[w]):
                    dist[w] = dist[u] + self.graph[u][w]
                    parent[w] = u

        for i in range(self.V):
            print(f"U->V: {parent[i]} -> {i} wt = {self.graph[parent[i]][i]}")

        self.print_solution(dist)

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
            [4, 0, 8, 0, 0, 0, 0, 11, 0],
            [0, 8, 0, 7, 0, 4, 0, 0, 2],
            [0, 0, 7, 0, 9, 14, 0, 0, 0],
            [0, 0, 0, 9, 0, 10, 0, 0, 0],
            [0, 0, 4, 14, 10, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 1, 6],
            [8, 11, 0, 0, 0, 0, 1, 0, 7],
            [0, 0, 2, 0, 0, 0, 6, 7, 0]
            ]

g.dijkstra(0)
