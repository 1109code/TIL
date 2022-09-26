# swea_2117 홈 방범 서비스 문제풀이
# 2022-09-23
def profit(n, m, k_max):
    global max_cnt

    for k in range(1, k_max + 1):
        cur_profit = -(k * k + (k - 1) * (k - 1))
        cnt = 0
        for p in range(-k + 1, k):
            for q in range(-k + 1 + abs(p), k - abs(p)):
                if 0 <= n + q < N and 0 <= m + p < N and houses[n + q][m + p] != 0:
                    cnt += 1
                    cur_profit += houses[n + q][m + p] * M

        if cur_profit >= 0:
            if cnt >= max_cnt:
                max_cnt = cnt


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    houses = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0

    for i in range(N):
        for j in range(N):
            profit(i, j, N + 1)

    print(f'#{tc} {max_cnt}')

