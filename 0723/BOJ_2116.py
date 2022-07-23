N = int(input())

# 다이스들 담기
dice_list = []
for i in range(N):
    dice_list.append(list(map(int, input().split())))

# 

front = [0 for i in range(N)]
back = [0 for i in range(N)]
top = [0 for i in range(N)]

front[0] = dice_list[0].idx(6)

if front[0] == 0 or 5:
    back[0] = dice_list[5]
elif dice_list[0].idx(6) == 1 or 3:
    back[]
for i in range(6):
    