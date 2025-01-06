def knapsack(capacity, weights, values):
    if capacity < 0 or len(weights) != len(values):
        return
    
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        w = weights[i-1]
        v = values[i-1]

        for j in range(1, capacity + 1):
            # no picking element
            dp[i][j] = dp[i-1][j]

            # check if picking element is better
            if j >= w:
                dp[i][j] = max(dp[i][j], dp[i-1][j-w] + v)
    
    selected_items = []
    item_col = capacity
    for i in range(n, 0, -1):
        if dp[i][item_col] != dp[i-1][item_col]:
            selected_items.append(i-1)
            item_col -= weights[i-1]
    
    return dp[n][capacity], selected_items


capacity = 10
values = [1, 4, 8, 5]
weights = [3, 3, 5, 6]
print(knapsack(capacity, weights, values))

capacity = 50
profit = [60, 100, 120]
weight = [10, 20, 30]
n = len(profit)
print(knapsack(capacity, weight, profit))
