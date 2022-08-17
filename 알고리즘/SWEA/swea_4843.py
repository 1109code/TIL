# swea_4843.py_특별한정렬 문제풀이
# 2022-08-11

T = int(input())
for t in range(T):
    N = int(input())
    board = list(map(int, input().split()))
    # cnt_board = [0 for i in range(N)]
    # # 카운팅 정렬
    # for i in range(N):
    #     cnt_board[board[i]] += 1
    
    # while True:
    #     i = 0
    #     while True:
            
    #         if cnt_board[i] != 0:
    #             print(i)

    for i in range(N):
        min_idx = i
        for j in range(i+1, N):
            if board[min_idx] > board[j]:
                min_idx = j
        
        board[i], board[min_idx] = board[min_idx], board[i]
    
    print('#{}'.format(t+1), end = ' ')
    for i in range(5):
        print(board[N-i-1], end = ' ')
        print(board[i], end = ' ')
    print()