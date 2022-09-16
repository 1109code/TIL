# BOJ_11725 트리의 부모 찾기
# 2022-09-16
def dfs(n):
    global next
    while tree[n]:
        next.append(tree[n].pop())
        par[next] = n
        dfs(a)



N = int(input())
tree = [[] for _ in range(N + 1)]
par = [0 for _ in range(N + 1)]
next = []
for n in range(N):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)