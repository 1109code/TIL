# swea_1859 백만 장자 프로젝트 문제풀이
# 2022-08-16

T = int(input())

for t in range(T):
    N = int(input())
    
    # 백만 장자 판
    board = list(map(int, input().split()))

    result = 0
    
    # 총 일 다 돌면서
    for i in range(N):
        after_max = 0
        
        # 현재 이후 최대값 찾기
        for j in range(i+1, N):
            if board[j] > after_max:
                after_max = board[j]
        
        # 현재 이후 최대값에서 현재 값 빼서 가산하기
        if after_max > board[i]:
            result += (after_max - board[i])

    print('#{0} {1}'.format(t+1, result))

    # price_min = 10000

    # profit = 0
    # for price in board:
    #     if price < price_min:
    #         price_min = price
    #     if price - price_min > profit:
    #         profit = price - price_min
    # print(profit)