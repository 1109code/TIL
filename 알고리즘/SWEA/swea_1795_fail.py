def dijkstra(N, X, adj, d):
    for i in range(N+1):
        d[i] = adj[X][i]

    U = [X]

    for _ in range(N-1):
        w = 0
        for i in range(1, N+1):
            if (i not in U) and d[i] < d[w]:
                w = i
        U.append(w)
        for v in range(1, N+1):
            if 0 < adj[w][v] < 1000000:
                d[v] = min(d[v], d[w] + adj[w][v])


T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    adj1 = [[1000000]*(N+1) for _ in range(N+1)]

    for i in range(N+1):
        adj1[i][i] = 0

    for _ in range(M):
        x, y, c = map(int, input().split())
        adj1[x][y] = c

    dout = [0] * (N+1)
    dijkstra(N, X, adj1, dout)

    max_len = 0

    for i in range(1, N + 1):
        dout2 = [0] * (N+1)
        dijkstra(N, i, adj1, dout2)
        cur_len = dout[i] + dout2[X]

        if cur_len > max_len:
            max_len = cur_len

    print(f'#{tc} {cur_len + dout[X]}')