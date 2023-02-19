# 2023-02-05 소문난 칠공주 문제풀이
from sys import stdin
input = stdin.readline

# 우하좌상
dr = [0, 1, 0, -1,]
dc = [1, 0, -1, 0,]
answer = ''
cnt = 0

def check(cur):
    global answer
    global cnt

    answer += board[cur[0]][cur[1]]
    # print(answer)
    visited[cur[0]][cur[1]] = 1

    if len(answer) == 7:
        if answer.count('S') > 3:
            cnt += 1
            answer = answer[:6]
            visited[cur[0]][cur[1]] = 0
            return
        answer = answer[:6]
        visited[cur[0]][cur[1]] = 0
        return

    if answer.count('Y') > 3:
        visited[cur[0]][cur[1]] = 0
        answer = answer[:-1]
        return
    
    for d in range(4):
        nr = cur[0] + dr[d]
        nc = cur[1] + dc[d]
        if 0 <= nr < 5 and 0 <= nc < 5:
            if visited[nr][nc] == 0:
                check([nr, nc])

board = [input() for _ in range(5)]
visited = list([0 for _ in range(5)] for _ in range(5))

for i in range(5):
    for j in range(5):
        check([i, j])
        print(answer)

print(cnt)
