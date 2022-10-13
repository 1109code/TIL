# swea_2382 미생물 격리 문제풀이
# 2022-09-30

# 미생물 이동
def move():
    visited = [[0] * N for _ in range(N)]
    for bug in bugs:
        cur_idx = [bug[0], bug[1]]
        next_idx = [bug[0] + direction[bug[4]][0], bug[1] + direction[bug[4]][1]]
        if visited[next_idx[0], next_idx[1]] == 1:
            if board[next_idx[0]][next_idx[1]][0] > bug[0]:
                bug


T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())

    direction = {
        1: [-1, 0],
        2: [1, 0],
        3: [0, -1],
        4: [0, 1],
    }

    board = [([] for _ in range(N)) for _ in range(N)]
    bugs = []
    for i in range(9):
        bugs.append([map(int, input().split()), i + 1])
        board[bugs[i][0]][bugs[i][1]] = [bugs[i][2], bugs[i][3]]



