# swea_5248 그룹 나누기 문제풀이
# 2022-09-30
def find_set(x):
    global parent

    # if x != parent[x]:
    #     parent[x] = find_set(parent[x])
    #
    # return parent[x]

    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])


def union(x, y):
    global parent
    # link(find_set(x), find_set(y))
    parent[find_set(y)] = find_set(x)


# def link(x, y):
#     if rank[x] > rank[y]:
#         parent[y] = x
#     else:
#         parent[x] = y
#         if rank[x] == rank[y]:
#             rank[y] += 1


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    parent = [i for i in range(N + 1)]
    # rank = [0] * (N + 1)

    regis = list(map(int, input().split()))

    for i in range(0, 2 * M, 2):
        union(regis[i], regis[i + 1])

    cnt = set()
    for i in range(1, N + 1):
        cnt.add(find_set(i))


    print(f'#{tc} {len(cnt)}')