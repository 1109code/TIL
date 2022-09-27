# swea_5208 전기버스2 문제풀이
# 2022-09-27
def charging(cur):
    global cnt

    if cur >= N:
        return

    cur_max = 0
    max_idx = 0
    cnt += 1

    for i in range(cur + 1, cur + charger[cur] + 1):
        if i >= N - 1:
            return

        if charger[i] > cur_max:
            cur_max = charger[i]
            max_idx = i

    charging(max_idx)


T = int(input())

for tc in range(1, T + 1):
    charger = list(map(int, input().split()))
    N = charger.pop(0)

    cnt = 0
    charging(0)
    print(f'#{tc} {cnt-1}')