N = int(input())

dice_list = []
for i in range(N):
    dice_list.append(list(map(int, input().split())))

# 반대편 숫자 idx 반환
def opposite(idx):
    if idx == 0 or idx == 5:
        opp = 5 - idx
    elif idx == 1 or idx == 3:
        opp = 4 - idx
    else:
        opp = 6 - idx
    return opp

# 2번째 다이스 부터 side로 올 수 있는 최대 값
def max_side(sides, top, bot):
    max_num = 0
    for i in range(6):
        if sides[i] == top or sides[i] == bot:
            pass
        else:
            if sides[i] > max_num:
                max_num = sides[i]
    return max_num


# 첫 번째 다이스 6이 앞으로 오게
front_idx = dice_list[0].index(6)
front_num = dice_list[0][front_idx]

back_idx = dice_list[0].index(dice_list[0][opposite(front_idx)])
back_num = dice_list[0][back_idx]

# 이때 위로 올 수 있는 후보 4개 정하기
first_top = []
for i in range(1, 7):
    if i == front_num or i == back_num:
        pass
    else:
        first_top.append(i)

# 두번째 다이스부터 bot과 top 정하고 side 중 최대값 가산
answer = 0
for i in first_top:
    max_sum = 6
    top_num = i
    for j in range(1,N):
        bot_num = top_num
        bot_idx = dice_list[j].index(bot_num)
        top_idx = opposite(bot_idx)
        top_num = dice_list[j][top_idx]
        
        max_number = max_side(dice_list[j], top_num, bot_num)
        max_sum += max_number
        
    if max_sum > answer:
        answer = max_sum
    

print(answer)