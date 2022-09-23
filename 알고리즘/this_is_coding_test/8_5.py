# 8_5 효율적인 화폐 구성 문제풀이
# 2022-09-23

N, M = map(int, input().split())

coins = []
for n in range(N):
    coins.append(int(input()))

dp = [10001] * (M + 1)
dp[0] = 0

for i in range(N):                                  # 코인 종류 순회 하면서
    for j in range(coins[i], M + 1):                # 현재 코인 크기 부터 끝까지 순회하며
        dp[j] = min(dp[j - coins[i]] + 1, dp[j])    # 현재 dp - 코인 크기 + 1과 현재 저장된 dp 중 최솟값으로 초기화
                                                    # 코인 사용 순서가 상관 없기 때문에 2, 3, 3 과 3, 3, 2 는 동일 취급

if dp[M] == 10001:
    print(-1)
else:
    print(dp[M])