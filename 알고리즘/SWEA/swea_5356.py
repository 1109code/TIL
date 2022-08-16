# swea_5356 의석이의 세로로 말해요 문제풀이
# 2022-08-16

T = int(input())
for t in range(T):
    board = []
    max = 0
    for i in range(5):
        board.append(input())
        if len(board[i]) > max:
            max = len(board[i])

    print('#{} '.format(t+1), end = '')
    for i in range(max):
        for j in range(5):
            if len(board[j]) - 1 >= i:
                print(board[j][i], end = '')
            else:
                pass
    print('')