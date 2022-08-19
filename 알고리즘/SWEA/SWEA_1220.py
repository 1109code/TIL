# swea_2N00.py
# 문제풀이


for t in range(10):
    board = []
    stop = 0
    # 1은 N극
    # 2는 S극
    N = int(input())
    for i in range(N):
        board.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                for k in range(i+1, N):
                    if board[k][j] == 1:
                        break
                    elif board[k][j] == 2:
                        stop += 1
                        break
                    
    print('#{} {}'.format(t+1, stop))