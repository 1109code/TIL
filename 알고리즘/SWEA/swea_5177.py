# swea_5177 이진 힙 문제풀이
# 2022-09-15

T = int(input())
for t in range(T):
    N = int(input())

    answer = [0 for _ in range(N + 1)]
    ch1 = [0 for _ in range(N + 1)]
    ch2 = [0 for _ in range(N + 1)]
    par = [0 for _ in range(N + 1)]

    for i in range(1, N + 1):
        if i % 2 == 0:
            ch1[i // 2] = i
        else:
            ch2[i // 2] = i
    nums = list(map(int, input().split()))
    cnt = 1
    for i in nums:
        answer[cnt] = i
        now = cnt
        while answer[now] < answer[now//2] and now != 1:
            answer[now], answer[now//2] = answer[now//2], answer[now]
            now = now // 2
        cnt += 1

    ans_sum = 0
    N = N // 2
    while N >= 1:
        ans_sum += answer[N]
        N = N // 2

    print('#{0} {1}'.format(t+1, ans_sum))