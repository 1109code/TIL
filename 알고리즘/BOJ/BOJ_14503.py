# BOJ_14503 로봇 청소기 문제풀이
# 2022-12-01

N, M = map(int, input().split())

robot = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]
cnt = 1

# 사방향 0: 북, 1: 동, 2: 남, 3: 서
d = [[0, -1], [-1, 0], [0, 1], [1, 0]]
b = [[1, 0], [0, -1], [-1, 0], [0, 1]]

while True:
    # 선 청소
    if board[robot[0]][robot[1]] == 0:
        cnt += 1
        board[robot[0]][robot[1]] = cnt

    # 사방향 탐색
    s = 0
    flag = 0
    while s != 4:
        s += 1
        # 
        if board[robot[0] + d[robot[2]][0]][robot[1] + d[robot[2]][1]] == 0:
            # 이동
            robot = [robot[0] + d[robot[2]][0], robot[1] + d[robot[2]][1], (robot[2] + 3) % 4]
            flag = 1
            break
        else:
            # 회전
            robot[2] = (robot[2] + 3) % 4
    
    if flag != 1:
        # 후진
        if board[robot[0] + b[robot[2]][0]][robot[1] + b[robot[2]][1]] != 1:
            robot = [robot[0] + b[robot[2]][0], robot[1] + b[robot[2]][1], robot[2]]
        else:
            break
print(cnt-1)