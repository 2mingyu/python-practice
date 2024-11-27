# DFS를 이용한 미로 탐색
def dfs_maze(maze, start, end):
    stack = [start]
    visited = set()
    path = []
    
    while stack:
        current = stack.pop()
        if current == end:
            path.append(current)
            break
        if current not in visited:
            visited.add(current)
            path.append(current)
            neighbors = maze[current]
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return path

# 테스트
maze = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: [4],
    4: []
}
print("DFS 경로:", dfs_maze(maze, 0, 4))

# A* 알고리즘
from heapq import heappush, heappop

def a_star(graph, start, end, heuristic):
    open_set = []
    heappush(open_set, (0 + heuristic[start], 0, start))
    came_from = {}
    cost_so_far = {start: 0}
    
    while open_set:
        _, current_cost, current = heappop(open_set)
        
        if current == end:
            path = []
            while current is not None:
                path.append(current)
                current = came_from.get(current, None)
            return path[::-1]
        
        for neighbor, weight in graph[current].items():
            new_cost = current_cost + weight
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                heappush(open_set, (priority, new_cost, neighbor))
                came_from[neighbor] = current
    
    return []

# 테스트
graph = {
    0: {1: 1, 2: 4},
    1: {2: 2, 3: 5},
    2: {3: 1},
    3: {}
}
heuristic = {0: 7, 1: 6, 2: 2, 3: 0}  # 휴리스틱 값
print("A* 경로:", a_star(graph, 0, 3, heuristic))
