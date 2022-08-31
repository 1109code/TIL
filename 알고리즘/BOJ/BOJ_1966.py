# BOJ_1966 프린터 큐
# 2022-08-28

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    idx = []
    for i in range(N):
        idx.append(i)

    cnt = 0
    while 1:
        if numbers[idx[0]] >= max(numbers):
            numbers[idx[0]] = 0
            cnt += 1
            if idx[0] == M:
                print(cnt)
                break
            idx.pop(0)

        else:
            idx.append(idx.pop(0))