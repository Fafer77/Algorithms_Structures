from collections import defaultdict, deque

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
    
    def add_edge(self, u , v):
        self.graph[u].append(v)

    def _dfs(self, v, visited, stack):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self._dfs(neighbor, visited, stack)
        stack.append(v)
    
    def _transpose(self):
        graph_t = Graph(self.V)
        for node in self.graph:
            for v in self.graph:
                for neighbor in self.graph[v]:
                    graph_t.add_edge(neighbor, v)
        return graph_t
    
    def _fill_order(self, visited, stack):
        for v in range(self.V):
            if not visited[v]:
                self._dfs(v, visited, stack)

    def _dfs_util(self, v, visited, component):
        visited[v] = True
        component.append(v)
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self._dfs_util(neighbor, visited, component)

    def kosaraju(self):
        stack = deque()
        visited = [False] * self.V

        self._fill_order(visited, stack)
        transposed_graph = self._transpose()

        visited = [False] * self.V
        scc_list = []

        while stack:
            node = stack.pop()
            if not visited[node]:
                component = []
                transposed_graph._dfs_util(node, visited, component)
                scc_list.append(component)
        return scc_list

if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)

    g2 = Graph(4)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 0)
    g2.add_edge(3, 2)

    sccs = g2.kosaraju()
    print("Strongly Connected Components:", sccs)
