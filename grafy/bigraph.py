from collections import deque, defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.adjacency_list = defaultdict(list)
    
    def add_edge(self, v, u):
        self.adjacency_list[v].append(u)
        self.adjacency_list[u].append(v)
    
    def bigraph(self):
        color = [0] * self.V
        queue = deque()
        for v in range(self.V):
            if color[v] == 0:
                color[v] = 1
                queue.append(v)
                while queue:
                    u = queue.pop()
                    for w in self.adjacency_list[u]:
                        if color[w] == color[u]:
                            return False
                        if color[w] == 0:
                            color[w] = -color[u]
                            queue.append(w)
        return True

def test_bigraph():
    # Graf dwudzielny
    g1 = Graph(4)
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(2, 3)
    g1.add_edge(3, 0)
    print("Graf 1 (dwudzielny):", g1.bigraph())  # Powinno zwrócić True

    # Graf niedwudzielny (cykl nieparzysty)
    g2 = Graph(5)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    g2.add_edge(3, 4)
    g2.add_edge(4, 0)
    print("Graf 2 (niedwudzielny):", g2.bigraph())  # Powinno zwrócić False

test_bigraph()

