# swea_13994 문제풀이
# 2022-08-12

T = int(input())

for t in range(T):
    board = [0 for i in range(1000)]
    N = int(input())
    for i in range(N):
        type, A, B = map(int, input().split())
        if type == 1:
            for j in range(A, B+1):
                board[j-1] += 1
        
        elif type == 2:
            for j in range(A, B+1, 2):
                board[j-1] += 1

        else:
            if A % 2 == 0:
                for j in range(A, B+1):
                    if j % 4 == 0:
                        board[j-1] += 1
            else:
                for j in range(A, B+1):
                    if j % 3 == 0 and j % 10 != 0:
                        board[j-1] += 1
    max = 0
    for i in board:
        if i > max:
            max = i
    print('#{0} {1}'.format(t+1, max))