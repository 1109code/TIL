# swea_5789 현주의 상자 바꾸기
# 2022-08-16

T = int(input())

for t in range(T):
    N, Q = map(int, input().split())

    board = [0 for i in range(N)]

    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            board[j-1] = i
    
    print('#{} '.format(t+1), end = '')
    for i in range(len(board)):
        print(board[i], end = ' ')
    print('')