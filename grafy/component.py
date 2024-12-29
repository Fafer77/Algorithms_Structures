class Graph():
    def __init__(self, n):
        self.adjacency_list = [[] for _ in range(n)]
        self.n = n

    def add_edge(self, v, u):
        self.adjacency_list[v].append(u)
        self.adjacency_list[u].append(v)
    
    def delete_edge(self, v, u):
        if u in self.adjacency_list[v]:
            self.adjacency_list[v].remove(u)
            self.adjacency_list[u].remove(v)

    def connected_components(self):
        component = [0] * self.n
        cn = 0
        stack = []

        for i in range(self.n):
            if component[i] > 0:
                continue
            cn = cn + 1
            stack.append(i)
            component[i] = cn

            while stack:
                v = stack.pop()
                for u in self.adjacency_list[v]:
                    if component[u] > 0:
                        continue
                    stack.append(u)
                    component[u] = cn

        print(f'Number of connected components: {cn}')
        for i in range(cn):
            print(f'component {i + 1}: ', end=None)
            for j in range(self.n):
                if component[j] == (i + 1):
                    print(f'{j} ', end=None)

g = Graph(17)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(1, 2)
g.add_edge(1, 14)
g.add_edge(14, 13)
g.add_edge(14, 16)
g.add_edge(13, 16)
g.add_edge(9, 5)
g.add_edge(5, 6)
g.add_edge(6, 8)
g.add_edge(6, 7)
g.add_edge(4, 11)
g.add_edge(11, 15)
g.add_edge(15, 10)
g.add_edge(15, 12)
g.add_edge(12, 4)

g.connected_components()
