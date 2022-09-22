# swea_5201 컨테이너 운반 문제풀이
# 2022-09-22

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    weight = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    weight.sort()
    trucks.sort()

    max_sum = 0

    flag = 0
    for i in range(M-1, -1, -1):
        for j in range(N-1, -1, -1):
            if trucks[i] >= weight[j]:
                max_sum += weight[j]
                weight[j] = 51
                flag = 1
                break

    print(f'#{tc} {max_sum}')