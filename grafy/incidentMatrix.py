class Graph():
    def __init__(self, n):
        self.V = n
        self.incidentMatrix = [[] for _ in range(n)]

    def add_edge(self, v, u):
        for i in range(self.V):
            self.incidentMatrix[i].append(0)
            
        self.incidentMatrix[v][-1] = 1
        self.incidentMatrix[u][-1] = -1
    
    def delete_edge(self, v, u):
        for edge in range(len(self.incidentMatrix[0])):
            if self.incidentMatrix[v][edge] == 1 and self.incidentMatrix[u][edge] == -1:
                for i in range(self.V):
                    self.incidentMatrix[i].pop(edge)
                break

    def display_matrix(self):
        for row in self.incidentMatrix:
            print(row)

    def transpose(self):
        for v in range(self.V):
            for edge in range(len(self.incidentMatrix[v])):
                self.incidentMatrix[v][edge] *= -1



g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)

print("Macierz przed usunięciem:")
g.display_matrix()

g.delete_edge(1, 2)
print("\nMacierz po usunięciu krawędzi (1, 2):")
g.display_matrix()

print("\nPo Transpozycji:")
g.transpose()
g.display_matrix()