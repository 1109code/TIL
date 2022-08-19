# BOJ_2300 기지국 문제풀이
# 2022-08-18

# 통신폭 = 한 변 길이
# 설치비용 = 통신폭의 합

N = int(input())
cord = [[] for i in range(N)]
x = [0 for i in range(N)]
y = [0 for i in range(N)]
length = [0 for i in range(N)]

for i in range(N):
    cord[i] = list(map(int, input().split()))
    
cord.sort()

for i in range(N):
    x[i], y[i] = cord[i][0], cord[i][1]
    length[i] = abs(y[i] * 2)

rectangles = []
rectangles.append(length[0])
left = 0
right = 0
while True:
    right += 1
    if (rectangles[-1] + length[right] > x[right] - x[left]) and (abs(y[right-1]) <= abs(y[right])):
        rectangles.pop()
        rectangles.append(x[right] - x[left])
        print(rectangles)
    else:
        rectangles.append(length[right])
        left = right
        print(rectangles)
    if right == N-1:
        break

print(sum(rectangles))
# 2차이가 나야됨
        


# 인접 x값 차이 
# 최대 절대 2y값

# 투포인터, left, right

# 최소 x좌표 부터 기지국 중심값 한칸씩 옮기면서?
# 점 만나면 이전 사각형이랑 합치는게 이득인지 비교


# 전체에서 자르기?
