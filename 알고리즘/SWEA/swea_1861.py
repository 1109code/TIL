# swea_1861 정사각형 방 문제풀이
# 2022-09-16
def bfs():
    global answer_list
    global cnt
    global answer

    r = len(answer_list)
    while True:
        cnt += 1
        answer = []
        for i in range(r):
            pos = answer_list.pop(0)
            answer.append(pos)
            for di, dj in d:
                if 0 <= pos[0] + di < N and 0 <= pos[1] + dj < N and board[pos[0]][pos[1]] - 1 == board[pos[0] + di][pos[1] + dj]:
                    answer_list.append([pos[0]+di, pos[1]+dj])
        r = len(answer_list)
        if r == 0:
            break


T = int(input())

for t in range(T):
    N = int(input())
    board = []

    for n in range(N):
        board.append(list(map(int, input().split())))

    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    cnt = 1
    answer_list = []
    answer = []
    for i in range(N):
        for j in range(N):
            answer_list.append([i, j])

    bfs()

    min = board[answer[0][0]][answer[0][1]]
    for i in answer:
        if board[i[0]][i[1]] <= min:
            min = board[i[0]][i[1]]

    print('#{0} {1} {2}'.format(t+1, min, cnt-1))