# tict_8_2 문제풀이
# 2022-09-23

X = int(input())
# 최대 입력값 만큼 초기화
dp = [0] * 300001

for i in range(2, X + 1):
    # 1을 빼는 경우
    # 이전 단계에 저장된 횟수 + 1
    dp[i] = dp[i - 1] + 1

    # 2로 나눠 떨어지는 경우
    # 현재 단계에 저장된 dp와 2로 나눴을 때 값의 dp에 저장된 횟수 + 1
    # 이하 동문
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)

print(dp[X])

for i in range(3):
