# BOJ_15553 난로 문제풀이
# 2022-08-16

N, K = map(int, input().split())

board = []
    
for m in range(N):
    board.append(int(input()))

sub_board = []
for i in range(N-1):
    sub_board.append(board[i+1]-board[i])

sorted_sub = sorted(sub_board)

day = board[-1] - board[0] + 1
for i in range(K-1):
    day -= (sorted_sub[len(sorted_sub) - i -1] - 1)

print(day)
    # min_day = board[-1] - board[0]
    # min_idx = 0
    # for i in range(N-1):
    #     if min_day > sub_board[i]:
    #         min_day = sub_board[i]
    #         min_idx = i
    