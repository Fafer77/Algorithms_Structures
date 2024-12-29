def topological_sort_util(v, adj, stack, visited):
    visited[v] = True
    for u in adj[v]:
        if not visited[u]:
            topological_sort_util(u, adj, stack, visited)
    stack.append(v)

def topological_sort(adj, V):
    stack = []
    visited = [False] * V
    for v in range(V):
        if not visited[v]:
            topological_sort_util(v, adj, stack, visited)

    print('Topological sort result:', end=' ')
    while stack:
        print(stack.pop(), end=' ')


V = 4
edges = [[0, 1], [1, 2], [3, 1], [3, 2]]
adj = [[] for _ in range(V)]
for i in edges:
    adj[i[0]].append(i[1])

topological_sort(adj, V)
