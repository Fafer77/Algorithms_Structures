import sys
from heapq import heappush, heappop
from collections import defaultdict

class Graph():
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))
    
    def dijkstra(self, src):
        dist = [sys.maxsize] * (self.V)
        dist[src] = 0
        parent = [-1] * (self.V)
        pq = []
        heappush(pq, (0, src))

        while pq:
            current_dist, u = heappop(pq)

            for v, weight in self.graph[u]:
                if current_dist + weight < dist[v]:
                    dist[v] = current_dist + weight
                    parent[v] = u
                    heappush(pq, (dist[v], v))

        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(f"{node} \t {dist[node]}")
        print("\nShortest Paths:")
        for node in range(self.V):
            if parent[node] != -1:
                print(f"U->V: {parent[node]} -> {node} wt = {dist[node] - dist[parent[node]]}")


g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(2, 3, 7)
g.add_edge(2, 8, 2)
g.add_edge(2, 5, 4)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(6, 8, 6)
g.add_edge(7, 8, 7)

g.dijkstra(0)
