# swea_1952 수영장 문제풀이
# 2022-09-23

T = int(input())

for tc in range(1, T + 1):
    costs = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    cost_daily = [0] * 14

    for i in range(12):
        if plan[i]:
            cost_daily[i] = costs[0]                 # 1일권으로 모두 구매하는 경우로 가격 초기화

    for i in range(12):
        if plan[i] != 0:
            if cost_daily[i] >= costs[1]/plan[i]:
                cost_daily[i] = costs[1]/plan[i]

    plan.extend([0, 0])
    for i in range(12):
        cost_sum = 0
        for j in range(3):
            cost_sum += cost_daily[i + j] * plan[i + j]

        if plan[i] + plan[i+1] + plan[i+2] != 0:
            if cost_sum >= costs[2]:
                for j in range(3):
                    cost_daily[i] = costs[2]/(plan[i] + plan[i+1] + plan[i+2])

    total = 0
    for i in range(12):
        total += plan[i] * cost_daily[i]

    if total >= costs[3]:
        print(int(costs[3]))
    else:
        print(int(total))


    # 1년권이 이득일 경우

    # 3달권이 이득일 경우

    # 1달권이 이득일 경우

    # 1일권이 이득일 경우
    for i in range(3):
