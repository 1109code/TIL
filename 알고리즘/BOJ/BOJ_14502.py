# BOJ_14502 연구소 문제풀이
# 2022-09-26

# 바이러스 퍼트리기
def virus(s):
    global virus_lab
    for i, j in d:
        if 0 <= s[0] + i < N and 0 <= s[1] + j < M:
            if virus_lab[s[0] + i][s[1] + j] == 0:
                virus_lab[s[0] + i][s[1] + j] = 2
                virus([s[0] + i, s[1] + j])


# 안전지역 세기
# def safe():
#
# # 벽 세우기
# def wall():

N, M = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(N)]

# ㄷㄷ 브루트 포스로 하라고?
# 일단 ㄱ
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

virus_lab = [[0] * M for _ in range(N)]
for n in range(N):
    for m in range(M):
        if lab[n][m] == 2:
            virus([n, m])

print(virus_lab, lab)