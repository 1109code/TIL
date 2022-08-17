# swea_4837_부분집합의 합
# 2022-08-11

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    
    result = 0
    for i in range(1<<12):
        cnt = 0
        total = 0

        for j in range(12):
            if i & (1<<j):
                cnt += 1
                total += A[j]

        if total == K and cnt == N:
            result += 1
    
    print('#{0} {1}'.format(t+1, result))