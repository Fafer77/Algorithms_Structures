from adjacencyList import Graph as GraphList
from adjacencyMatrix import Graph as GraphMatrix

class DFSGraph(GraphList):
    def __init__(self, n):
        super().__init__(n)

    def create_visited(self, n):
        return [False for _ in range(n)]

    def dfs_recursive(self, v, visited=None):
        if visited is None:
            visited = self.create_visited(len(self.adjacency_list))
        
        visited[v] = True
        print(f'The visited vertex is {v}')

        for u in self.adjacency_list[v]:
            if not visited[u]:
                self.dfs_recursive(u, visited)

    def dfs_iterative(self, v, visited=None):
        if visited is None:
            visited = self.create_visited(len(self.adjacency_list))
        
        stack = [v]
        visited[v] = True

        while (stack):
            vertex = stack.pop()
            print(f'The visited vertex is {vertex}')
            
            for u in self.adjacency_list[vertex]:
                if not visited[u]:
                    stack.append(u)
                    visited[u] = True


class DFSGraphMatrix(GraphMatrix):
    def __init__(self, n):
        super().__init__(n)

    def dfs_recursive(self, v, visited=None):
        if visited is None:
            visited = [False] * self.V
        
        visited[v] = True
        print(f'The visited vertex is {v}')

        for u in range(self.V):
            if not visited[u] and self.adjacencyMatrix[v][u] == 1:
                self.dfs_recursive(u, visited)

g = DFSGraph(8)
g.add_edge(3, 5)
g.add_edge(3, 4)
g.add_edge(2, 4)
g.add_edge(5, 2)
g.add_edge(7, 5)
g.add_edge(5, 7)
g.dfs_iterative(3)
