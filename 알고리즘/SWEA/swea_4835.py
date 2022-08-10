# 4835_구간합 문제풀이
# 2022-08-09
# import sys
# sys.stdin = open('swea_4835_input.txt', 'r')

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    board = list(map(int, input().split()))
    max = 0
    min = 10000*N
    
    
    for i in range(N-M+1):
        sum = 0
        for j in range(M):
            sum += board[i+j]
        if sum > max:
            max = sum
        if sum < min:
            min = sum

    print(f'#{t+1} {max-min}')