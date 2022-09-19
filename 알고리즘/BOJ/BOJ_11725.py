# BOJ_11725 트리의 부모 찾기
# 2022-09-16
import sys
sys.setrecursionlimit(10**6)

def dfs(s):
    while tree[s]:
        p = tree[s].pop()
        tree[p].remove(s)
        par[p] = s
        dfs(p)


N = int(input())

tree = [[] for _ in range(N + 1)]
par = [0 for _ in range(N + 1)]

for n in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1)
for i in range(2, N+1):
    print(par[i])