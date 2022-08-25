N = int(input())
info = [[] for i in range(6)]

for i in range(6):
    direction, length = map(int, input().split())
    info[i][0].append(direction)
    info[i][1].append(length)



'''
상하 3
좌우 3
'''
ver = []
hor = []
for i in range(6):
    if info[i][0] == (3 or 4):
        ver.append(info[i])
    else:
        hor.append(info[i])


'''
아 아 위
아 위 아
위 아 아

위 위 아
위 아 위
아 위 위

상 상 하
상 하 상
하 상 상

하 하 상
하 상 하
상 하 하
'''