# swea_1954_달팽이숫자 문제풀이
# 2022-08-09

T = int(input())

for t in range(T): 
    N = int(input())
    board = [[0]*N for i in range(N)]
    number = 1
    a = 0
    while True:
        for i in range(a, N-a-1):
            board[a][i] = number
            number += 1

        for i in range(a, N-a-1):
            board[i][N-a-1] = number
            number += 1
            
        for i in range(N-a-1, a, -1):
            board[N-a-1][i] = number
            number += 1
            
        for i in range(N-a-1, a, -1):
            board[i][a] = number
            number += 1
        if number > N**2:
            break
        elif number == N**2:
            board[N//2][N//2] = number
            break
        
        a += 1
    
    print('#{0}'.format(t+1))
    for i in range(N):
        for j in range(N):
            print(board[i][j], end = ' ')
        print()