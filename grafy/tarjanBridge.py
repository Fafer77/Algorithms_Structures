def dfs_tarjan(adj, V, u, time, disc, parent, low, bridges):
    disc[u] = low[u] = time
    time += 1
    for v in adj[u]:
        if disc[v] == -1:
            parent[v] = u
            dfs_tarjan(adj, V, v, time, disc, parent, low, bridges)
            low[u] = min(low[u], low[v])
            if low[v] > disc[u]:
                bridges.append((u, v))
        elif v != parent[u]:
            low[u] = min(low[u], disc[v])


def find_bridges_tarjan(adj, V):
    disc = [-1] * V
    parent = [-1] * V
    low = [-1] * V
    bridges = []
    time = 0

    for i in range(V):
        if disc[i] == -1:
            dfs_tarjan(adj, V, i, time, disc, parent, low, bridges)

    for bridge in bridges:
        print(bridge[0], '->', bridge[1])

V = 5
adj = [[] for _ in range(V)]
adj[0].append(3)
adj[0].append(2)
adj[0].append(1)
adj[1].append(2)
adj[3].append(4)
adj[4].append(3)
adj[2].append(1)
adj[1].append(0)
adj[2].append(0)
adj[3].append(0)

find_bridges_tarjan(adj, V)


