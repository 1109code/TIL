# swea_6485_삼성시의버스노선
# 2022-08-09

T = int(input())
for t in range(T):
    N = int(input())
    A = [0 for i in range(N)]
    B = [0 for i in range(N)]
    
    board = [0 for i in range(5000)]
    
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    for i in range(N):
        for j in range(A[i]-1, B[i]):
            board[j] += 1

    P = int(input())

    print('#{0}'.format(t+1), end = ' ')
    for i in range(P):
        print(board[int(input())-1], end=' ')
    print()