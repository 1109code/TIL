# swea_2819 격자판의 숫자 이어 붙이기 문제풀이
# 2022-09-21
def search(n, m):
    global now, answer, check

    if len(check) == 7:
        if check in answer:
            return
        answer.append(check)
        return

    check += str(board[n][m])

    for di, dj in d:
        if 0 <= n + di < 4 and 0 <= m + dj < 4:
            search(n + di, m + dj)
            check = check[0:-1]


T = int(input())

d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for t in range(T):
    check = ''
    answer = []
    now = 0
    board = []
    for i in range(4):
        board.append(list(map(int, input().split())))

    for i in range(4):
        for j in range(4):
            search(i, j)

    print(f'#{t+1} {len(answer)}')