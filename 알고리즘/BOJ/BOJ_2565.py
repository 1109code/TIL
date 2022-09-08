# BOJ_2565 전깃줄
# 2022-09-05

N = int(input())


lines = [list(map(int, input().split())) for _ in range(N)]
lines.sort()
print(lines)

for i in range(N):
    if lines[i][1] > 