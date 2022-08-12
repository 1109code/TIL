# swea_12712 문제풀이
# 2022-08-12

T = int(input())

for t in range(T):
    N, M = map(int,input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    tot_max = 0
    # 십자가
    for i in range(N):
        for j in range(N):
            tot = 0
            for k in range(-M+1, M):
                if 0 <= i+k < N:
                    tot += board[i+k][j]
                if 0 <= j+k < N:
                    tot += board[i][j+k]

            if tot - board[i][j] > tot_max:
                tot_max = tot - board[i][j]

    # 크로스

    for i in range(N):
        for j in range(N):
            tot = 0
            for k in range(-M+1, M):
                if 0 <= i+k < N and 0 <= j+k < N:
                    tot += board[i+k][j+k]
                if 0 <= i+k < N and 0 <= j-k < N:
                    tot += board[i+k][j-k]
            
            if tot - board[i][j] > tot_max:
                tot_max = tot - board[i][j]

    print('#{0} {1}'.format(t+1, tot_max))