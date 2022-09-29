def dijkstra(N, X, adj, d):
    for i in range(N):
        d[i] = adj[X][i]
    visited[X] = True
    for _ in range(N):
        w = float('inf')
        for i in range(N):
            if not visited[i] and d[i] < w:
                target = i
                w = d[i]
        visited[target] = True
        for v in range(N):
            if 0 < adj[target][v] < float('inf'):
                d[v] = min(d[v], d[target] + adj[target][v])
    return


T = int(input())
for tc in range(1, T + 1):
    # N : 끝번호
    N, E = map(int, input().split())
    # 정점의 개수 v
    V = N + 1
    adj = [[float('inf')] * V for _ in range(V)]
    for i in range(V):
        adj[i][i] = 0
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w
    visited = [False] * V
    dout = [0] * V
    dijkstra(V, 0, adj, dout)
    print('#{} {}' .format(tc, dout[-1]))