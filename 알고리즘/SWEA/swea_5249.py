# swea_5249 최소 신장 트리 문제풀이
# 2022-09-30
from collections import defaultdict

def dij():
    for i in range(V):
        for e, w in grid[i]:
            dist[e] = min(dist[e], w + dist[i])


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    grid = defaultdict(list)
    dist = [float('inf')] * (V + 1)
    dist[0] = 0
    for _ in range(E):
        s, e, w = map(int, input().split())
        grid[s].append((e, w))
    dij()
    answer = dist[-1]
    print(answer)

