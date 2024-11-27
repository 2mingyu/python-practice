# 2-근사 알고리즘 예제: 최소 간선 커버
def vertex_cover(graph):
    visited = set()
    cover = set()
    
    for u, neighbors in enumerate(graph):
        for v in neighbors:
            if u not in visited and v not in visited:
                cover.add(u)
                cover.add(v)
                visited.add(u)
                visited.add(v)
                break
    
    return cover

# 테스트
graph = [
    [1, 2],
    [0, 2, 3],
    [0, 1, 3],
    [1, 2]
]
print("근사 최소 간선 커버:", vertex_cover(graph))
