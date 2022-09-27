def npr(i, k, r):                                   # p[i]부터 p[r]까지를 a[0]~a[k]의 순열로 채움
    global max_cnt, cnt
    if i == r:                                      # 순열이 완성되었으면 p는 [0, 1, 2, 3, 4]의 형태.
        if cnt >= max_cnt:
            max_cnt = cnt
        else:
            return

    elif cnt < max_cnt:
        return

    else:                                           # 완성이 아직 안되었으면 순열만들기
        for j in range(k):                          # 순회하기
            if used[j] == 0:                        # 쓴적없는 숫자면
                used[j] = 1                         # 썼다는 표시 후
                p[i] = a[j]                         # i번째 자리는 a[j]로 채움
                cnt *= arr[i][p[i]] / 100
                print(used)

                npr(i+1, k, r)                      # 다음자리 채우러가기

                used[j] = 0                         # 다음차례를 위해 원상복귀


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        arr.append(tmp)

    used = [0]*N
    a = list(range(0, N))
    p = [0] * N  # 0~N-1번 인덱스 존재
    max_cnt = 0
    cnt = 1
    npr(0, N, N)  # p[0], p[N]은 0으로 고정, p[1]~p[N-1]을 순열로 채움

    print('#{} {}'.format(tc, max_cnt))