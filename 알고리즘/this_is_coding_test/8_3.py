# tict_8_3 개미 전사 문제풀이
# 2022-09-23

N = int(input())
container = list(map(int, input().split()))
# dp 활용을 위한 공간
dp = [0] * N

# 0번째와 1번째 초기화
dp[0] = container[0]
# 1번째는 0번째와 1번째 중 최대값
dp[1] = max(dp[0], container[1])

# 이전 위치를 털었으면 현재 위치를 털 수 없고
# 전전 위치를 털었으면 현재 위치를 털 수 있음
# 따라서 현재 위치의 dp는 이전과, 전전 위치 + 현재 위치 의 값
for i in range(2, N):
    dp[i] = max(dp[i-1], dp[i-2] + container[i])

print(dp[N-1])