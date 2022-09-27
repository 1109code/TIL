# swea_1865 동철이의 일 분배
# 2022-09-27

def work(s, cur_pos):                               
    global max_pos

    if s == N:                                              # 모든 일이 배정 됐을 때 확률이 최대 확률보다 크면 초기화
        if cur_pos > max_pos:
            max_pos = cur_pos
            return
        else:                                               # 아니면 그냥 나가기
            return

    if cur_pos <= max_pos:                                  # (백트랙킹) 중간에 이미 최대 확률보다 작아졌으면 탈출
        return

    for n in range(N):
        if visited[n] == 0 and pcts[s][n] != 0:             # 배정한 적이 없고 확률이 0이 아니면
            cur_pos *= (pcts[s][n] / 100)                   # 현재까지의 확률에 곱해주기
            visited[n] = 1                                  # 방문 표시

            work(s + 1, cur_pos)                            # 재귀

            cur_pos /= (pcts[s][n] / 100)                   # 재귀 탈출 후 다시 원래대로 나눠주기
            visited[n] = 0                                  # 방문 표시 해제


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    max_pos = 0
    visited = [0] * N

    pcts = [list(map(float, input().split())) for _ in range(N)]        # 성공 확률 입력
    work(0, 1)

    print(f'#{tc} {max_pos * 100:.6f}')