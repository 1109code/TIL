# swea_5174 subtree 문제풀이
# 2022-09-15

def ch_cnt(n):
    global cnt
    if n:
        ch_cnt(ch1[n])
        ch_cnt(ch2[n])
        cnt += 1


T = int(input())
for t in range(T):
    cnt = 0
    E, N = map(int, input().split())
    ch1 = [0 for _ in range(E + 2)]
    ch2 = [0 for _ in range(E + 2)]
    info = list(map(int, input().split()))

    for e in range(0, E * 2, 2):
        if ch1[info[e]] == 0:
            ch1[info[e]] = info[e + 1]
        else:
            ch2[info[e]] = info[e + 1]

    ch_cnt(N)
    print('#{0} {1}'.format(t+1, cnt))

