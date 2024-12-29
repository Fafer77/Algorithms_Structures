from collections import deque, defaultdict

def find_centers(n, edges):
    if n == 0:
        return []
    elif n == 1:
        return [0]

    adj_list = defaultdict(list)
    degrees = [0] * n
    for v, u in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
        degrees[u] += 1
        degrees[v] += 1

    queue = deque()
    for i in range(n):
        if degrees[i] == 1:
            queue.append(i)

    left = n
    while left > 2:
        leaves = len(queue)
        left -= leaves
        for _ in range(leaves):
            leaf = queue.popleft()
            for neighbor in adj_list[leaf]:
                degrees[neighbor] -= 1
                if degrees[neighbor] == 1:
                    queue.append(neighbor)

    return list(queue)

n = 5
edges = [(0, 1), (1, 2), (2, 3), (3, 4)]
n1 = 9
edges1 = [(0, 5), (0, 6), (0, 8), (0, 3), (6, 7), (3, 2), (2, 1), (2, 4)]
print(find_centers(n1, edges1))
