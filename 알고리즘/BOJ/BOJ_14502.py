# BOJ_14502 연구소 문제풀이
# 2022-09-26
from collections import deque
# 바이러스 퍼트리기


def virus():
    visited = [[0] * M for _ in range(N)]
    q = deque()

    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                q.append([i, j])
                visited[i][j] = 1

    while q:                                        # BFS로 바이러스 퍼뜨리기
        i, j = q.popleft()
        for l, m in d:
            if 0 <= i + l < N and 0 <= j + m < M:
                if board[i + l][j + m] == 0 and visited[i + l][j + m] == 0:
                    q.append([i + l, j + m])
                    visited[i + l][j + m] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and board[i][j] == 0:
                cnt += 1

    return cnt


# 안전지역 세기
# def safe():
#
# 벽 세우기
def wall(c):
    global cnt_max

    if c == 3:
        a = virus()
        if cnt_max < a:
            cnt_max = a
        return

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                wall(c+1)
                board[i][j] = 0


N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
cnt_max = 0

d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# 벽 세울 위치 찾기
wall(0)
print(cnt_max)