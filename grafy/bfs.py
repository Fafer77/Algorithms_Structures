from adjacencyList import Graph as GraphList
from adjacencyMatrix import Graph as GraphMatrix
from queue import Queue


class BFSGraph(GraphList):
    def __init__(self, n):
        super().__init__(n)

    def bfs(self, v, visited=None):
        if visited is None:
            visited = [False] * len(self.adjacency_list)

        q = Queue()
        q.put(v)
        visited[v] = True

        while (not q.empty()):
            vertex = q.get()
            print(f'The visited vertex is {vertex}')

            for u in self.adjacency_list[vertex]:
                if not visited[u]:
                    q.put(u)
                    visited[u] = True             


g = BFSGraph(5)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 4)
g.add_edge(2, 3)

print("Przebieg BFS zaczynając od wierzchołka 0:")
g.bfs(0)
