# swea_2300 문제풀이
# 2022-08-19

N = int(input())

cord = []
x = []
y = []
for i in range(N):
    cord.append(list(map(int, input().split())))

cord.sort()

for i in range(N):
    x.append(cord[i][0])
    y.append(cord[i][1])


length = []
for i in range(N):
    length.append(abs(y[i]*2))

rect = []
rect.append(length[0])

left = 0
right = 0

while True:
    right += 1
    if x[right] - length[right] < x[right-1]:
        length[right] = x[right] - x[right-1]
        if rect[-1] + length[right] > x[right]-x[left]:
            rect.pop()
            rect.append(x[right]-x[left])
        else:
            length[right] = abs(y[right]*2)
            rect.append(length[right])
            left = right
            
    else:
        if rect[-1] + length[right] > x[right]-x[left]:
            rect.pop()
            rect.append(x[right]-x[left])
        else:
            rect.append(length[right])
            left = right

    if right == N-1:
        break

print(rect)


# 기지국 개수?
# y축?