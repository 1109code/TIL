# swea_5202 화물 도크 문제풀이
# 2022-09-22

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    register = []
    for n in range(N):
        register.append(list(map(int, input().split())))
        register.sort(key=lambda x: (x[1]))

    cur_end = register[0][1]
    cnt = 1
    for i in range(1, len(register)):
        if register[i][0] >= cur_end:
            cnt += 1
            cur_end = register[i][1]

    print(f'#{tc} {cnt}')