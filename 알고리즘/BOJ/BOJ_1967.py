# BOJ_1967 트리의 지름 문제풀이
# 2022-09-20

def search(s):
    global max_len, target, cur_len, ch

    if s:
        for child in ch[s]:
            if visited[child[1]] == 0:
                visited[child[1]] += 1
                cur_len += child[0]

                if cur_len >= max_len:
                    max_len = cur_len
                    target = child[1]

                search(child[1])

                cur_len -= child[0]
                visited[child[1]] -= 1


N = int(input())

nodes = [0]

ch = [[] for _ in range(N + 1)]
length = [0] * (N + 1)
cur_len = 0
max_len = 0
target = 0
visited = [0] * (N + 1)


for i in range(N-1):
    info = list(map(int, input().split()))
    ch[info[0]].append([info[2], info[1]])
    ch[info[1]].append([info[2], info[0]])


search(1)
search(target)

print(max_len)