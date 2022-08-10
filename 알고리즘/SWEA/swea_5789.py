# swea_5789_현주의상자바꾸기 문제풀이
# 2022-08-09

T = int(input())
for t in range(T):
    N, Q = map(int, input().split())
    board = [0 for i in range(N)]
    
    for q in range(Q):
        L, R = map(int, input().split())
        for i in range(L, R+1):
            board[i-1] = q+1
    board = [str(i) for i in board]
    
    print('#{0}'.format(t+1), end=' ')
    print('{0}'.format(' '.join(board)))