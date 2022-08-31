# IM 대비 swea_12712 파리퇴치3 문제풀이
# 2022-08-26

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

# 상하 / 대각 델타
    dp = [[0, 1], [1, 1]]
    sum_max = 0

    for i in range(N):
        for j in range(N):

            for d in dp:
                total = 0
                # 분사 길이만큼
                for k in range(-M + 1, M):
                    # 좌우, 우하 대각
                    if 0 <= i + d[0] * k < N and 0 <= j + d[1] * k < N:
                        total += board[i + d[0] * k][j + d[1] * k]
                    # 상하, 우상 대각
                    # 어차피 d[0] 는 0 이므로 상하일 때 -1 을 곱해도 상관 없음
                    # 우상일때만 영향을 줌
                    if 0 <= i + d[1] * k < N and 0 <= j + d[0] * (-1) * k < N:
                        total += board[i + d[1] * k][j + d[0] * (-1) * k]

                if total - board[i][j] > sum_max:
                    sum_max = total - board[i][j]

    print('#{} {}'.format(t+1, sum_max))