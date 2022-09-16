# swea_4012 요리사 문제풀이
# 2022-09-16

def dfs(elements, start, k):
    if k == 0:
        results.append(elements[:])

    for i in range(start, N):
        elements.append(i)
        dfs(elements, i + 1, k - 1)
        elements.pop()

T = int(input())

for t in range(T):
    results = []
    N = int(input())

    foods = []
    for i in range(N):
        foods.append(list(map(int, input().split())))

    dfs([], 0, N//2)

    answer = 20000

    for r in results:
        A = 0
        B = 0
        reverse = []
        for n in range(N):
            if n not in r:
                reverse.append(n)

        for n in range(N):
            if n in r:
                for i in r:
                    if i != n:
                        A += foods[n][i]

            else:
                for i in reverse:
                    if i != n:
                        B += foods[n][i]

        if abs(A-B) < answer:
            answer = abs(A-B)

    print('#{0} {1}'.format(t+1, answer))