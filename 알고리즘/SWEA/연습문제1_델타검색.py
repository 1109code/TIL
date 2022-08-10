# 연습문제1_델타검색 문제풀이
# 2022-08-10

T = int(input())
for t in range(T):
    N = int(input())
    board = []
    for i in range(N):
        board.append(list(map(int,input().split())))

    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]

    sum = 0

    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    sub = board[i][j] - board[ni][nj]
                    if sub >= 0:
                        sum += sub
                    else:
                        sum += -sub
    print('#{0} {1}'.format(t+1, sum))