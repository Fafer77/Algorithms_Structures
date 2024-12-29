from adjacencyList import Graph

class GraphPath(Graph):
    def __init__(self, n):
        super().__init__(n)

    def dfs(self, v, x, stack, visited=None):
        if visited is None:
            visited = [False] * len(self.adjacency_list)
        
        visited[v] = True
        stack.append(v)

        if v == x:
            return True

        for u in self.adjacency_list[v]:
            if not visited[u]:
                if self.dfs(u, x, stack, visited):
                    return True
        
        stack.pop()
        return False

    def find_path(self, v, u):
        n = len(self.adjacency_list)
        visited = [False] * n
        path_list = [-1] * n

        stack = [v]
        visited[v] = True

        while stack:
            w = stack.pop(0)
            if w == u:
                break
            
            for t in self.adjacency_list[w]:
                if not visited[t]:        
                    path_list[t] = w
                    stack.append(t)
                    visited[t] = True
        
        if path_list[u] == -1:
            print(f'No path was found between {v} and {u}')
        else:
            path = []
            while u != -1:
                path.append(u)
                u = path_list[u]
            path.reverse()
            print('Path:', ' -> '.join(map(str, path)))


    def find_path_second(self, v, u):
        stack = []

        if self.dfs(v, u, stack):
            print('Path:', ' -> '.join(map(str, stack)))
        else:
            print(f'No path between {v} and {u}')


g = GraphPath(8)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(2, 4)
g.add_edge(5, 2)
g.add_edge(7, 5)
g.add_edge(5, 7)

g.find_path_second(3, 7)
