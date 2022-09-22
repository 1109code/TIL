# swea_5203 베이비진 게임 문제푸링
# 2022-09-22
def baby_gin(p, n):
    global r_t

    for i in range(10):
        if p[i] >= 3:
            p[i] -= 3
            r_t[n][1] += 1
        if p[i] >= 1 and p[i + 1] >= 1 and p[i + 2] >= 1:
            p[i] -= 1
            p[i + 1] -= 1
            p[i + 2] -= 1
            r_t[n][0] += 1


T = int(input())

for tc in range(1, T + 1):
    p1 = [0] * 12
    p2 = [0] * 12
    r_t = [[0, 0], [0, 0]]
    numbers = list(map(int, input().split()))
    for i in range(0, 12, 2):
        p1[numbers[i]] += 1
        p2[numbers[i+1]] += 1

        baby_gin(p1, 0)
        if sum(r_t[0]) >= 1:
            print(f'#{tc} 1')
            break

        baby_gin(p2, 1)
        if sum(r_t[1]) >= 1:
            print(f'#{tc} 2')
            break

    if sum(r_t[0]) + sum(r_t[1]) == 0:
        print(f'#{tc} 0')