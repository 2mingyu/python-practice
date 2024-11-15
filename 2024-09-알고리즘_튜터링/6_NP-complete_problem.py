def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

# 테스트
values = [60, 100, 120]  # 아이템 가치
weights = [10, 20, 30]   # 아이템 무게
capacity = 50            # 배낭 용량
print("최대 가치:", knapsack(values, weights, capacity))

from itertools import permutations

def tsp(graph, start):
    nodes = list(range(len(graph)))
    nodes.remove(start)
    min_path_cost = float('inf')
    
    for perm in permutations(nodes):
        current_cost = 0
        k = start
        for i in perm:
            current_cost += graph[k][i]
            k = i
        current_cost += graph[k][start]  # 돌아오는 비용
        min_path_cost = min(min_path_cost, current_cost)
    
    return min_path_cost

# 테스트
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
start = 0
print("최소 비용 경로:", tsp(graph, start))
