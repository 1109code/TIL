# swea_5189 전자키트 문제풀이
# 2022-09-22
def permute(n, k):
    global P, offices, used, p_list
    if n == k:
        P.append(p_list[:])

    else:
        for i in range(k):
            if not used[i]:
                p_list[n] = offices[i]
                used[i] = True
                permute(n+1, k)
                used[i] = False

    return P


def energy_cost(order):
    energy_sum = 0
    start = 0

    for i in order:
        energy_sum += costs[start][i - 1]
        start = i - 1

    energy_sum += costs[start][0]

    return energy_sum


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 100 * (N ** 2)
    offices = [i for i in range(2, N + 1)]
    used = [False] * (N - 1)
    p_list = [0] * (N - 1)
    P = []
    visit_order = permute(0, len(offices))
    
    for visit in visit_order:

        cur_min = energy_cost(visit)

        if cur_min <= min_sum:
            min_sum = cur_min

    print(f'#{tc} {min_sum}')
