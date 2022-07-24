N = int(input())

# 기둥 입력
columns = []

for i in range(N):
    col = list(map(int, input().split()))
    columns.append(col)
print(columns)
cloumns = columns.sort()
print(columns)

max [0, 0]
for i in range(N):
    if columns[i][1] > max[1]:
        max = columns[i]
area_sum = 0


for i in range(N-1):
    height = columns[i][1]
    area_sum += height * 


# 지금 이후 가장 높은 기둥
pos = [0 for i in range(N)]
height = [0 for i in range(N)]
for i in range(N):
    pos[i] = columns[i][0]
    height[i] = columns[i][1]

max_height = max(height)
print(max_height)

max_pos = pos[height.index(max_height)]
print(max_pos)

for i in range:

# 첫 기둥 높이부터 수평으로 쭉 가다가 더 높은 숫자 만나면 올라가기
area = 0
area_sum = 0
for i in range(max(pos)):
    
    
# 가장 높은 기둥 만나면 그때부턴 남은 것들 중 최대값 까지 쭉 가기
