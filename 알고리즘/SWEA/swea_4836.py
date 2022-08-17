# swea_4836_색칠하기 문제풀이
# 2022-08-11

T = int(input())

for t in range (T):
    board = [list(0 for i in range(10)) for _ in range(10)]
    N = int(input())

    color = []
    cnt = 0

    for i in range(N):
        color.append(list(map(int, input().split())))
    
    red = []
    blue = []
    for k in range(N):
        if color[k][-1] == 1:
            for i in range(color[k][0], color[k][2]+1):
                for j in range(color[k][1], color[k][3]+1):
                    board[i][j] = 1
    
    for k in range(N):
        if color[k][-1] == 2:
            for i in range(color[k][0], color[k][2]+1):
                for j in range(color[k][1], color[k][3]+1):
                    if board[i][j] == 1:
                        cnt += 1
                        board[i][j] = 0
    
    print('#{0} {1}'.format(t+1, cnt))