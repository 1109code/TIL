# swea_5251 최소 이동 거리 문제풀이
# 2022-09-29
def dij(N, X, adj, d):
    for i in range(N):
        d[i] = adj[X][i]
    d[0] = 1000000

    U = [X]
    for _ in range(N):
        w = 0
        for i in range(N):
            if (i not in U) and d[i] < d[w]:
                w = i

        U.append(w)
        for v in range(N):
            if 0 < adj[w][v] < 1000000:
                d[v] = min(d[v], d[w] + adj[w][v])
    return

T = int(input())

for tc in range(1, T + 1):
    N, E = map(int, input().split())

    info = [list(map(int, input().split())) for _ in range(E)]

    adj1 = [[1000000] * (N + 1) for _ in range(N + 1)]

    for i in range(N+1):
        adj1[i][i] = 0

    for i in range(E):
        adj1[info[i][0]][info[i][1]] = info[i][2]

    dout = [1000000] * (N + 1)
    dij(N + 1, 0, adj1, dout)
    print(f'#{tc} {dout[-1]}')