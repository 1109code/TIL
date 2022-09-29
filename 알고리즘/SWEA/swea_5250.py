# swea_5250 최소 비용 문제풀이
# 2022-09-29
from collections import deque
def bfs():
    global q, visited

    while q:
        cur = q.popleft()                                                       # 현재 위치
        for di, dj in d:                                                        # 델타탐색
            ni = cur[0] + di
            nj = cur[1] + dj
            if 0 <= ni < N and 0 <= nj < N:                                     # 판 안에 델타탐색이 위치하면
                diff = 0                                                        # 다음 타겟과 현재 타겟의 차이
                if board[ni][nj] - board[cur[0]][cur[1]] > 0:                   # 다음 타겟이 더 높으면
                    diff = board[ni][nj] - board[cur[0]][cur[1]]                # 차이 저장

                if visited[ni][nj] > visited[cur[0]][cur[1]] + diff + 1:        # 다음 타겟이 이번에 저장될 값보다 클 때만
                    visited[ni][nj] = visited[cur[0]][cur[1]] + diff + 1        # 값 저장
                    q.append([ni, nj])                                          # 다음 위치 큐에 추가


T = int(input())
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for tc in range(1, T + 1):
    q = deque([[0, 0]])                                                         # bfs에 활용할 큐

    N = int(input())
    cnt_min = 1000 * (N ** 2)

    board = [list(map(int, input().split())) for _ in range(N)]                 # 입력 판
    visited = [[1000 * (N ** 2)] * N for _ in range(N)]                         # 방문할 곳 최대치로 초기화
    visited[0][0] = 0                                                           # 시작점은 0

    bfs()
    print(f'#{tc} {visited[N-1][N-1]}')