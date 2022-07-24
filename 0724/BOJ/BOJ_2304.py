N = int(input())
columns = []

for i in range(N):
    col = list(map(int, input().split()))
    columns.append(col)
cloumns = columns.sort()

graph = [0 for i in range(columns[-1][0]+1)]

for i in range(len(columns)):
    graph[columns[i][0]] = columns[i][1]

max_idx = graph.index(max(graph))
area = 0
height = 0
for i in range(max_idx):
    if graph[i] > height:
        height = graph[i]
    area += height

height = 0
for i in range(len(graph)-1, max_idx-1, -1):
    if graph[i] > height:
        height = graph[i]
    area += height
print(area)