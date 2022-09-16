# swea_5699 세제곱근을 찾아라 문제풀이
# 2022-09-16

T = int(input())

for t in range(T):
    N = int(input())
    if N == 1:
        answer = 1
    else:
        num = 1
        answer = -1
        while num ** 3 < N:
            num += 1
            if num ** 3 == N:
                answer = num

    print('#{0} {1}'.format(t+1, answer))