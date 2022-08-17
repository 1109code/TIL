# swea_1979_어디에단어가들어갈수있을까 문제풀이
# 2022-08-11

T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    board = []
    c = [0 for i in range(15)]

    for j in range(N):
        board.append(list(map(int,input().split())))

    for k in range(N):
        count = 1
        for l in range (N-1):
            if board[k][l] == 1 and board[k][l+1]== 1:
                count += 1
                if l == N-2:
                    c[count-1]+=1
            elif board[k][l] == 1 and board[k][l+1]==0:
                c[count-1]+=1
                count = 1
                
    for k in range(N):
        count = 1
        for l in range (N-1):
            if board[l][k] == 1 and board[l+1][k]== 1:
                count += 1
                if l == N-2:
                    c[count-1]+=1
            elif board[l][k] == 1 and board[l+1][k]==0:
                c[count-1]+=1
                count = 1
    print('#%d %d' %((i+1), c[K-1]))
