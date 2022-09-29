import collections
graph = collections.defaultdict(list)

for u, v, w in times:
    graph[u].append((v, w))

Q = [(0, K)]
dist = collections.defaultdict(int)
