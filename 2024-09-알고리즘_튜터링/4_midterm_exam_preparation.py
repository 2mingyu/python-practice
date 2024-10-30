# 그리디 알고리즘을 사용한 동전 거스름돈 문제
def coin_change(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if amount == 0:
            break
        count += amount // coin
        amount %= coin
    return count if amount == 0 else -1

# 동전 거스름돈 문제 예시
coins = [1, 5, 10, 25]
amount = 63
print(f"Coins needed: {coin_change(coins, amount)}")

import heapq

# 다익스트라 알고리즘
def dijkstra(graph, start):
    # 최단 거리 테이블
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# 그래프 예시
graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3},
    'E': {'C': 8, 'D': 3}
}

start_node = 'A'
print(f"Shortest distances from {start_node}: {dijkstra(graph, start_node)}")

