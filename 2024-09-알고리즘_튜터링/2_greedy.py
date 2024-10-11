# 동전 거스름돈 문제
def coin_change(coins, amount):
    coins.sort(reverse=True)  # 큰 단위 동전부터 사용
    count = 0
    for coin in coins:
        count += amount // coin
        amount %= coin
    return count

# 최소 신장 트리 (Kruskal 알고리즘)
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX

def kruskal(n, edges):
    uf = UnionFind(n)
    edges.sort(key=lambda x: x[2])  # 가중치로 정렬
    mst_cost = 0
    mst_edges = []
    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_cost += weight
            mst_edges.append((u, v))
    return mst_cost, mst_edges

# 최단 경로 문제 (다익스트라 알고리즘)
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]  # 우선순위 큐

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# 부분 배낭 문제 (Fractional Knapsack Problem)
def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)  # 가치/무게 비율로 정렬
    total_value = 0
    for weight, value in items:
        if capacity - weight >= 0:
            total_value += value
            capacity -= weight
        else:
            total_value += value * (capacity / weight)
            break
    return total_value

# 집합 커버 문제 (Set Cover Problem)
def set_cover(universe, subsets):
    covered = set()
    cover = []
    while covered != universe:
        subset = max(subsets, key=lambda s: len(s - covered))
        cover.append(subset)
        covered |= subset
    return cover

# 작업 스케줄링 문제 (Task Scheduling Problem)
def task_scheduling(tasks):
    tasks.sort(key=lambda x: x[1])  # 종료 시간을 기준으로 정렬
    schedule = []
    last_end_time = 0
    for start, end in tasks:
        if start >= last_end_time:
            schedule.append((start, end))
            last_end_time = end
    return schedule


# -------------------------------
# 각 알고리즘 실행 예시
# -------------------------------

# 동전 거스름돈 문제 실행 예시
coins = [500, 100, 50, 10]
amount = 1260
print("동전 거스름돈: ", coin_change(coins, amount))

# 최소 신장 트리 (Kruskal 알고리즘) 실행 예시
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
n = 4
print("최소 신장 트리: ", kruskal(n, edges))

# 다익스트라 알고리즘 실행 예시
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
print("최단 경로: ", dijkstra(graph, 'A'))

# 부분 배낭 문제 실행 예시
items = [(10, 60), (20, 100), (30, 120)]
capacity = 50
print("부분 배낭 문제: ", fractional_knapsack(items, capacity))

# 집합 커버 문제 실행 예시
universe = {1, 2, 3, 4, 5}
subsets = [{1, 2, 3}, {2, 4}, {3, 5}, {4, 5}]
print("집합 커버 문제: ", set_cover(universe, subsets))

# 작업 스케줄링 문제 실행 예시
tasks = [(0, 6), (1, 4), (3, 5), (3, 8), (4, 7), (5, 9), (6, 10), (8, 11)]
print("작업 스케줄링: ", task_scheduling(tasks))
