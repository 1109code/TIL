import random
height = []
for i in range(9):
    height.append(int(input()))
print(height)

# 제거 대상
answer = []
for i in range(9):
    for j in range(9):
        if i == j:
            pass
        else:
            height_sum = sum(height)-height[i]-height[j]
            if height_sum == 100:
                for k in range(9):
                    if k != (i and j):
                        answer.append(height[k])
                        break
        height_sum = 0
print(answer)
answer = answer.sort()
for i in range(7):
    print(answer[i])