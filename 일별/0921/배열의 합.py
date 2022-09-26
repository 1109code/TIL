def f(i, k):
    global minV
    if i == k:
        s = 0
        for l in range(k):
            s += arr[l][p[l]]
        if minV > s:
            minV = s

    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            f(i+1, k)
            p[i], p[j] = p[j], p[i]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [i for i in range(N)]
    minV = N * 10
    f(0, N)
    print(f'#{tc} {minV}')