# BOJ_10163 문제풀이
# 2022-08-09

N = int(input())



x1, y1, width, height = [], [], [], []

max_x1 = 0
max_y1 = 0
min_x1 = 1001
min_y1 = 1001
for k in range(N):
    cord = list(map(int, input().split()))
    
    x1.append(cord[0])
    y1.append(cord[1])
    width.append(cord[2])
    height.append(cord[3])

    if x1[k] + width[k] > max_x1:
        max_x1 = x1[k] + width[k]
    if y1[k] + height[k] > max_y1:
        max_y1 = y1[k] + height[k]
    if x1[k] < min_x1:
        min_x1 = x1[k]
    if y1[k] < min_y1:
        min_y1 = y1[k]

board = [[0]*(max_x1-min_x1+1) for i in range(max_y1-min_y1+1)]

for k in range(N):
    for i in range(y1[k]-min_y1, y1[k]-min_y1 + height[k]):
        for j in range(x1[k]-min_x1, x1[k]-min_x1 + width[k]):
            board[i][j] = k + 1

for k in range(N):
    cnt = 0
    for i in range(y1[k]-min_y1, y1[k]-min_y1 + height[k]):
        for j in range(x1[k]-min_x1, x1[k]-min_x1 + width[k]):
            if board[i][j] == k + 1:
                cnt += 1
    print(cnt)