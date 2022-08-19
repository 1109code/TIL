# swea_5356 의석이의 세로로 말해요 문제풀이
# 2022-08-16

T = int(input())
for t in range(T):
    board = []
    max = 0
    # 길이 5 동안
    for i in range(5):
        board.append(input())
        # board 최대 값
        if len(board[i]) > max:
            max = len(board[i])

    print('#{} '.format(t+1), end = '')
    
    # board 최대값 까지
    for i in range(max):
        # 세로로
        for j in range(5):
            # 해당 j 의 길이가 범위에 있으면 프린트
            if len(board[j]) - 1 >= i:
                print(board[j][i], end = '')
            # 없으면 넘어가기
            else:
                pass
    print('')