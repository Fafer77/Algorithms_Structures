from adjacencyList import Graph as GraphList

class DFSGraph(GraphList):
    def __init__(self, n):
        super().__init__(n)

    def create_visited(self, n):
        return [False for _ in range(n)]

    def dfs(self, v, visited=None):
        if visited is None:
            visited = self.create_visited(len(self.adjacency_list))
        
        counter = 0
        stack = [v]
        visited[v] = True

        while stack:
            vertex = stack.pop()
            counter += 1
            
            for u in self.adjacency_list[vertex]:
                if not visited[u]:
                    stack.append(u)
                    visited[u] = True
                    
        return counter

    def check_connectivity(self, v):
        return self.dfs(v) == self.n


g = DFSGraph(8)
g.add_edge(3, 5)
g.add_edge(3, 4)
g.add_edge(2, 4)
g.add_edge(5, 2)
g.add_edge(7, 5)
g.add_edge(5, 7)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(4, 6)
g.add_edge(5, 6)
g.add_edge(2, 0)

print(g.check_connectivity(3))
