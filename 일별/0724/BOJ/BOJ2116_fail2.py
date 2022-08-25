N = int(input())


dice_list = []
for i in range(N):
    dice_list.append(list(map(int, input().split())))

def opposite(bot):
    if bot == 0 or bot == 5:
        top = 5 - bot
    elif bot == 1 or bot == 3:
        top = 4 - bot
    else:
        top = 6 - bot
    return top

#첫 번째 주사위 정하기
front = dice_list[0].index(6)
print(f'front = {front}')
back = opposite(front)
print(f'bakc = {back}')
del dice_list[0][back]
print(f'dice_list = {dice_list}')
del dice_list[0][dice_list[0].index(6)]
print(f'dice_list = {dice_list}')


max_sum = 0
for top in dice_list[0]:
    sum = 0
    for j in range(1, N):
        bot = dice_list[j].index(top)
        top = dice_list[j].index(dice_list[j].index(opposite(top)))

        print(top)
        print(bot)
        del dice_list[j][dice_list[j].index(bot)]
        print(f'dice_list ={dice_list[j]}')
        del dice_list[j][dice_list[j].index(top)]
        print(f'dice_list ={dice_list[j]}')
        sum += max(dice_list[j])
    if sum > max_sum:
        max_sum = sum

print(max_sum)