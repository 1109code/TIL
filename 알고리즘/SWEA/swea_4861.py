# swea_4861 문제풀이
# 2022-08-16

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    test = []
    

    for i in range(N):
        for j in range(N - M + 1):
            for k in range(M):
                test.append(board[i][j+k])
            if test[::] == test[::-1]:
                print('#{0} {1}'.format(t+1, ''.join(test)))
            test = []
    
    for j in range(N):
        for i in range(N - M + 1):
            for k in range(M):
                test.append(board[i+k][j])
            if test[::] == test[::-1]:
                print('#{0} {1}'.format(t+1, ''.join(test)))
            test = []