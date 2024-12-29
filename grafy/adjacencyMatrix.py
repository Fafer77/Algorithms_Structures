class Graph:
    def __init__(self, n) -> None:
        self.V = n
        self.adjacencyMatrix = [[0 for _ in range(n)] for _ in range(n)]
    
    def add_edge(self, v1, v2):
        self.adjacencyMatrix[v1][v2] = 1
    
    def delete_edge(self, v1, v2):
        self.adjacencyMatrix[v1][v2] = 0

    