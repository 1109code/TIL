# swea_5188 최소합 문제풀이
# 2022-09-21
def min_search(i, j, cur_sum):
    global sum_min

    if i == N-1 and j == N-1:               # 탈출 조건 ( 가장 오른쪽 아래 도착 시)
        if cur_sum <= sum_min:              # 해당 경로의 합이 최소합 보다 작으면 최소합 초기화
            sum_min = cur_sum
        return

    if cur_sum > sum_min:                   # 중간에 최소합 보다 커지면 탈출
        return

    for di, dj in d:
        if 0 <= i + di < N and 0 <= j + dj < N:     # 판의 범위 내에 있으면
            min_search(i + di, j + dj, cur_sum + board[i + di][j + dj]) # 재귀로 dfs


T = int(input())
d = [[0, 1], [1, 0]]

for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]     # 판 입력

    sum_min = 13 * 10                                               # 판의 모든 값을 더했을 때를 최소합으로 초기화

    min_search(0, 0, board[0][0])                                   # dfs 돌기

    print(f'#{tc} {sum_min}')