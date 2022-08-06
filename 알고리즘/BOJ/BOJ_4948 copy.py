while True:
    N= int(input())
    board = []
    if N == 0:
        break
    
    for i in range(N+1, 2*N+1):
        board.append(i)
    for j in range(2, N+1):
        for k in range((N+1)//j, (2*N)//j+1):
            if k*j in board:
                board.remove(k*j)
    print(len(board))
