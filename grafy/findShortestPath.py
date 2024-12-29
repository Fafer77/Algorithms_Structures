from adjacencyList import Graph as GraphList
from queue import Queue


class Graph(GraphList):
    def __init__(self, n):
        super().__init__(n)

    def find_path_BFS(self, vs, ul):
        n = len(self.adjacency_list)
        visited = [False] * n
        path = [-1] * n

        q = Queue()
        q.put(vs)
        visited[vs] = True

        while not q.empty():
            v = q.get()
            if v == ul:
                break

            for u in self.adjacency_list[v]:
                if not visited[u]:
                    visited[u] = True
                    q.put(u)
                    path[u] = v

        path_track = []
        if path[ul] == -1:
            print(f'No path was found between {vs} and {ul}')
        else:
            while ul != -1:
                path_track.append(ul)
                ul = path[ul]
            path_track.reverse()
            print('Path:', ' -> '.join(map(str, path_track)))


g = Graph(8)

g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(3, 5)
g.add_edge(2, 4)
g.add_edge(5, 2)
g.add_edge(7, 5)
g.add_edge(5, 7)

g.find_path_BFS(3, 7)
