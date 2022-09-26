# swea_2819 격자판의 숫자 이어 붙이기 문제풀이
# 2022-09-21
import sys
sys.setrecursionlimit(10**6)


def search(i, j):
    global answer, cur_ans, board, cnt
    if len(cur_ans) == 7:
        if cur_ans not in answer:
            cnt += 1
            answer.append(cur_ans[:])
        return

    for n, m in d:
        if 0 <= i + n < 4 and 0 <= j + m < 4:
            cur_ans.append(board[i + n][j + m])
            search(i + n, j + m)
            cur_ans.pop()


T = int(input())

d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for t in range(T):
    board = []
    cur_ans = []
    answer = []
    cnt = 0

    for i in range(4):
        board.append(list(map(int, input().split())))

    for i in range(4):
        for j in range(4):
            search(i, j)

    print(f'#{t+1} {cnt}')