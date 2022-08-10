# swea_1208_flatten 문제풀이
# 2022-08-09

# 최대값 에서 하나 빼서
# 최소값에 하나 더하기
# dumping 횟수만큼 반복
def my_max(board):
    max = 0
    max_idx = 0
    for i, j in enumerate(board):
        if j > max:
            max = j
            max_idx = i
    return max, max_idx

def my_min(board):
    min = 100
    min_idx = 0
    for i, j in enumerate(board):
        if j < min:
            min = j
            min_idx = i
    return min, min_idx

for t in range(10):
    dump = int(input())
    board = list(map(int, input().split()))
    
    while dump!=0:
        max_idx = my_max(board)[1]
        min_idx = my_min(board)[1]
        board[max_idx] -= 1
        board[min_idx] += 1
        dump -= 1

    print(f'#{t+1} {my_max(board)[0] - my_min(board)[0]}')