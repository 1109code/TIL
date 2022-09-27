# swea_5208 전기버스2 문제풀이
# 2022-09-27
def charging(cur):
    global cnt_min, cnt
    if cnt > cnt_min:
        return

    if cur >= N-1:
        if cnt < cnt_min:
            cnt_min = cnt
        return

    cnt += 1
    for i in range(charger[cur]):
        charging(cur + charger[cur] - i)
    cnt -= 1


T = int(input())

for tc in range(1, T + 1):
    charger = list(map(int, input().split()))
    N = charger.pop(0)

    cnt = 0
    cnt_min = N
    charging(0)

    print(f'#{tc} {cnt_min - 1}')