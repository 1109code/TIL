# swea_1865 동철이의 일 분배
# 2022-09-27

def work(s, cur_pos):
    global max_pos

    if s == N:
        if cur_pos > max_pos:
            max_pos = cur_pos
            return
        else:
            return

    if cur_pos <= max_pos:
        return

    for n in range(N):
        if visited[n] == 0 and pcts[s][n] != 0:
            cur_pos *= (pcts[s][n] / 100)
            visited[n] = 1

            work(s + 1, cur_pos)

            cur_pos /= (pcts[s][n] / 100)
            visited[n] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    max_pos = 0
    visited = [0] * N

    pcts = [list(map(float, input().split())) for _ in range(N)]
    work(0, 1)

    print(f'#{tc} {max_pos * 100:.6f}')