def bellman_ford(graph, source):
    dist = {vertex: float('inf') for vertex in graph}
    dist[source] = 0

    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

    for u in graph:
        for v, weight in graph[u].items():
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                raise ValueError('Graph contains negative weight cycle')

    return dist

graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}
source = 'A'

shortest_distances = bellman_ford(graph, source)
print(shortest_distances)
    