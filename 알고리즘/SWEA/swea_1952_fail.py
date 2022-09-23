# swea_1952 수영장 문제풀이
# 2022-09-23

T = int(input())

for tc in range(1, T + 1):
    costs = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    cost_daily = [0] * 14

