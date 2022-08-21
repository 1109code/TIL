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
    length[i] = y[i] * 2


rectangles = []
# center = x[0]
length = abs(y[0] * 2)
rectangles.append([length])

# for i in range(x[1], x[-1] + 1):
#     if i in x:
#         # center = i
#         length = abs(y[0] * 2)
#         j = 1
#         while rectangles[-1] + length < x[i]- x[i-j]:
#             rectangles.pop[-1]
#             rectangles.append[x[i] - x[i-j]]

#             j += 1

#         if 

rectangles = []
length = abs(y[i] * 2)
rectangles.append([length])

for i in range(1, N):
    length = abs(y[i]*2)
    j = 1
    while rectangles[-1] + length < x[i] - x[i-j]:
        rectangles.pop[-1]
        rectangles.append[x[i] - x[i-j]]

rectangles = []
rectangles.append[length[0]]

left = 0
right = 0


while True:
    right += 1
    if rectangles[-1] + length[right] > right - left:
        rectangles.pop()
        rectangles.append(right - left)
    else:
        


# 인접 x값 차이 
# 최대 절대 2y값

# 투포인터, left, right

# 최소 x좌표 부터 기지국 중심값 한칸씩 옮기면서?
# 점 만나면 이전 사각형이랑 합치는게 이득인지 비교