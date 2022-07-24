N = int(input())

# 다이스들 담기
dice_list = []
for i in range(N):
    dice_list.append(list(map(int, input().split())))
# 
front = [0 for i in range(N)]
back = [0 for i in range(N)]
bot = [0 for i in range(N)]
top = [0 for i in range(N)]

#주사위 배열
def order(front):
    if front == 0 or 5:
        back = 5 - front
        top = 
    elif front == 1 or 3:
        back = 4 - front
        side = [0, 2, 4, 5]
    else:
        back = 6 - front
        side = [0, 1, 3, 5]
    return back, side

front[0] = dice_list[0].idx(6)