# 연습문제2_부분집합_문제풀이
# 2022-08-10

T = int(input())

for t in range(T):
    arr = list(map(int, input().split()))

    n = len(arr)
    cnt = -1

    for i in range(1<<n):
        sum = 0
        for j in range(n):
            if i & (1<<j):
                sum += arr[j]
        if sum == 0:
            cnt += 1
    if cnt > 0:
        print('#{} 1'.format(t+1))
    else:
        print('#{} 0'.format(t+1))