# BOJ_11000 강의실 배정 문제풀이
# 2022-09-22

N = int(input())


classes = [list(map(int, input().split())) for _ in range(N)]

classes.sort(key=lambda x: x[1])

c_len = len(classes)

visited = [0 for i in range(c_len)]

room = 0
while sum(visited) < c_len:

    end = 0
    for i in range(c_len):
        if visited[i] == 0:
            start = classes[i][0]
            if start >= end:
                visited[i] = 1
                end = classes[i][1]

    room += 1

print(room)