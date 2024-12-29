import sys
from heapq import heappop, heappush
from collections import defaultdict

class Graph():
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def add_edge(self, v, u, weight):
        self.graph[v].append((u, weight))
        self.graph[u].append((v, weight))

    def print_mst(self, parent, dist):
        print("Edge \tWeight")
        total_weight = 0
        for i in range(1, self.V):
            print(f"{parent[i]} - {i} \t{dist[i]}")
            total_weight += dist[i]
        print(f"Total Weight of MST: {total_weight}")

    def prims(self):
        dist = [sys.maxsize] * (self.V)
        parent = [-1] * (self.V)
        in_mst = [False] * (self.V)

        dist[0] = 0
        pq = []
        heappush(pq, (0, 0))

        while pq:
            weight_u, u = heappop(pq)
            if in_mst[u]:
                continue
            
            in_mst[u] = True
            for v, weight in self.graph[u]:
                if weight < dist[v] and not in_mst[v]:
                    dist[v] = weight
                    parent[v] = u
                    heappush(pq, (weight, v))
                    
        self.print_mst(parent, dist)

graph = Graph(9)
graph.add_edge(0, 1, 4)
graph.add_edge(0, 7, 8)
graph.add_edge(1, 2, 8)
graph.add_edge(1, 7, 11)
graph.add_edge(2, 3, 7)
graph.add_edge(2, 8, 2)
graph.add_edge(2, 5, 4)
graph.add_edge(3, 4, 9)
graph.add_edge(3, 5, 14)
graph.add_edge(4, 5, 10)
graph.add_edge(5, 6, 2)
graph.add_edge(6, 7, 1)
graph.add_edge(6, 8, 6)
graph.add_edge(7, 8, 7)
graph.prims()

graph = Graph(7)
graph.add_edge(0, 1, 2)
graph.add_edge(6, 5, 2)
graph.add_edge(5, 4, 4)
graph.add_edge(5, 1, 7)
graph.add_edge(0, 3, 6)
graph.add_edge(1, 2, 3)
graph.add_edge(1, 4, 8)
graph.add_edge(3, 4, 5)

print("Minimal Spanning Tree (MST):")
graph.prims()
