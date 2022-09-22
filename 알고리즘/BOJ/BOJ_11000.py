# BOJ_11000 강의실 배정 문제풀이
# 2022-09-22

N = int(input())


classes = [list(map(int, input().split())) for _ in range(N)]

classes.sort(key=lambda x: x[1])
room = [0]

for c in classes:
    flag = 0

    for i in range(len(room)):
        if c[0] >= room[i]:
            room[i] = c[1]
            flag = 1
            break

    if flag == 0:
        room.append(c[1])

print(len(room))