N = int(input())
info = [[] for i in range(6)]

for i in range(6):
    direction, length = map(int, input().split())
    info[i].append(direction)
    info[i].append(length)

# 방향이 2번만에 180도 바뀌면 빼야하나?