# swea_9386 연속한 1의 개수
# 2022-08-12

T = int(input())

for t in range(T):
    N = int(input())
    board = input()

    i = 0
    cnt = 0
    my_max = 0
    while True:
        if board[i] == '1':
            cnt += 1
            if cnt > my_max:
                my_max = cnt
        else:
            cnt = 0
        i += 1
        if i == len(board):
            break

    print('#{0} {1}'.format(t+1, my_max))