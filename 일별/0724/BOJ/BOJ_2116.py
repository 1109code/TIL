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

# 주사위 side로 올 수 있는 최대 값
def max_side(sides, top, bot):
    max_num = 0
    for i in range(6):
        if sides[i] == top or sides[i] == bot:
            pass
        else:
            if sides[i] > max_num:
                max_num = sides[i]
    return max_num

answer = 0
# 첫번째 다이스 top 을 1 ~ 6 까지 돌리기
for i in range(1,7):
    max_sum = 0
    top_num = i
    # 각각의 다이스들 옆면 최대값 가산
    for j in range(N):
        bot_num = top_num
        bot_idx = dice_list[j].index(bot_num)
        top_idx = opposite(bot_idx)
        top_num = dice_list[j][top_idx]
        
        max_number = max_side(dice_list[j], top_num, bot_num)
        max_sum += max_number
    
    if max_sum > answer:
        answer = max_sum
    
print(answer)