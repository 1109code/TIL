# 4828_min-max 문제풀이
# 2022-08-09
# import sys
# sys.stdin = open('swea_4828_input.txt' , 'r')
T = int(input())

for k in range(T):
    N = int(input())
    
    ai = list(map(int, input().split()))

    max = ai[0]
    min = ai[0]
    for i in range(1, N):
        if ai[i] > max:
            max = ai[i]
        if ai[i] < min:
            min = ai[i]

    print(f'#{k+1} {max-min}')