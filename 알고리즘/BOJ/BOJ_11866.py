# BOJ_11866 요세푸스 문제 0
# 2022-08-29

N, K = map(int, input().split())

numbers = []
for i in range(N):
    numbers.append(i+1)

answer = []
now = 0
while numbers:
    for i in range(K-1):
        if numbers:
            numbers.append(numbers.pop(0))
        else:
            break
    if numbers:
        answer.append(numbers.pop(0))

print('<', end='')
print(*answer, sep=', ', end='')
print('>')