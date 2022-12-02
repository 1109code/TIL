# BOJ_15686 치킨 배달 문제풀이
# 2022-12-02
import sys
si = sys.stdin.readline

# 치킨집 중 M개 선택
def combination(arr, N): 
    result = []

    if N == 0:
        return [[]]
    else:
        for i in range(len(arr)):
            ch = [arr[i]]
            for j in combination(arr[i+1:], N-1):
                result.append(ch + j)
    return result    

# N: 도시크기, M: 폐업 X 치킨집 수
N, M = map(int, si().split())
# 도시 입력
city = [list(map(int, si().split())) for _ in range(N)]

# 도시 순회하며 치킨집 찾기
# 치킨집 리스트
chick = []
home = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chick.append([i, j])
        elif city[i][j] == 1:
            home.append([i, j])


chicken_combi = combination(chick, M)
answer = 9999999999999999

# 집 순회하며 거리 계산해 최소 찾기
for chickens in chicken_combi:
    chick_sum = 0
    for h in home:
        dist_min = 9999999999999999
        hi, hj = h[0], h[1]
        for c in chickens:
            ci, cj = c[0], c[1]
            dist = abs(ci-hi) + abs(cj-hj)
            if dist < dist_min:
                dist_min = dist
        chick_sum += dist_min
    if chick_sum < answer:
        answer = chick_sum

print(answer)
