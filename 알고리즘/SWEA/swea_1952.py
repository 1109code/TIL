# swea_1952 수영장 문제풀이
# 2022-09-23

T = int(input())

for tc in range(1, T + 1):
    costs = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    monthly_costs = []

    for i in range(12):
        monthly_costs.append(costs[0] * plan[i])
    monthly_costs.extend([0, 0])

    for i in range(12):
        if monthly_costs[i] >= costs[1]:
            monthly_costs[i] = costs[1]

    dp = [30*3000] * 14
    for i in range(3):
        tri_sum = sum(monthly_costs[:i+1])
        dp[i] = min(costs[2], tri_sum)

    for i in range(3, 14):
        dp[i] = min(dp[i-3] + costs[2], dp[i-1] + monthly_costs[i])

    if dp[-1] > costs[-1]:
        dp[-1] = costs[-1]
    print(f'#{tc} {dp[-1]}')
