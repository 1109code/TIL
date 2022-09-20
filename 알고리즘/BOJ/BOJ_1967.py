# BOJ_1967 트리의 지름 문제푸리
# 2022-09-20
def post(n):
    global max_len
    if n:
        for i in ch[n]:
            post(i)
        cur_sum = 0

        for i in ch[n]:
            if
cur_len[i] + length[i]

        if cur_sum >= max_len:
            max_len = cur_sum

        for i in ch[n]:
            if cur_len[i] + length[i] >= cur_len[n]:
                cur_len[n] = cur_len[i] + length[i]


N = int(input())

ch = [[] for _ in range(N + 1)]

# par = [0 for _ in range(N + 1)]
length = [0 for _ in range(N + 1)]
cur_len = [0 for _ in range(N + 1)]
max_len = 0

for e in range(N - 1):
    info = list(map(int, input().split()))
    ch[info[0]].append(info[1])
    # par[info[1]] = info[0]
    length[info[1]] = info[2]

post(1)
print(max_len)