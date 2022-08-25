# 키들 담을 공간
height = []
# 키 담기
for i in range(9):
    height.append(int(input()))
# 정답 담을 공간
answer = []

height_sum = 0
# 0, 0 부터 8, 8 까지 다 돌며 제외할 키 2개 찾기 위해 이중 for 문
for i in range(9):
		# 정답이 구해지면 탈출하기 위한 if 문
    if height_sum == 100:
        break
    for j in range(9):
        height_sum = 0
				# i, j가 동일하면 한 명만 빠지기 때문에 pass
        if i == j:
            pass
				# 난쟁이 키들 중 i, j 키를 제외했을때 합이 100이면 answer에 더하고 탈출
        else:
            height_sum = sum(height)-height[i]-height[j]
            if height_sum == 100:
                for k in range(9):
                    if k != i and k != j:
                        answer.append(height[k])
                break
# 순서대로 정렬하기 위해 오늘 배운 sorted 활용
answer = sorted(answer)
for i in range(7):
    print(answer[i])