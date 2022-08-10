# swea_1209 sum 문제풀이
# 2022-08-10

for t in range(10):
    T = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    sum_max = 0
    
    
    for i in range(100):
        # 가로 합
        sum = 0
        cross_right = 0
        for j in range(100):
            sum += board[i][j]
            if i == j:
                cross_right += board[i][j]
        if sum > sum_max:
            sum_max = sum
        # 세로 합
        sum = 0
        cross_left = 0
        for j in range(100):
            sum += board[j][i]
            if j == 99-i:
                cross_left += board[i][j]
        if sum > sum_max:
            sum_max = sum

    if cross_right > sum_max:
        sum_max = cross_right
    if cross_left > sum_max:
        sum_max = cross_left

    print('#{0} {1}'.format(t+1, sum_max))