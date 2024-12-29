from adjacencyList import Graph as GraphList

class Graph(GraphList):
    def __init__(self, n):
        super().__init__(n)

    def _DFSTree(self, v, visited, spanning_tree):
        visited[v] = True
        for u in self.adjacency_list[v]:
            if not visited[u]:
                spanning_tree[u].append(v)
                spanning_tree[v].append(u)
                self._DFSTree(u, visited, spanning_tree)

    def find_spanning_tree(self, v):
        visited = [False] * self.n
        spanning_tree = [[] for _ in range(self.n)]
        self._DFSTree(v, visited, spanning_tree)
        return spanning_tree
    
g = Graph(5)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(3, 2)
g.add_edge(3, 4)
g.add_edge(4, 0)
g.add_edge(1, 3)
g.add_edge(4, 1)

print(g.find_spanning_tree(0))