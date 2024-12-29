from collections import defaultdict

class Graph:
    def __init__(self, n):
        self.graph = defaultdict(list)
        self.n = n
        self.time = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def ap_util(self, u, visited, disc, low, parent, ap):
        children = 0
        visited[u] = True
        disc[u] = low[u] = self.time
        self.time += 1

        for v in self.graph[u]:
            if not visited[v]:
                parent[v] = u
                children += 1
                self.ap_util(v, visited, disc, low, parent, ap)
                low[u] = min(low[v], low[u])

                if parent[u] == -1 and children > 1:
                    ap[u] = True

                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True

            elif v != parent[u]:
                low[u] = min(disc[v], low[u])

    def tarjan_ap(self):
        visited = [False] * self.n
        disc = [-1] * self.n
        low = [-1] * self.n
        parent = [-1] * self.n
        articulation_points = [False] * self.n

        for v in range(self.n):
            if not visited[v]:
                self.ap_util(v, visited, disc, low, parent, articulation_points)

        for index,value in enumerate(articulation_points):
            if value:
                print(index, end=' ')


g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)

print("\nArticulation points in first graph ")
g1.tarjan_ap()

g2 = Graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print("\nArticulation points in second graph ")
g2.tarjan_ap()

g3 = Graph(7)
g3.addEdge(0, 1)
g3.addEdge(1, 2)
g3.addEdge(2, 0)
g3.addEdge(1, 3)
g3.addEdge(1, 4)
g3.addEdge(1, 6)
g3.addEdge(3, 5)
g3.addEdge(4, 5)
print("\nArticulation points in third graph ")
g3.tarjan_ap()
