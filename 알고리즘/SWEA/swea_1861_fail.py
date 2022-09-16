# swea_1861 정사각형 방 문제풀이
# 2022-09-16
def search(x, y):
    global cnt
    global cnt_max
    global max_idx

    for di, dj in d:
        if 0 <= x + di < N and 0 <= y + dj < N and board[x][y] + 1 == board[x + di][y + dj]:
            cnt += 1
            if cnt > cnt_max:
                cnt_max = cnt
            search(x + di, y + dj)
            cnt -= 1


T = int(input())

for t in range(T):
    N = int(input())
    board = []
    for n in range(N):
        board.append(list(map(int, input().split())))

    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    ans_idx = [0, 0]
    ans_max = 1
    cnt_max = 1

    for i in range(N):
        for j in range(N):
            cnt = 1

            search(i, j)

            if cnt_max >= ans_max and board[ans_idx[0]][ans_idx[1]] >= board[i][j]:
                ans_idx = [i, j]
                ans_max = cnt_max

    print('#{0} {1} {2}'.format(t+1, board[ans_idx[0]][ans_idx[1]], ans_max))
