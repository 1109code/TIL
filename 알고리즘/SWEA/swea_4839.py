# swea_4839_이진탐색
# 2022-08-11

T = int(input())
for t in range(T):
    P, Pa, Pb = map(int, input().split())

    # A
    l = 1
    r = P
    c = 0
    cnt_a = 0
    while l <= r:
        c = int((l+r)/2)
        if c == Pa:
            break
        elif c > Pa:
            r = c
            cnt_a += 1
        elif c < Pa:
            l = c
            cnt_a += 1

    # B
    l = 1
    r = P
    c = 0
    cnt_b = 0  # 1 8 4.5 4 5
    while l <= r:
        c = int((l+r)/2)
        if c == Pb:
            break
        elif c > Pb:
            r = c
            cnt_b += 1
        elif c < Pb:
            l = c
            cnt_b += 1
    
    winner = []
    if cnt_a == cnt_b:
        winner = 0
    elif cnt_a < cnt_b:
        winner = 'A'
    else:
        winner = 'B'

    print('#{0} {1}'.format(t+1, winner))