# swea_1861 정사각형 방 문제풀이
# 2022-09-16
def dfs(pos1, pos2):
    global d
    global cnt
    global cnt_max

    for di, dj in d:
        if 0 <= pos1 + di < N and 0 <= pos2 + dj < N and board[pos1][pos2] + 1 == board[pos1 + di][pos2 + dj]:
            cnt += 1
            if cnt > cnt_max:
                cnt_max = cnt
            dfs(pos1 + di, pos2 + dj)
            cnt -= 1



T = int(input())

for t in range(T):
    N = int(input())
    board = []
    for n in range(N):
        board.append(list(map(int, input().split())))

    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    ans_max = 0
    for i in range(N):
        for j in range(N):
            cnt = 1
            cnt_max = 1
            dfs(i, j)
            if cnt_max > ans_max:
                ans_max = cnt_max
                x, y = i, j
            elif cnt_max == ans_max:
                if board[x][y] >= board[i][j]:
                    x, y = i, j
    print('#{0} {1} {2}'.format(t+1, board[x][y], ans_max))