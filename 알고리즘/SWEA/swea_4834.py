# swea_4834_숫자카드 문제풀이
# 2022-08-09

T = int(input())

for t in range(T):
    N = int(input())
    board = [0 for i in range(10)]
    ai = int(input())
    for i in range(N):
        board[ai%10] += 1
        ai = ai//10

    max_cnt = 0
    max_idx = 9
    for i in range(9, -1, -1):
        if board[i] > max_cnt:
            max_cnt = board[i]
            max_idx = i
    
    print(f'#{t+1} {max_idx} {max_cnt}')