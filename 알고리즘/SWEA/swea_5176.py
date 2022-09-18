# swea_5176 이진탐색 문제풀이
# 2022-09-15

def order(n):
    global cnt
    if n:
        order(ch1[n])
        answer[n] = cnt
        cnt += 1
        order(ch2[n])


T = int(input())

for t in range(T):
    cnt = 1
    N = int(input())
    answer = [0 for _ in range(N + 1)]
    ch1 = [0 for _ in range(N + 1)]
    ch2 = [0 for _ in range(N + 1)]

    for i in range(1, N + 1):
        if i % 2 == 0:
            ch1[i//2] = i
        else:
            ch2[i//2] = i

    order(1)
    print('#{0} {1} {2}'.format(t+1, answer[1], answer[N//2]))