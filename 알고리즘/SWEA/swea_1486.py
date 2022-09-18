# swea_1486 장훈이의 높은 선반 문제풀이
# 2022-09-16

T = int(input())

for t in range(T):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    answer = [B for _ in range(1<<N)]
    min_answer = []
    for i in range(1<<N):
        for j in range(N):
            if i & (1<<j):
                answer[i] -= heights[j]
        if answer[i] <= 0:
            min_answer.append(abs(answer[i]))

    print('#{0} {1}'.format(t+1, min(min_answer)))