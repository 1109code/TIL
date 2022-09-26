# swea_2819 격자판의 숫자 이어 붙이기 문제풀이
# 2022-09-21
def search(n, m):
    global now, answer, check

    if now == 7:
        answer.add(''.join(check))
        return

    check[now] = board[n][m]
    for di, dj in d:
        if 0 <= n + di < 4 and 0 <= m + dj < 4:
            now += 1
            search(n + di, m + dj)
            now -= 1


T = int(input())

d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for t in range(T):
    check = [0 for _ in range(7)]
    answer = set()
    now = 0
    board = []
    for i in range(4):
        board.append(list(input().split()))

    for i in range(4):
        for j in range(4):
            check[0] = board[i][j]
            search(i, j)

    print(f'#{t+1} {len(answer)}')