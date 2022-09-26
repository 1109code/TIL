# swea_5188 최소합 문제풀이
# 2022-09-21
def min_search(pos):
    global ans_list

    now = 0
    while now < 7:
        now += 1
        for i in range(len(pos)):
            for di, dj in d:
                if 0 <= pos[i][0] + di < N and 0 <= pos[i][1] + dj < N:
                    pos.append([pos[i][0] + di, pos[i][1] + dj])
                    ans_list.append(ans_list[now] + board[pos[i][0] + di][pos[i][1] + dj])
            pos.pop(0)



T = int(input())
d = [[0, 1], [1, 0]]

for tc in range(1, T+1):
    ans_list = [[] for _ in range(7)]

    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    ans_list[0] = board[0][0]

    min_search([[0, 0]])

    print(f'#{tc} {min(ans_list[-1])}')