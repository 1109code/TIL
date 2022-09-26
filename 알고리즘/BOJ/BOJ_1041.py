# BOJ_1041 주사위 문제풀이
# 2022-09-26

N = int(input())
dice = list(map(int, input().split()))
num_sum = 0

if N == 1:
    print(sum(dice) - max(dice))

else:
    # 1면만 보이는 경우
    # 5N^2 - 16N + 12
    num_sum += min(dice) * (5 * (N ** 2) - 16 * N + 12)

    # 2면이 보이는 경우
    # 8N - 16
    # 2면이 붙어 있는데 최소인 경우 찾기
    two_min = 100

    for i in range(6):
        for j in range(i+1, 6):
            if (i == 0 and j == 5) or (i == 1 and j == 4) or (i == 2 and j == 3):
                pass
            else:
                if dice[i] + dice[j] < two_min:
                    two_min = dice[i] + dice[j]

    num_sum += two_min * (8 * N - 12)

    # 3면이 보이는 경우
    # 4
    three_min = 150
    dice_nums = [1, 2, 4, 3, 1]

    for i in range(4):
        if dice[0] + dice[dice_nums[i]] + dice[dice_nums[i + 1]] < three_min:
            three_min = dice[0] + dice[dice_nums[i]] + dice[dice_nums[i + 1]]

        if dice[-1] + dice[dice_nums[i]] + dice[dice_nums[i + 1]] < three_min:
            three_min = dice[-1] + dice[dice_nums[i]] + dice[dice_nums[i + 1]]

    num_sum += three_min * 4

    print(num_sum)

