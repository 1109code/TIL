# swea_5250 최소 비용 문제풀이
# 2022-09-29
from collections import deque


def bfs():
    global visited, q, cnt_min
    q.append([0, 0, 0])

    while q:
        cur = q.popleft()

        if cur[0] == N-1 and cur[1] == N-1:
            if cur[2] < cnt_min:
                cnt_min = cur[2]
            continue

        if cur[2] <= cnt_min:
            for i, j in d:
                if 0 <= cur[0] + i < N and 0 <= cur[1] + j < N and visited[cur[0] + i][cur[1] + j] == 0:
                    if board[cur[0] + i][cur[1] + j] - board[cur[0]][cur[1]] > 0:
                        cur[2] += board[cur[0] + i][cur[1] + j] - board[cur[0]][cur[1]]
                    visited[cur[0] + i][cur[1] + j] = 1
                    q.append([cur[0] + i, cur[1] + j, cur[2] + 1])


T = int(input())
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]


for tc in range(1, T):
    q = deque()

    N = int(input())
    cnt_min = 1000 * (N ** 2)

    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    bfs()
    print(cnt_min)