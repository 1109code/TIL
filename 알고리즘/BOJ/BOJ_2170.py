# boj_2170 선긋기 문제풀이
# 2022-08-24

N = int(input())
line = [list(map(int, input().split()))]

for i in range(1, N):
    x, y = map(int, input().split())
    for j in range(len(line)):
        if x < line[j][0] <= y and x < line[j][1] <= y:
            pass
        elif x < line[j][0] < y:
            line[j] = [x, line[j][1]]
        elif x < line[j][1] < y:
            line[j] = [line[j][0], y]
cnt = 0
for length in line:
    cnt += length[1] - length[0] + 1

print(cnt)